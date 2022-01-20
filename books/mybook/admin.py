from django.contrib import admin
from mybook.models import Booksinfo
# Register your models here.

class Booksinfoadmin(admin.ModelAdmin):
    b_info = ['Name','Author','date','quantity']

admin.site.register(Booksinfo, Booksinfoadmin)
