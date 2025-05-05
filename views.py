from django.shortcuts import redirect, render
from base.models import products,cartmodel
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    category_nav=True
    tre_nav=False
    sale_nav=False
    all_products=products.objects.all()
    
    # TRENDING FUNCTIONALITY
    if 'trending' in request.GET:
        tre_nav=True
        category_nav=False
        trending_products=products.objects.filter(trending=1)
        all_products=trending_products
        

    # SALE FUNCTIONALITY
    if 'sale' in request.GET:
        sale_nav=True
        category_nav=False
        sale_products=products.objects.filter(sale=1)
        all_products=sale_products


    # SEARCH OPERATION
    if 'query' in request.GET:
        query_data=request.GET['query']
        category_nav=False
        all_products=products.objects.filter(Q(category__icontains=query_data) | Q(name__icontains=query_data))

    # NAV BAR FOR CATEGORY
    products_category=[]
    for i in all_products:
        if i.category not in products_category:
            products_category+=[i.category]

    if 'category_query' in request.GET:
        category_query_data=request.GET['category_query']
        all_products=products.objects.filter(category=category_query_data)
        context={'all_products':all_products,'products_category':products_category}
        return render(request,'home.html',context)
    

    # NAV BAR FOR PRODUCT NAME
    name_nav=True
    products_name=[]
    for i in all_products:
        if i.name not in products_name:
            products_name+=[i.name]

    if 'name_query' in request.GET:
        name_query_data=request.GET['name_query']
        name_nav=False
        all_products=products.objects.filter(name=name_query_data)
        context={'all_products':all_products,'products_name':products_name}


    # CREATING PRODUCTS
    if request.method=='POST':
        category_data=request.POST['category']
        name_data=request.POST['name']
        desc_data=request.POST['desc']
        price_data=request.POST['price']
        img_data=request.FILES['img']
        products.objects.create(category=category_data,name=name_data,desc=desc_data,price=price_data,image=img_data)
        return redirect('home')
    return render(request,'home.html',context={'all_products':all_products,'products_category':products_category,'category_nav':category_nav,'products_name':products_name,'name_nav':name_nav,'tre_nav':tre_nav,'sale_nav':sale_nav})

@login_required(login_url='login')
def cart(request):
    cart_products=cartmodel.objects.all()
    for i in cart_products:
        return render(request,'cart.html',context={'cart_products':cart_products})

@login_required(login_url='login')
def addtocart(request,pk):
    a=products.objects.get(id=pk)
    cartmodel.objects.create(category=a.category,name=a.name,desc=a.desc,price=a.price,image=a.image)
    return redirect('home')


def removecart(request,id):
    a=cartmodel.objects.get(id=id)
    a.delete()
    return redirect('cart')

def knowus(request):
    return render(request,'knowus.html')
