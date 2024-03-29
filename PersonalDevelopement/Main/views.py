from django.shortcuts import HttpResponse
from django.shortcuts import render
# from django.http import loader
# from django.template import httpResponse

def Main(request):
    # template=loader.get_template("MainApp.html")
    # return httpResponse(template.render())
    return render(request,"MainApp.html")
