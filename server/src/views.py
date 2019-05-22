from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. http response")

def data(request):
    print(request.body)
    return HttpResponse('data', request)