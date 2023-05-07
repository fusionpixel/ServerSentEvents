from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('transactions', views.view_transactions, name='transactions'),
    path('transactions', views.TransactionView.as_view(), name='transactions'),
    path('transaction_stream', views.TransactionStreamView.as_view(), name='transaction_stream'),

]
