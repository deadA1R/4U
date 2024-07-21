from django.template.response import TemplateResponse

def login_cust(request):
    return TemplateResponse(request, 'login.html')
