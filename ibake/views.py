from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from ibake.models import Item

class ItemField(forms.Field):
    def clean(self, value):
        if not value:
            raise forms.ValidationError('This field is required.')
        value = value.strip()
        if len(value) == 0: 
            raise forms.ValidationError('This field is required.')
        if len(value) > 50:
            raise forms.ValidationError('This field is over 50 characters.')

        return value
        
class ContactForm(forms.Form):
    item = ItemField()
    
def main(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid():
            item = form.cleaned_data['item']
            
            return HttpResponseRedirect('/') 
    else:
        form = ContactForm()

    return render_to_response('main/main.html', {
        'form': form,
    })