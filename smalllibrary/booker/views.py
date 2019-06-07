from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Book, Binding, Publisher, Borrow, Transaction
# from .forms import ItemForm

def list_book(request):
    print(request.user)
    context = dict()
    context['books'] = Book.objects.all().order_by('id')
    return render(request, 'booker/book.html', context)

@login_required
def list_borrow(request):
    context = dict()
    context['borrows'] = Borrow.objects.filter(borrower__username=request.user)
    return render(request, 'booker/borrow.html', context)

@login_required
def return_book(request):
    if request.method == 'GET':
        try:
            Transaction.objects.create(
                book = book,
                actor = actor,
                action = "return",
            )
        except Exception as e:
            print(e)
            raise e

@login_required
def borrow_book(request,pk):
    if request.method == 'GET':
        try:
            book = Book.objects.get(pk=pk)
            actor = request.user
            Transaction.objects.create(
                book = book,
                actor = actor,
                action = "borrow",
            )
            Borrow.objects.create(
                borrower = actor,
                book = book,
            )
            return redirect('booker:book')
        except Exception as e:
            print(e)
            raise e