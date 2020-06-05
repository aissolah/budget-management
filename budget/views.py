from django.shortcuts import render,get_object_or_404,redirect
from .models import Budget,Charge

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



# ***Signup the user***
def signup_user(request):
	if request.method == "GET":
		return render(request,'budget/signup_user.html',{'form':UserCreationForm})
	else:
		if request.POST["password1"] == request.POST["password2"]:
			user = User.objects.create_user(request.POST["username"],password=request.POST["password1"])
			login(request,user)
			return redirect('budgets')
		else:
			return render(request,'budget/signup_user.html',{'form':UserCreationForm,'error':'Passwords did not match'})

# ***Log the user in***
def login_user(request):
	if request.method == "GET":
		return render(request,'budget/login_user.html',{'form':AuthenticationForm})
	else:
		user = authenticate(username=request.POST["username"],password=request.POST["password"])
		if user is None:
			return render(request,'budget/login_user.html',{'form':AuthenticationForm, 'error':'Invalid username or password'})
		else:
			login(request,user)
			return redirect('budgets')

# ***logout the user ***
def logout_user(request):
	if request.method == "POST":
		logout(request)
		return redirect("home")

# ***Home page***
def home(request):
  return render(request, 'budget/home.html')

# ***Shows all the budgets of the currently logged in user***
def budgets(request):
  budgets = Budget.objects.all()
  return render(request, 'budget/budgets.html',{'budgets':budgets})

# ***Detail page of a selected budget***
def budget_detail(request, budget_id):
  budget = get_object_or_404(Budget,pk=budget_id)
  charges = Charge.objects.all().filter(budget=budget_id)
  return render(request, 'budget/budget_detail.html',{'budget':budget,'charges':charges})