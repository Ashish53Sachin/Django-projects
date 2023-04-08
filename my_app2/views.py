from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

# # Create your views here.
# def hello_world_app2():
#     pass
from django.http import HttpResponse
# import datetime

def hello_world_app2(request):
    # now = datetime.datetime.now()
    html = "<html><body>YOU ARE IN MYAPP2</body></html>" 
    return HttpResponse(html)