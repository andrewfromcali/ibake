from django.shortcuts import render_to_response

def foo(request):
    return render_to_response("green/foo.html")
