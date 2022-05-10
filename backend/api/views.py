import json
from django.http import JsonResponse

# Create your views here.

def api_home(request, *args, **kwargs):

    print(request.GET) #url query params
    body = request.body #byte string of JSON data
    data = {}
    try:
        data=json.loads(body) #String of JSON data -> Python Dict
    except:
        pass
    print(data.keys())
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)
    # return JsonResponse({"message":"Hi There, I am learning from CodingEntrepreneurs!!"})