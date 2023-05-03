from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View
from store.models.country import Country
from store.models.city import  City
import string


class Account (View):
    def get(self, request):
        data={}
        countries = Country.get_all_countreis()
        cities = City.get_all_cities()

            
        data['countries'] = countries
        data['cities'] = cities
        
        return render (request, 'account.html', data)

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        confirmpassword = postData.get('confirmpassword')
        date = postData.get('date')
        address = postData.get('address')
        country = postData.get('country')
        
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
            'date' : date,
            'address': address,
            'country':country
        }
        error_message = None

        customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password,
                             date = date,
                             address = address,
                             country = country)

        error_message = self.validateCustomer (customer, confirmpassword)

        if not error_message:
            print (first_name, last_name, phone, email, password)
            customer.password = make_password (customer.password)
            customer.register ()
            return redirect ('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            countries = Country.get_all_countreis() 
            cities = City.get_all_cities()
                
            data['countries'] = countries
            data['cities'] = cities
            

            return render (request, 'account.html', data)

    def validateCustomer(self, customer, confirm):
        error_message = None
        if (not customer.first_name):
            error_message = "Please Enter your First Name !!"
        elif len (customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len (customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (customer.password) < 7:
            error_message = 'Password must be 7 char long'
        elif not any([char.isdigit() for char in customer.password]):
            error_message = 'Password requires a digit'
        elif not any([char.isupper() for char in customer.password]):
            error_message = 'Password requires a capital'
        elif not any([True if char in string.punctuation else False for char in customer.password]):
            error_message = 'Password requires a special character' 
        elif len (customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists ():
            error_message = 'Email Address Already Registered..'
        elif customer.password != confirm:
            error_message  = 'The passwords do not match'
        
        # saving

        return error_message
