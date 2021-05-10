from django.shortcuts import render,redirect
from mobile.models import Product,Order,cart
from .forms import register_form,login_form,product_create_form,order_form,cart_form
from django.contrib.auth import authenticate,login,logout
from .decorators import login_required,admin_only

# Create your views here.
@admin_only
def index_page(request):
    return render(request,"mobile/base.html")
@login_required
def list_mobile(request):
    mobiles=Product.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile/listmobile.html",context)

def user_register(request):
    form=register_form()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_login")
    else:
        form = register_form(request.POST)
        context = {}
        context["form"] = form
        return render(request, "mobile/register.html", context)

    return render(request,"mobile/register.html",context)

def user_login(request):
    form=login_form()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=login_form(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if not user.is_superuser:
                    return redirect("user_home")
                else:
                    return redirect("index")



    return render(request,"mobile/login.html",context)
@login_required
def index_page2(request):
    return render(request,"mobile/base2.html")
@admin_only
def create_product(request):
    form=product_create_form()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=product_create_form(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_detail")

    return render(request,"mobile/addproduct.html",context)
#@login_required
def get_mobile_objects(id):
    return Product.objects.get(id=id)
@login_required
def mobile_detail(request,id):
    mobile=Product.objects.get(id=id)
    context={}
    context["mobile"]=mobile
    return render(request,"mobile/mobileview.html",context)
@admin_only
def product_details(request):
    mobile=Product.objects.all()
    context={}
    context["mobile"]=mobile
    return render(request,"mobile/productdetail.html",context)
@login_required
def delete_mobile(request,id):
    mobile=get_mobile_objects(id)
    mobile.delete()
    return redirect("product_detail")
@admin_only
def update_mobile(request,id):
    mobile=get_mobile_objects(id)
    form=product_create_form(instance=mobile)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=product_create_form(request.POST,instance=mobile,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_detail")
    return render(request,"mobile/mobileupdate.html",context)
@login_required
def product_view(request,id):
    mobile=Product.objects.get(id=id)
    context={}
    context["mobile"]=mobile
    return render(request,"mobile/productview.html",context)
@login_required
def user_logout(request):
    logout(request)
    return redirect("user_login")
@login_required
def order_product(request,id):
    cart_view=cart.objects.get(id=id)
    form=order_form(initial={"product":cart_view.product,"user":request.user})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=order_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            form = order_form(request.POST)
            context = {}
            context["form"] = form
            return render(request, "mobile/orderproduct.html", context)
    return render(request,"mobile/orderproduct.html",context)

@login_required
def add_to_cart(request,id):
    product=get_mobile_objects(id)
    form=cart_form(initial={"user":request.user,"product":product})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=cart_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            form = cart_form(request.POST)
            context = {}
            context["form"] = form
            return render(request, "mobile/cartadd.html",context)

    return render(request,"mobile/cartadd.html",context)
@login_required
def my_cart(request):
    cart_item=cart.objects.filter(user=request.user)
    context={}
    context["cart_item"]=cart_item
    return render(request,"mobile/mycart.html",context)
@login_required
def remove_order(request,id):
    cart_item=cart.objects.get(id=id)
    cart_item.delete()
    return redirect("my_cart")

@login_required
def account_details(request):
    return render(request,"mobile/accounts.html")
@login_required
def view_orders(request):
    orders=Order.objects.filter(user=request.user)
    context={}
    context["orders"]=orders
    return render(request,"mobile/vieworders.html",context)
@login_required
def cancel_order(request,id):
    order=Order.objects.get(id=id)
    order.status='Order Cancelled'
    order.save()
    return redirect("view_order")