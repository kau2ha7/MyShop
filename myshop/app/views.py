from django.shortcuts import render
from django.views import View
from .forms import CustomerCreationForm
from django.views.generic import DetailView,FormView
from .models import Product,Cart,OrderPlaced,Customer
from django.contrib import messages

# def home(request):
#  return render(request, 'app/home.html')
class ProductView(View):
  def get(self,request):
    topwears = Product.objects.filter(category = 'TW')
    bottomwears = Product.objects.filter(category = 'BW')
    mobiles = Product.objects.filter(category = 'M')
    laptops = Product.objects.filter(category = 'L')
    return render(request,'app/home.html',{'topwears':topwears,  'bottomwears':bottomwears,'mobiles':mobiles,'laptops':laptops})
  

# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class ProductDetailView(View):
  def get(self,request, pk):
   product = Product.objects.get(pk=pk)
   return render(request,'app/productdetail.html',{'product':product})

 
  
    
def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')


def mobile(request,data=None):
  if data == None:
   mobiles = Product.objects.filter(category = 'M')
  elif data == 'Apple' or data == 'Motorola' or data == 'Samsung' or data == 'Nokia':
   mobiles = Product.objects.filter(category='M').filter(brand = data) 
  elif data =='below':
    mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)  
  elif data =='above':
    mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)    
   
  return render(request, 'app/mobile.html',{'mobiles':mobiles})

def laptop(request,data=None):
  if data == None:
   laptops = Product.objects.filter(category = 'L')
  elif data == 'Apple' or data == 'Lenovo' or data == 'HP':
   laptops = Product.objects.filter(category='L').filter(brand = data) 
  elif data =='below':
    laptops = Product.objects.filter(category='L').filter(discounted_price__lt=10000)  
  elif data =='above':
    laptops = Product.objects.filter(category='L').filter(discounted_price__gt=10000)    
  return render(request, 'app/laptop.html',{'laptops':laptops})


def topwear(request,data=None):
  if data == None:
   topwears = Product.objects.filter(category = 'TW')
  elif data == 'Gucci' or data == 'Levis' or data == 'Lee' or data == 'Lee_Cooper' or data == 'Tommy_Hielfiger':
   if data is not None:
     normalized_data = data.replace('_', ' ')
   topwears = Product.objects.filter(category='TW').filter(brand = normalized_data)
  elif data =='below':
    topwears = Product.objects.filter(category='TW').filter(discounted_price__lt=10000)  
  elif data =='above':
    topwears = Product.objects.filter(category='TW').filter(discounted_price__gt=10000)     
  return render(request, 'app/topwear.html',{'topwears':topwears})


def bottomwear(request,data=None):
  if data == None:
   bottomwears = Product.objects.filter(category = 'BW')
  elif data == 'Gucci' or data == 'Levis' or data == 'Lee' or data == 'Lee_Cooper' or data == 'Papa_Jeans' or data == 'Buffalo':
   if data is not None:
     normalized_data = data.replace('_', ' ')
   else:
     bottomwears = Product.objects.filter(category = 'BW')
   bottomwears = Product.objects.filter(category='BW').filter(brand = normalized_data) 
  elif data =='below':
    bottomwears = Product.objects.filter(category='BW').filter(discounted_price__lt=10000)  
  elif data =='above':
    bottomwears = Product.objects.filter(category='BW').filter(discounted_price__gt=10000)    
  return render(request, 'app/bottomwear.html',{'bottomwears':bottomwears})

def login(request):
 return render(request, 'app/login.html')

class CustomerRegistrationView(View):
 def get(self,request):
  form = CustomerCreationForm()
  print(form)
  return render(request, 'app/customerregistration.html',{'form':form})
 def post(self,request):
  form = CustomerCreationForm(request.POST)
  if form.is_valid():
   messages.success(request,'Congratulation!You have created your account!')
   form.save()
  return render(request, 'app/customerregistration.html',{'form':form})

def checkout(request):
 return render(request, 'app/checkout.html')
