from django import forms
from mybook.models import Booksinfo

class Booksinfoform(forms.ModelForm):
    
    class Meta:
        model = Booksinfo
    
        fields = '__all__'
