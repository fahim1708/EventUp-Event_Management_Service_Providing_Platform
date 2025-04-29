from django.shortcuts import render, redirect
from Decoration.models import Package
from django.contrib.auth.models import User
import json

def Base(request):
    return render(request,'base.html')

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Decoration.models import Profile, Order_Info, Order_Detail
from .forms import ProfileEditForm
@login_required
# def profile(request):
#     user = request.user
#     try:
#         user_profile = Profile.objects.get(user=user)
#     except Profile.DoesNotExist:
#         user_profile = None  # Handle case where the profile doesn't exist

#     context = {
#         'user': user,
#         'user_profile': user_profile
#     }
#     return render(request, 'profile.html', context)


def profile(request):
    user = request.user

    # Check if the user already has a profile, and if not, create one
    user_profile, created = Profile.objects.get_or_create(user=user)

    # Handle form submission for editing profile
    if request.method == 'POST':
        # Create a form instance with the submitted data and bind it to the user profile
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=user_profile)

        if profile_form.is_valid():
            # Save the User model fields
            user.first_name = profile_form.cleaned_data.get('first_name')
            user.last_name = profile_form.cleaned_data.get('last_name')
            user.email = profile_form.cleaned_data.get('email')
            user.save()  # Save the updated User model

            # Save the Profile model fields
            profile_form.save()  # Save the updated profile
            
            return redirect('Profile')  # Redirect to the profile page after saving
    else:
        profile_form = ProfileEditForm(instance=user_profile)

    # Fetch user's orders
    orders = Order_Info.objects.filter(user=user)  # Fetch orders related to the logged-in user

    context = {
        'user': user,
        'user_profile': user_profile,
        'profile_form': profile_form, 
        'orders': orders  # Add the orders to the context
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    user = request.user
    try:
        # Get the user's profile
        user_profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        # Handle case where the profile doesn't exist
        user_profile = None

    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        district = request.POST.get('district')
        thana = request.POST.get('thana')
        address = request.POST.get('address')

        # Update user object
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()

        # Update profile object
        if user_profile:
            user_profile.phone = phone
            user_profile.district = district
            user_profile.thana = thana
            user_profile.address = address
            user_profile.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('profile')  # Redirect to the profile page after saving

    # Render the edit profile page with user and profile data
    context = {
        'user': user,
        'user_profile': user_profile,
    }
    return render(request, 'edit_profile.html', context)

def order_view(request, order_id):
    orderDetail = Order_Detail.objects.filter(order_id=order_id)
    order = Order_Info.objects.get(order_id=order_id)

    package_count = orderDetail.filter(package__isnull=False).count()
    item_count = orderDetail.filter(item__isnull=False).count()
    context = {
        "order": order,
        "orderDetail" : orderDetail,
        "package_count": package_count,
        "item_count": item_count
    }
    return render(request,"order_view.html",context)
