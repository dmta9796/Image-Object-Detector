from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
import sys
import os
from PIL import Image
# sys.path.append('./PyTorch-YOLOv3')
#import src.PyTorch-YOLOv3.models
# from man.PyTorchYOLOv3 import models
#from ../PyTorch-YOLOv3/models import *
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
import src.PyTorchYOLOv3.models as models
import src.PyTorchYOLOv3.detect as detect


def image_to_byte_array(image:Image):
  imgByteArr = io.BytesIO()
  image.save(imgByteArr, format=image.format)
  imgByteArr = imgByteArr.getvalue()
  return imgByteArr


def index(request):
    return HttpResponse("Hello, world. http response")

@csrf_exempt
def data(request):
    data = request.body
    image = Image.open(io.BytesIO(data))
    processedimage = detect.detectimage(image)
    print(processedimage)
    return HttpResponse(image_to_byte_array(processedimage))