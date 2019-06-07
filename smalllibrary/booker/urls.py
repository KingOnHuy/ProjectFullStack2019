from django.urls import path
from .views import list_book,list_borrow,borrow_book,return_book

app_name = 'booker'

urlpatterns = [
    # path('', borrowing, name='home'),
    path('', list_book, name='book'),
    path('borrowing/<int:pk>/', borrow_book, name='borrow_book'),
    path('borrowlist/', list_borrow, name='list_borrow'),
    path('returnbook/<int:pk>/', return_book, name='return_book'),
    # path('logout/', logoutView, name='logout'),
]
