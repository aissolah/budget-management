from django.urls import path
from .views import home, budget_detail
urlpatterns = [
    path('', home, name="home"),
    path('<int:budget_id>', budget_detail, name="budget_detail"),
]