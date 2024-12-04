from django.shortcuts import render,redirect
from capp.models import productdb,categorydb
from webapp.models import contactdb,signupdb,cartdb,orderdb
from django.contrib import messages
import razorpay

def home(request):
    cat=categorydb.objects.all()
    return render(request,'home.html',{'cat':cat})
def product_page(request):
    pro=productdb.objects.all()
    return render(request,'product_page.html',{'pro':pro})

def about_page(request):
    return render(request,'about_page.html')
def contact_page(request):
    return render(request,'contact_page.html')
def save_page(request):
    if request.method=="POST":
        a=request.POST.get('Name')
        b=request.POST.get('Mobile')
        c=request.POST.get('Email')
        d=request.POST.get('Message')
        data=contactdb(Name=a,Mobile=b,Email=c,Message=d)
        data.save()
        return redirect(contact_page)
def product_filtered(request,cat_name):
    data= productdb.objects.filter(Categoryname=cat_name)
    return render(request,'product_filtered.html',{'data':data})

def product_single(request,pro_id):
    data=productdb.objects.get(id=pro_id)
    return render(request,"product_single.html",{'data':data})
def signup_page(request):
    return render(request,'signup_page.html')
def signin_page(request):
    return render(request,'signin_page.html')

def save_signup(request):
    if request.method=="POST":
        a = request.POST.get('Name')
        b = request.POST.get('Mobile')
        c = request.POST.get('Email')
        d = request.POST.get('Password')
        e = request.POST.get('Re_password')
        data = signupdb(Name=a, Mobile=b, Email=c, Password=d,Re_password=e)
        if signupdb.objects.filter(Name=a):
            messages.warning(request,"User name already exist")
            return redirect(signin_page)
        elif signupdb.objects.filter(Email=c):
            messages.warning(request,"User name already exist")
            return redirect(signin_page)
        data.save()
        return redirect(home)
def user_login(request):
    if request.method=='POST':
        un=request.POST.get('username')
        pswd=request.POST.get('password')
        if signupdb.objects.filter(Name=un,Password=pswd).exists():
            request.session['Name']=un
            request.session['Password']=pswd
            messages.success(request, "Login successfully...")
            return redirect(home)

        else:
            messages.error(request, "Invalid")
            return redirect(signin_page)
    else:
        messages.error(request, "Invalid")
        return redirect(signin_page)
def user_logout(request):
    del request.session['Name']
    del request.session['Password']
    messages.success(request,"Logout")
    return redirect(home)

def save_cart(request):
    if request.method=="POST":
        a = request.POST.get('Username')
        b = request.POST.get('Productname')
        c = request.POST.get('Quantity')
        d = request.POST.get('Price')
        e = request.POST.get('Totalprice')
        data = cartdb(Username=a, Productname=b, Quantity=c,Price=d,Totalprice=e)
        data.save()
        return redirect(home)


def cart(request):
    data=cartdb.objects.filter(Username=request.session['Name'])
    subtotal=0
    shipping_amount=0
    total=0
    for i in data:
        subtotal=subtotal+i.Totalprice
        if subtotal>50000:
            shipping_amount=100
        else:
            shipping_amount=250
        total=shipping_amount+subtotal
    return render(request,'cart.html',{'data':data,'subtotal':subtotal,'shipping_amount':shipping_amount,'total':total})

def delete_cart(request,cart_id):
    x=cartdb.objects.filter(id=cart_id)
    x.delete()
    return redirect(cart)

def checkout(request):
    data = cartdb.objects.filter(Username=request.session['Name'])

    subtotal = 0
    shipping_amount = 0
    total = 0
    for i in data:
        user=i.Username
        subtotal = subtotal + i.Totalprice
        if subtotal > 50000:
            shipping_amount = 100
        else:
            shipping_amount = 250
        total = shipping_amount + subtotal
    return render(request, 'checkout.html',
                  {'data': data, 'subtotal': subtotal, 'shipping_amount': shipping_amount, 'total': total,'user':user})



def save_order(request):
    if request.method=="POST":
        a = request.POST.get('Name')
        b = request.POST.get('Email')
        c = request.POST.get('Place')
        d = request.POST.get('Address')
        e = request.POST.get('Mobile')
        f = request.POST.get('Message')
        g = request.POST.get('Totalprice')
        data = orderdb(Name=a, Email=b, Place=c,Address=d,Mobile=e,Message=f,Totalprice=g)
        data.save()
        return redirect(payment)

def payment(request):
    # retrieve the data from orderdb with the specified ID
    customer=orderdb.objects.order_by('-id').first()
    # get the payment amount of the specified customer
    payy=customer.Totalprice
    # convert the amount into paisa (smallest currency unit)
    amount= int(payy*100)  # assuming the payment amount in rupees
    payy_str= str(amount)

    for i in payy_str:
        print(i)
    if request.method=="POST":
        order_currency='INR'
        client= razorpay.Client(auth=('rzp_test_fis20GTuy931b9','LIVeo1oNh8POcRHvgqT2YGRI'))
        paymen=client.order.create({'amount':amount,'currency':order_currency})
    return render(request,"payment.html",{'customer':customer,'payy_str':payy_str })



# Create your views here.
