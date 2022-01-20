from django.shortcuts import redirect, render
from mybook.models import Booksinfo
from mybook.forms import Booksinfoform

# Create your views here.
def index(request):
    return render(request,'mybook/home.html')

def mybook(request):
    b_info = Booksinfo.objects.all()
    return render(request,'mybook/mybook.html', {'books':b_info})

def form(request):
    b_form = Booksinfoform()
    if request.method == 'POST':
        b = Booksinfoform(request.POST)
        if b.is_valid():
            b.save()
            return redirect('/')
    
    return render(request, 'mybook/form.html',{'form':b_form})

def delete(request,id):
    b_del = Booksinfo.objects.get(id=id)
    b_del.delete()
    return redirect('/mybook/b')

def update(request,id):
    b = Booksinfo.objects.get(id=id)
    if request.method == 'POST':
        b_f = Booksinfoform(request.POST, instance=b)
        if b_f.is_valid():
            b_f.save()
            return redirect('/mybook/b')
    return render(request,'mybook/update.html',{'f':b})