from django.http import HttpResponse

def tryhelloworld(request):
    return HttpResponse("HelloWolrd")