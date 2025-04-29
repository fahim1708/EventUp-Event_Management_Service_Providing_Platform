from django.contrib import admin
from .models import *

# Customer Admin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'District')

# Package Admin
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'package_id', 'price', 'location', 'quantity')

# Item Admin
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Price', 'Available_Quantity', 'Location')

# Package Detail Admin
@admin.register(Package_Detail)
class PackageDetailAdmin(admin.ModelAdmin):
    list_display = ('package', 'item')

# Package Availability Admin
@admin.register(PackageBooked)
class PackageBookedAdmin(admin.ModelAdmin):
    list_display = ('package', 'start_date', 'end_date')

# Item Availability Admin
@admin.register(ItemBooked)
class PackageBookedAdmin(admin.ModelAdmin):
    list_display = ('item', 'start_date', 'end_date')

# Register other models without custom admin classes
admin.site.register(Review)
admin.site.register(Product_Catagory)
admin.site.register(Profile)
admin.site.register(Order_Info)
admin.site.register(Order_Detail)
