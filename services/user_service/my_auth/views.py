from django.http import HttpResponse

def auth_view(request):
    return HttpResponse('AUTH')
