from django.http import JsonResponse

# Create your views here.

def api_home(request, *args, **kwargs):
    return JsonResponse({"message":"Hi There, I am learning from CodingEntrepreneurs!!"})