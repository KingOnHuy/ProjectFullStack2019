from django.contrib import admin
from .models import Borrow
from .models import Book
from .models import Transaction
from .models import Publisher
from .models import Binding

# Register your models here.
@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Borrow._meta.fields]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Book._meta.fields]

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Transaction._meta.fields]
    # readonly_fields = [f.name for f in Transaction._meta.fields]

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Publisher._meta.fields]

@admin.register(Binding)
class BindingAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Binding._meta.fields]
