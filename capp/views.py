from django.shortcuts import render,redirect
from capp.models import categorydb,productdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from webapp.models import contactdb
from django.contrib import messages

def index(request):
    x=categorydb.objects.count()
    y =productdb.objects.count()
    return render(request,"index.html",{'x':x,'y':y})

def add_category(request):
    return render(request,"add_category.html")
def save_category(request):
    if request.method=="POST":
        a=request.POST.get('Categoryname')
        b=request.POST.get('Description')
        c = request.FILES['Categoryimage']
        obj=categorydb(Categoryname=a,Description=b,Categoryimage=c)
        obj.save()
        messages.success(request,"Category Saved...")
        return redirect(add_category)

def display_category(request):
    cat=categorydb.objects.all()
    return render(request,'display_category.html',{'cat':cat})



def edit_category(request,cat_id):
    cat=categorydb.objects.get(id=cat_id)
    return render(request,'edit_category.html',{'cat':cat})

def update_category(request,cat_id):
    if request.method=='POST':
        a=request.POST.get('Categoryname')
        b=request.POST.get('Description')
        try:
            img=request.FILES['Categoryimage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= categorydb.objects.get(id=cat_id).Categoryimage
        categorydb.objects.filter(id=cat_id).update(Categoryname=a,Description=b,Categoryimage=file)
        messages.success(request, "Category Updated...")
        return redirect(display_category)
def delete_category(request,cat_id):
    x=categorydb.objects.filter(id=cat_id)
    x.delete()
    messages.error(request, "Category Deleted...")
    return redirect(display_category)



def add_product(request):
    pro=categorydb.objects.all()
    return render(request,"add_product.html",{'pro':pro})

def save_product(request):
    if request.method=="POST":
        a=request.POST.get('Categoryname')
        b=request.POST.get('Productname')
        c = request.POST.get('Quantity')
        d = request.POST.get('Mrp')
        e = request.POST.get('Description')
        f = request.POST.get('Country')
        g = request.POST.get('Manufactured')
        h = request.FILES['Productimage1']
        i = request.FILES['Productimage2']
        j = request.FILES['Productimage3']
        obj=productdb(Categoryname=a,Productname=b,Quantity=c,Mrp=d,Description=e,Country=f,Manufactured=g,Productimage1=h,Productimage2=i,Productimage3=j)
        obj.save()
        messages.success(request, "Product Saved...")
        return redirect(add_product)
def display_product(request):
    pro=productdb.objects.all()
    return render(request,'display_product.html',{'pro':pro})
def edit_product(request,pro_id):
    cat=categorydb.objects.all()
    pro=productdb.objects.get(id=pro_id)
    return render(request,'edit_product.html',{'pro':pro,'cat':cat})

def update_product(request,pro_id):
    if request.method=='POST':
        a = request.POST.get('Categoryname')
        b = request.POST.get('Productname')
        c = request.POST.get('Quantity')
        d = request.POST.get('Mrp')
        e = request.POST.get('Description')
        f = request.POST.get('Country')
        g = request.POST.get('Manufactured')
        try:
            img1=request.FILES['Productimage1']
            fs=FileSystemStorage()
            file1=fs.save(img1.name,img1)
        except MultiValueDictKeyError:
            file1= productdb.objects.get(id=pro_id).Productimage1

        try:
            img2=request.FILES['Productimage2']
            fs=FileSystemStorage()
            file2=fs.save(img2.name,img2)
        except MultiValueDictKeyError:
            file2= productdb.objects.get(id=pro_id).Productimage2

        try:
            img3 = request.FILES['Productimage3']
            fs = FileSystemStorage()
            file3 = fs.save(img3.name, img3)
        except MultiValueDictKeyError:
            file3 = productdb.objects.get(id=pro_id).Productimage3

        productdb.objects.filter(id=pro_id).update(Categoryname=a,Productname=b,Quantity=c,Mrp=d,Description=e,Country=f,Manufactured=g,Productimage1=file1,Productimage2=file2,Productimage3=file3)
        messages.success(request, "Product Updated...")
        return redirect(display_product)

def delete_product(request,pro_id):
    pro=productdb.objects.filter(id=pro_id)
    pro.delete()
    messages.error(request, "Product Deleted...")
    return redirect(display_product)

def login_page(request):
    return render(request,"login.html")

def admin_login(request):
    if request.method=='POST':
        un=request.POST.get('username')
        pswd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pswd)
            if user is not None:
                login(request,user)
                request.session['username']=un
                request.session['password'] = pswd
                messages.success(request, "Welcome...")
                return redirect(index)
            else:
                messages.error(request, "Invalid user name/password...")
                return redirect(login_page)
        else:
            messages.error(request, "Invalid user name/password...")
            return redirect(login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Good Bye...")
    return redirect(login_page)
def user_data(request):
    data=contactdb.objects.all()
    return render(request,'user_data.html',{'data':data})
def delete_data(request,user_id):
    data=contactdb.objects.filter(id=user_id)
    data.delete()
    return redirect(user_data)





# Create your views here.
