from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world. http response")

@csrf_exempt
def data(request):
    print(request.body)
    return HttpResponse(request.body)