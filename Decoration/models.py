from django.db import models
from datetime import timedelta
from django.utils import timezone 
from django.contrib.auth.models import User
from .built_in_func import upload_to, get_default_available_to

class Customer(models.Model):
    Customer_ID = models.AutoField(primary_key=True)  # Primary Key
    Name = models.CharField(max_length=255)  # Store the customer's name
    Email = models.EmailField(max_length=255)  # Store the customer's email
    Password = models.CharField(max_length=128)  # Store the customer's password
    Phone_No = models.CharField(max_length=20, null=True)  # Store the customer's phone number
    District = models.CharField(max_length=100, null=True)  # Store the district
    Thana = models.CharField(max_length=100, null=True)  # Store the thana (sub-district)
    Address = models.TextField(null=True)  # Store the full address

    def __str__(self):
        return self.Name  # String representation of the object
    

class Product_Catagory(models.Model):
    catagory_id = models.AutoField(primary_key=True)
    catagory_name = models.CharField(max_length=255)

    def __str__(self):
        return self.catagory_name
    

class Package(models.Model):
    Product_Catagory = models.ForeignKey(Product_Catagory, on_delete=models.CASCADE, null=True, blank=True)
    package_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)  # Store the title of the decoration item
    description = models.TextField()  # Store the description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Store the price
    image = models.ImageField(upload_to='decorations/packages')  # Store the image
    location = models.CharField(max_length=255, default='Unknown')  # Store the location
    quantity = models.PositiveIntegerField()  # Store the quantity
    
    def __str__(self):
        return self.title


class Item(models.Model):
    Product_Catagory = models.ForeignKey(Product_Catagory, on_delete=models.CASCADE, null=True, blank=True)
    Item_ID = models.AutoField(primary_key=True)  # Primary key
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Available_Quantity = models.IntegerField()
    Cover_Image = models.ImageField(upload_to='decorations/items')
    Location = models.CharField(max_length=255)
    Catagory = models.CharField(default='General', max_length=100)

    def __str__(self):
        return self.Title


from django.core.exceptions import ValidationError
class PackageBooked(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='availabilities')
    start_date = models.DateField(null=True,blank=True)  
    end_date = models.DateField()

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError('End date cannot be before start date.')

    def __str__(self):
        return f"{self.package} availability from {self.start_date} to {self.end_date}"
    

class ItemBooked(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='availabilities',null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField()

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError('End date cannot be before start date.')

    def __str__(self):
        return f"{self.item} availability from {self.start_date} to {self.end_date}"


class Package_Detail(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='Pack_Details',null=True,blank=True)  # Foreign key to Decoration_Packages
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_details', null=True, blank=True)
    media_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')], null=True, blank=True)  # To differentiate between image and video
    file = models.FileField(upload_to=upload_to, null=True, blank=True)  # Store media files based on their type
    
    def __str__(self):
        return self.package.title


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Foreign key from CustomerInfo
    package = models.ForeignKey(Package, on_delete=models.CASCADE)  # Foreign key from Decoration_Packages
    rating = models.PositiveIntegerField()  # Store the rating (e.g., 1-5 stars)
    review = models.TextField()  # Store the review text
    
    def __str__(self):
        return f'Review by {self.customer.Name} for {self.package.title}'

  
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    phone = models.CharField(max_length=15)
    order_phone = models.CharField(max_length=15,null=True,blank=True)
    district = models.CharField(max_length=50)
    thana = models.CharField(max_length=50)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='client/profile_pictures', null=True, blank=True)

    def __str__(self):
        return self.user.username


import uuid
from datetime import datetime
class Order_Info(models.Model):
    order_id = models.BigIntegerField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField()
    date_from = models.DateField()
    date_to = models.DateField()
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=100)
    thana = models.CharField(max_length=100)
    total_Price = models.IntegerField(null=True,default=0)
    order_date = models.DateField(null=True)

    def __str__(self):
        return f"Order by {self.full_name} from {self.date_from} to {self.date_to}"
    def save(self, *args, **kwargs):
        if not self.order_id:
            # Format order_id as "daymonthyear_userid_serial"
            today = datetime.now()
            day = today.strftime("%d")
            month = today.strftime("%m")
            year = today.strftime("%Y")
            
            # Get user_id as string
            user_id = str(self.user.id)
            
            # Get a serial number for the day (number of orders by this user today)
            serial = (
                Order_Info.objects.filter(user=self.user, order_date=today.date()).count() + 1
            )
            
            # Generate order_id in the format "daymonthyear_userid_serial"
            order_id = f"{day}{month}{year}{user_id}{serial:03d}"
            self.order_id = int(order_id)

        super(Order_Info, self).save(*args, **kwargs)


class Order_Detail(models.Model):
    order_id = models.ForeignKey(Order_Info, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    items_quantity = models.IntegerField()
    