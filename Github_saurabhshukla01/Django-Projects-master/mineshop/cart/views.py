from django.shortcuts import *
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import *
from django.http import *
from django.core.urlresolvers import reverse


# Create your views here.
@require_POST
def cart_add(request,product_id):
    cart= Cart(request)
    product = get_object_or_404(Product,id=product_id)
    form = CartForm(request.POST)
    if form.is_valid():
        cd=form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],
                 update_quantity=cd['update'])
        
    return redirect('cart:cart_detail')   

def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    #product = get_object_or_404(Product,id=d)

    for item in cart:
        
        item['update_quantity_form'] = CartForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    
    return render(request,'cart/detail.html',{'cart':cart})
    '''
    for item in cart:
        if item['product']==product:
            cart_product=item
    form = CartForm(initial={'quantity':cart_product['quantity'],
                             'update':True})
    return render(request,'cart/detail.html',{'cart_product':cart_product,
                                         'form':form,
                                         'product':product})
    '''
    
