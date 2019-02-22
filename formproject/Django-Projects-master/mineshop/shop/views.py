from django.shortcuts import *
from .models import *
# Create your views here.
from cart.forms import *
from cart.cart import Cart

def index(request):
    cat=Categories.objects.all()

    for i in cat:
        for k in i.product_set.all():
            print (k.name)
            
    return render(request,'home.html',{'cat':cat})

def product_category(request,n):
    all_prod=Categories.objects.get(slug=n)
    categories=Categories.objects.all()
    return render(request,'product_cat.html',{'cat':all_prod,'categories':categories})

def detail(request,d,slug):
    cart=Cart(request)
    #product=Product.objects.get(slug=slug)
    product = get_object_or_404(Product, id=d, slug=slug)
    if request.method=='POST':
        cartform=CartForm(request.POST)
        if cartform.is_valid():
            cd=cartform.cleaned_data
            cart.add(product=product,quantity=cd['quantity'],
                 update_quantity=cd['update'])

            return redirect('cart:cart_detail')

    else:
        cartform=CartForm()
        
    return render(request,'detail.html',{'prod':product,'cartform':cartform})
