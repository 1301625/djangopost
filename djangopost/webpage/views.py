from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
def main(request):
    return  render(request,'webpage/layout.html')
    

def Home(request):
    return render(request,'webpage/home.html')
# Create your views here.

def News(request):
    temp = [1,2,3,4,5,6,7,8,9]
    context = {"number":temp}
    return render(request,'webpage/news.html', context= context)
def Contact(request):
    return render(request, 'webpage/contact.html')
def About(request):
    return render(request, 'webpage/about.html')


class MyView(View):
    def get(self,request):
        return HttpResponse('result')
