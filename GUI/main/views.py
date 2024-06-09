from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import scripts

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')


def pops(request):
    if request.method=='POST':
        print(scripts.definition())
        # uploaded_file = request.FILES['file']
        # uploaded_file = uploaded_file.read().decode('utf-8')
        # print(uploaded_file)
        # print(scripts.aboba())
    else:
        print('ERROR')