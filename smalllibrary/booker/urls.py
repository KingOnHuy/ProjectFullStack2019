from django.urls import path
from .views import list_book,list_borrow,borrow_book

app_name = 'booker'

urlpatterns = [
    # path('', borrowing, name='home'),
    path('', list_book, name='book'),
    path('borrowing/<int:pk>/', borrow_book, name='borrow_book')
    # path('logout/', logoutView, name='logout'),
]
