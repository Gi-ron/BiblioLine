'''Module for the customer cart'''
from django.shortcuts import render
from django.views import  View
from store.models.product import Products


class Cart(View):
    '''view class for cart products'''
    def get(self , request):
        '''get all products inside the cart'''
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )
