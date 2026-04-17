from django.urls import path
from .views import ExpenseListCreateAPIView, ExpenseRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('expense/', ExpenseListCreateAPIView.as_view(), name='expense-list-create'),
    path('expense/<int:pk>/', ExpenseRetrieveUpdateDestroyAPIView.as_view(), name='expense-update-delete'),
]