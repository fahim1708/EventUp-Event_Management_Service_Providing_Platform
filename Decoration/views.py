from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Avg
from .models import *
import json
def search_view(request):
    location = request.GET.get('location', '')
    results = Package.objects.filter(location=location)
    return render(request, 'search_results.html', {'results': results})


def delete_old_bookings():
    # Get today's date
    today = timezone.now().date()

    # Delete old PackageBooked records where end_date is before today
    PackageBooked.objects.filter(end_date__lt=today).delete()

    # Delete old ItemBooked records where end_date is before today
    ItemBooked.objects.filter(end_date__lt=today).delete()


from django.db.models import Q
def Decoration(request):
    delete_old_bookings()
    # Initialize the decoration query set
    packages = Package.objects.all()
    items = Item.objects.all()

    # Get search criteria from GET parameters
    location = request.GET.get('location', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    # Apply location search filter
    if location:
        packages = packages.filter(location__icontains=location)
        items = items.filter(Location__icontains=location)

    # Apply date range filter and exclude booked packages/items only if bookings exist
    if start_date and end_date:
        # Check if there are any bookings in PackageBooked or ItemBooked
        if PackageBooked.objects.exists():
            # Filter packages that are not booked in the given date range
            packages = packages.exclude(
                Q(availabilities__start_date__lte=end_date) & Q(availabilities__end_date__gte=start_date)
            )
        
        if ItemBooked.objects.exists():
            # Filter items that are not booked in the given date range
            items = items.exclude(
                Q(availabilities__start_date__lte=end_date) & Q(availabilities__end_date__gte=start_date)
            )

    # Check if there are any matching packages or items
    no_package = not packages.exists()
    no_item = not items.exists()

    # Handle AJAX request for location autocomplete
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and 'query' in request.GET:
        query = request.GET.get('query', '')
        if query:
            locations = Package.objects.filter(location__icontains=query).values_list('location', flat=True).distinct()
            return JsonResponse(list(locations), safe=False)
        return JsonResponse([], safe=False)

    # Render the page with decorations and items
    return render(request, 'decoration.html', {
        'packages': packages,
        'items': items,
        'no_package': no_package,
        'no_items': no_item,
        'date_from': start_date,
        'date_to': end_date
    })


def view_page_decoration(request):
    return render(request,'view_page_decoration.html')


def DecorationDetailView(request, pk):
    package = get_object_or_404(Package, package_id=pk)
    items = package.Pack_Details.all()

    images = items.filter(media_type='image')
    videos = items.filter(media_type='video')
    
    # Determine if there are no images or videos
    no_image = not images.exists()
    no_video = not videos.exists()
    
    # Retrieve ratings and reviews for the package
    reviews = Review.objects.filter(package=package)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    reviewers_count = reviews.values('customer').count()

    return render(request, 'decoration_detail.html', {
        'package': package, 
        'items': items,
        'no_image': no_image,
        'no_video': no_video,
        'reviews': reviews,
        'average_rating': average_rating,
        'reviewers_count': reviewers_count,
    })


from .built_in_func import name_splitter
from .models import Order_Info, Profile
from .forms import OrderInfoForm
from django.shortcuts import get_object_or_404
from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
@login_required(login_url='Login')
def ConfirmationView(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        messages.error(request, "Please log in first.")
        return redirect('Login')
    
    # Get the selected item IDs (for packages)
    selected_items_ids = request.GET.get('selectedItems', '').split(',')
    
    # Filter out any empty or invalid IDs
    selected_items_ids = [item_id for item_id in selected_items_ids if item_id.isdigit()]
    # Get the selected item IDs with quantities (as a JSON-encoded string)
    items_with_quantity = request.GET.get('itemsWithQuantity', '{}')

    # Decode the JSON string into a Python dictionary
    try:
        items_with_quantity = json.loads(items_with_quantity)
    except json.JSONDecodeError:
        items_with_quantity = {}
    # Filter selected packages using the correct field name for the package ID
    selected_packages = Package.objects.filter(package_id__in=selected_items_ids)

    # Filter selected items using the correct field name for the item ID (Item_ID)
    selected_items = Item.objects.filter(Item_ID__in=items_with_quantity.keys())

    # Create a dictionary that maps each item to its selected quantity
    selected_items_with_quantities = [
        {
            'item': item,
            'quantity': items_with_quantity.get(str(item.Item_ID), 1)  # Default to 1 if not found
        }
        for item in selected_items
    ]

    # Calculate the total price of the selected packages and items
    total_price = sum(package.price for package in selected_packages)
    total_price += sum(entry['item'].Price * entry['quantity'] for entry in selected_items_with_quantities)
    #---------------------
    user = request.user
    email = user.email
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone_no = request.POST.get("phone_no")
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        address = request.POST.get("address")
        district = request.POST.get("district")
        thana = request.POST.get("thana")
        total_price = total_price
        order_date = date.today()

        # Create a new Order_Info object with the form data
        order = Order_Info(
            user=user,
            full_name=full_name,
            phone_no=phone_no,
            email=email,
            date_from=date_from,
            date_to=date_to,
            address=address,
            district=district,
            thana=thana,
            total_Price=total_price,
            order_date=order_date
        )
        first_name, last_name = name_splitter(full_name)
        # Save the order to the database
        order.save()
        
        # Update the user's profile only if the data is new or changed
        profile = user.profile
        if phone_no and not profile.phone:
            profile.phone = phone_no
            profile.order_phone = phone_no
        elif phone_no and profile.phone:
            profile.order_phone = phone_no
        if address and not profile.address:
            profile.address = address
        if district and not profile.district:
            profile.district = district
        if thana and not profile.thana:
            profile.thana = thana
        profile.save()
        
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Create Order_Detail entries for selected packages
        for package in selected_packages:
            PackageBooked.objects.create(
                package = package,
                start_date = date_from,
                end_date = date_to
                )
            Order_Detail.objects.create(
                order_id=order,
                package=package,
                item=None,  # Set to None for package entries
                items_quantity=1  # Assuming quantity 1 for packages
                )

        # Create Order_Detail entries for selected items
        for entry in selected_items_with_quantities:
            ItemBooked.objects.create(
                item=entry['item'],
                start_date = date_from,
                end_date = date_to
                )
            Order_Detail.objects.create(
                order_id=order,
                package=None,  # Set to None for item entries
                item=entry['item'],
                items_quantity=entry['quantity']
            )

        messages.success(request, "Your order is placed successfully!")

        # Redirect to the decoration page after successful submission
        return redirect('decoration')
    


    user_profile = user.profile  # Assuming profile is linked to User via OneToOne field
    form = OrderInfoForm(initial={
        'full_name': f"{request.user.first_name} {request.user.last_name}",
        'email': request.user.email,
        'phone_no': user_profile.phone if hasattr(user_profile, 'phone') else '',
        'address': user_profile.address if hasattr(user_profile, 'address') else '',
        'district': user_profile.district if hasattr(user_profile, 'district') else '',
        'thana': user_profile.thana if hasattr(user_profile, 'thana') else '',
        'date_from': start_date,
        'date_to': end_date
    })

    # Pass packages and items (with quantities) separately
    context = {
        'selected_packages': selected_packages,
        'selected_items_with_quantities': selected_items_with_quantities,
        'total_price': total_price,
        'form':form,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'order_confirmation.html', context)

