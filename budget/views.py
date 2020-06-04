from django.shortcuts import render,get_object_or_404
from .models import Budget,Charge
# Create your views here.
def home(request):
  budgets = Budget.objects.all()
  return render(request, 'budget/home.html',{'budgets':budgets})

def budget_detail(request, budget_id):
  budget = get_object_or_404(Budget,pk=budget_id)
  charges = Charge.objects.all().filter(budget=budget_id)
  return render(request, 'budget/budget_detail.html',{'budget':budget,'charges':charges})