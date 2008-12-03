from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from ibake.models import Item
from google.appengine.ext import db

class ItemField(forms.Field):
    def clean(self, value):
        if not value:
            raise forms.ValidationError('This field is required.')
        value = value.strip()
        if len(value) == 0: 
            raise forms.ValidationError('This field is required.')
        if len(value) > 50:
            raise forms.ValidationError('This field is over 50 characters.')

        query = db.Query(Item)
        query.filter('permalink =', Item.get_friendly_url(value))
        if query.get():
            raise forms.ValidationError('This item already exists.')
        return value
        
class ContactForm(forms.Form):
    item = ItemField()
    
def main(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid():
            name = form.cleaned_data['item']
            sp = Item(name=name,permalink=Item.get_friendly_url(name),parent_permalink='-')
            sp.put()
            return HttpResponseRedirect('/') 
    else:
        form = ContactForm()

    query = Item.all()
    query.order('permalink')

    return render_to_response('main/main.html', {
        'form': form,
        'items': query.fetch(1000, 0),
    })