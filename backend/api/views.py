import json
from django.forms import model_to_dict
# from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.

# def api_home(request, *args, **kwargs):
#     print(request.GET) #url query params
#     body = request.body #byte string of JSON data
#     data = {}
#     try:
#         data=json.loads(body) #String of JSON data -> Python Dict
#     except:
#         pass
#     print(data.keys())
#     print(data)
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type

#     return JsonResponse(data)
#     # return JsonResponse({"message":"Hi There, I am learning from CodingEntrepreneurs!!"})


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data ={}
#     if model_data:

#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price 

#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#     return JsonResponse(data)

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data ={}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#     return Response(data)


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data ={}
#     if instance:
#         data = ProductSerializer(instance).data
#     return Response(data)


@api_view(["POST"])
def api_home(request, *args, **kwargs):

    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):

        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "Not good data title is required!"}, status=400 )
