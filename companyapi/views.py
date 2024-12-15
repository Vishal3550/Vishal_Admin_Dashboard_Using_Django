from django.http import HttpResponse,JsonResponse


def home_page(request):
    print("home page requested")
    friends=[
        'ankit',
        'ravi',
        'uttam',
        'vishal'
    ]
    return JsonResponse(friends, safe=False)

