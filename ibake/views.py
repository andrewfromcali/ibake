from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
import django;

def main(request):
  return render_to_response('main/main.html', {
      'form': django.VERSION
  })
