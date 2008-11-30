from django.shortcuts import render_to_response

def main(request):
    return render_to_response("main/main.html")

def main2(request):
    return render_to_response("main/main2.html")
