from django.shortcuts import render,redirect
from ecommerceapp.models import Contact,Product,OrderUpdate,Orders, Rating 
from django.contrib import messages
from math import ceil
from ecommerceapp import keys
from django.conf import settings
MERCHANT_KEY=keys.MK
import json
from django.views.decorators.csrf import  csrf_exempt
from PayTm import Checksum
from django.db.models import Avg, Count 
from django.contrib.auth.decorators import login_required

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        
        for item in prod:
            ratings = item.ratings_set.all()
            avg_rating = ratings.aggregate(Avg('stars'))['stars__avg']
            rating_count = ratings.count()
            
            item.avg_rating = round(avg_rating, 1) if avg_rating is not None else 0.0
            item.rating_count = rating_count
            
            stars_list = []
            if item.avg_rating > 0:
                for j in range(1, 6):
                    if item.avg_rating >= j:
                        stars_list.append('full')
                    elif item.avg_rating >= j - 0.5:
                        stars_list.append('half')
                    else:
                        stars_list.append('empty')
            else:
                stars_list = ['empty'] * 5
                
            item.stars_list = stars_list

            if request.user.is_authenticated:
                user_rating = ratings.filter(user=request.user).first()
                item.user_rating = user_rating.stars if user_rating else 0
            else:
                item.user_rating = 0
                
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
        
    params = {'allProds': allProds}
    return render(request, "index.html", params)


@login_required(login_url='/auth/login/')
def rate(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        rating_value = int(request.POST.get('rating'))
        user = request.user
        
        try:
            product = Product.objects.get(id=product_id)
            existing_rating = Rating.objects.filter(user=user, product=product).first()
            if existing_rating:
                existing_rating.stars = rating_value
                existing_rating.save()
                messages.success(request, f"Your rating for {product.product_name} has been updated to {rating_value} stars.")
            else:
                new_rating = Rating(product=product, user=user, stars=rating_value)
                new_rating.save()
                messages.success(request, f"Your rating of {rating_value} stars for {product.product_name} has been saved.")
        except Product.DoesNotExist:
            messages.error(request, "Product not found.")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    return redirect('/')

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        pnumber=request.POST.get("pnumber")
        myquery=Contact(name=name,email=email,desc=desc,phonenumber=pnumber)
        myquery.save()
        messages.info(request,"we will get back to you soon..")
        return render(request,"contact.html")

    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")


def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')

    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        Order = Orders(items_json=items_json,name=name,amount=amount, email=email, address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
        print(amount)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id,update_desc="the order has been placed")
        update.save()
        thank = True
        id = Order.order_id
        oid=str(id)+"ShopyCart"
        param_dict = {
            'MID':keys.MID,
            'ORDER_ID': oid,
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})

    return render(request, 'checkout.html')


@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            a=response_dict['ORDERID']
            b=response_dict['TXNAMOUNT']
            rid=a.replace("ShopyCart","")
           
            print(rid)
            filter2= Orders.objects.filter(order_id=rid)
            print(filter2)
            print(a,b)
            for post1 in filter2:
                post1.oid=a
                post1.amountpaid=b
                post1.paymentstatus="PAID"
                post1.save()
            print("run agede function")
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login & Try Again")
        return redirect('/auth/login')

    currentuser = request.user.username
    items = Orders.objects.filter(email=currentuser)
    rid = ""
    delivered_count = 0

    for i in items:
        print(i.oid)
        myid = i.oid
        rid = myid.replace("ShopyCart", "").strip()
        print(rid)

    status = []

    if rid.isdigit():
        status = OrderUpdate.objects.filter(order_id=int(rid))
        for j in status:
            print(j.update_desc)
            if j.delivered:
                delivered_count += 1
    else:
        print("Invalid or empty order ID:", repr(rid))

    context = {
        "items": items, 
        "status": status,
        "delivered_count": delivered_count
    }
    return render(request, "profile.html", context)