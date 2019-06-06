from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Book, Binding, Publisher, Borrow, Transaction
# from .forms import ItemForm

def list_book(request):
    context = dict()
    context['books'] = Book.objects.all().order_by('id')
    return render(request, 'book.html', context)

def list_borrow(request):
    context = dict()
    context['borrows'] = Borrow.objects.all().order_by('id')
    return render(request, 'borrow.html', context)

def borrowing(request):
    if request.method == 'POST':
        try:
            book = Book.objects.get(pk=pk)
            actor = request.user()
            print(actor)
            Transaction.objects.create(
                book = book,
                actor = actor,
                # action = item.price * amount,
            )
            return redirect('list_borrow')
        except Exception as e:
            print(e)
            raise e