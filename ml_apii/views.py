from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .apps import MlApiiConfig
import onnxruntime as ort
from PIL import Image
# from torchvision import transforms as transform
import base64
from io import BytesIO
import numpy as np

def run_model(model, x):

    outputs = model.run(None, {'image': x})
    predicted = outputs[0][0].argmax(0)
    # print(f'Predicted: "{predicted}"')
    return predicted

# imageTransform = transform.Compose(
#     [
#         transform.ToTensor(),
#         transform.Grayscale(),
#         transform.Resize((200,200)),

#     ]
# )
class call_model(APIView):

    def get(self,request):
        # if request.method == 'GET':
            
        # sentence is the query we want to get the prediction for
        # params = request.GET.get('image')
        # getting image from header
        # params = request.headers['image']
        # enc = base64.b64encode("./iPAD2_c40_EX06.jpg")
        # with open("./iPAD2_C40_EX06.jpg", "rb") as image_file:
        #     enc = base64.b64encode(image_file.read())
        enc = request.headers['image']
        img = Image.open(BytesIO(base64.b64decode(enc)))
        predictor = ort.InferenceSession("./models/plantIdentification.onnx")
        # img = Image.open(params)
        # img = imageTransform(img)
        # img = img.reshape((1,1,200,200))
        data = np.array(img)
        data = data/255
        data = data.reshape((1,1,100,100))
        data = data.astype(np.float32)
        # img2 = img.numpy()
        response = run_model(predictor,img)            
        # returning JSON response
        response= {"prediction":str(response)}
        return JsonResponse(response, safe=False)
# Create your views here.
