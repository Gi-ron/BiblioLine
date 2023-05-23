'''Module for the news added for the customer'''
from django.shortcuts import render
from django.views import View

class News (View):
    '''view class for the account service'''
    def get(self, request):
        '''get function for bring the account data'''
        return render (request, 'news.html')
