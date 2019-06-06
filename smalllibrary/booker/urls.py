from django.urls import path
from .views import list_book,list_borrow,borrowing

app_name = 'borrowing'

urlpatterns = [
    # path('', borrowing, name='home'),
    path('', list_book, name='borrowing'),
    # path('logout/', logoutView, name='logout'),
]
