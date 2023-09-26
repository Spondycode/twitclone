from django.shortcuts import render, redirect
from .models import Profile, Meep
from django.contrib import messages
from .forms import MeepForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms

def home(request):
    if request.user.is_authenticated:
        form = MeepForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                meep =form.save(commit=False)
                meep.user = request.user
                meep.save()
                messages.success(request, ("Your Meep has been Meeped "))
                return redirect('home')


        meeps = Meep.objects.all().order_by("-created_at")
        context = {"meeps":meeps, "form":form}
        return render(request, 'muscovite/home.html', context)
    else:
        meeps = Meep.objects.all().order_by("-created_at")
        context = {"meeps":meeps}
        return render(request, 'muscovite/home.html', context)



def about(request):
    return render(request, 'muscovite/about.html')


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        context = {"profiles":profiles}
        return render(request, 'muscovite/profile_list.html', context)
    else:
        messages.success(request, ("You have to log in to see this page"))
        return redirect ('home')


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        meeps = Meep.objects.filter(user_id=pk).order_by("-created_at")

#Post form logic
        if request.method == "POST":
            #Get user 
            current_user_profile = request.user.profile
        # Get form data
            action = request.POST['follow']
        # Decide to Follow or Unfollow
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            current_user_profile.save()



        context = {"profile":profile, "meeps":meeps}
        return render(request, 'muscovite/profile.html', context)
    else:
        messages.success(request, ("You have to log in to see this page"))
        return redirect ('home')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are logged in Meep - Something..."))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, Try again"))
            return redirect('login')

    else:
        return render(request, 'muscovite/login.html')



def logout_user(request):
    logout(request)
    messages.success(request, ("Bye Bye - See you later..."))
    return redirect('home')


def register(request):
    form = SignUpForm()
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You are registered and logged in"))
            return redirect('home')
  # else:
  #   form = SignUpForm()
    context = {'form':form}
    return render(request, 'muscovite/register.html', context)

