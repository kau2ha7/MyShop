from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
State_Choices=(
('AndhraPradesh ','AndhraPradesh'),
('Arunachal Pradesh','Arunachal Pradesh'),
('Assam','Assam'),
('Bihar','Bihar'),
('Chhattisgarh','Chhattisgarh'),
('Goa','Goa'),
('Gujarat','Gujarat'),
('Haryana','Haryana'),
('Himachal Pradesh','Himachal Pradesh'),
('Jammu & Kashmir','Jammu & Kashmir'),
('Jharkhand','Jharkhand'),
('Karnataka','Karnataka'),
('Kerala','Kerala'),
('Madhya Pradesh','Madhya Pradesh'),
('Maharashtra','Maharashtra'),
('Manipur','Manipur'),
('Meghalaya','Meghalaya'),
('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
('Orissa','Orissa'),
('Punjab','Punjab'),
('Rajasthan','Rajasthan'),
('Sikkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'),
('Tripura','Tripura'),
('Uttarakhand','Uttarakhand'),
('Uttar Pradesh','Uttar Pradesh'),
('West Bengal','West Bengal'),
('Tripura','Tripura'),
('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
('Chandigarh','Chandigarh'),
('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
('Daman & Diu','Daman & Diu'),
('Delhi','Delhi'),
('Lakshadweep','Lakshadweep'),
('Pondicherry','Pondicherry'),
)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices = State_Choices, max_length=50)


    def __str__(self):
        return str(self.id)
    

Category_Choices=(
    ('M','Mobiles'),
    ('L','Laptops'),
    ('TW','Top Wears'),
    ('BW','Bottom Wears'),
)    
    
class Product(models.Model):
    title = models.CharField(max_length=200)    
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    brand = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=Category_Choices,max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
     return str(self.id)
    
class Cart(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField(default = 1)

   def __str__(self):
     return str(self.id)
   
Status_Choices=(
   ('Accepted','Accepted'),
   ('Packed','Packed'),
   ('On The Way','On The Way'),
   ('Delivered','Delivered'),
   ('Cancel','Cancel'),
)   
       
class OrderPlaced(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField(default = 1)
   customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
   ordered_date = models.DateTimeField(auto_now_add=True)
   status = models.CharField(choices=Status_Choices,max_length=50,default='Pending')
       