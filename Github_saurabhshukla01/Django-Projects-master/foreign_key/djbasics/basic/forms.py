from django import forms
from .models import *

class Publisherform(forms.ModelForm):

    def clean_email(self):
        print self.cleaned_data

        mail = self.cleaned_data['email']

        try:
            match = Publisher.objects.get(email__iexact=mail)
        except:
            return self.cleaned_data['email']

        raise forms.ValidationError("This email already exists.")

    def clean_name(self):
        print self.cleaned_data
        name = self.cleaned_data['name']

        try:
            match = Publisher.objects.get(name__iexact=name)
        except:
            return self.cleaned_data['name']

        raise forms.ValidationError("This user already exists.")
    
    class Meta:
        model=Publisher
        fields='__all__'


class Bookform(forms.ModelForm):
    #publisher = forms.ModelChoiceField(queryset=Publisher.objects.all())

    def clean_title(self):
        bk = self.cleaned_data['title']
        try:
            book_name = Book.objects.get(title__iexact=bk)
        except Book.DoesNotExist:
            return self.cleaned_data['title']

        raise forms.ValidationError("This book already exists.")
    
    class Meta:
        model=Book
        #fields=['title','publisher','publication_date']
        fields='__all__'
