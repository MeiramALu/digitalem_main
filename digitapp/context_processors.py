from .models import Lab

def labs(request):
    return {'labs': Lab.objects.all()}