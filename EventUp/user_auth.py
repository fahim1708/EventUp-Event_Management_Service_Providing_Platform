from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def registration2(request):
    if request.method == "POST":
        username  = request.POST.get("username")
        email  = request.POST.get("email")
        password = request.POST.get("password")
        print(username,password)

        if User.objects.filter(username=username).exists():
            messages.warning(request,'Email are already exists!')
            return redirect('sign_up2')
        
        if User.objects.filter(username=username).exists():
            messages.warning(request,'Username are already exists!')
            return redirect('sign_up2')
        
        user = User(
            username = username,
            email = email
        )

        user.set_password(password)
        user.save()
        return redirect('login')
    
    return render(request,'Registrations\signup2.html')


def registration(request):
    if request.method == "POST":
        username  = request.POST.get("username")
        email  = request.POST.get("email")
        password = request.POST.get("password")
        print(username,password)

        if User.objects.filter(username=username).exists():
            messages.warning(request,'Email are already exists!')
            return redirect('sign_up')
        
        if User.objects.filter(username=username).exists():
            messages.warning(request,'Username are already exists!')
            return redirect('sign_up')
        
        user = User(
            username = username,
            email = email
        )

        user.set_password(password)
        user.save()
        return redirect('Login')
    
    return render(request,'Registrations\signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You're Successfully Logged In!")
            return redirect('decoration')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'Registrations\login.html')
        
def logout_view(request):
    logout(request)
    messages.success(request, "You're Logged Out!")
    return redirect('decoration')

def Profile(request):
    return render(request,'registration\profile.html')

def Profile_Update(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')