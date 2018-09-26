from django.http import HttpResponse


def  index(request):
    return HttpResponse("Hello My Name is Kévin")

# Create your views here.
