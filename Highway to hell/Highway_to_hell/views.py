from django.shortcuts import render
from Highway_to_hell.models import Highway, UserWant


# Create your views here.
def index(request):
    highway = Highway.objects.all()
    Select_highway = request.GET.get('se_highway')
    context = {
        'highway':  Highway.objects.all()
    }
    return render(request, 'highway/index.html', context)