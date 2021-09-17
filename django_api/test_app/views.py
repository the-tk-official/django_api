from django.shortcuts import render
from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def simple(request):
    # perform operations
    method = request.method.lower()
    if method == 'get':
        return JsonResponse({'data': [1, 2, 3, 4, 5]})
    elif method == "post":
        return JsonResponse({'data': 'Added data successfully!'})
    elif method == 'put':
        return JsonResponse({'data': 'Updated data successfully!'})
    return JsonResponse({'error': 'Method not allowed'})
