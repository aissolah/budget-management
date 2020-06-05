from django.urls import path
from .views import home, signup_user, login_user, logout_user, budgets, budget_detail
urlpatterns = [
	path('signup/', signup_user, name="signup_user"),
	path('logout/', logout_user, name="logout_user"),
	path('login/', login_user, name="login_user"),
    path('', home, name="home"),
    path('budgets/', budgets, name="budgets"),
    path('budgets/<int:budget_id>', budget_detail, name="budget_detail"),
]