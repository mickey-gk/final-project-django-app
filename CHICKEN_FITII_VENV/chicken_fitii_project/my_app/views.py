from django.shortcuts import render
from django.utils import timezone #for rendering data according to time and date

# Create your views here.
def index(request):
    context = {
        'name': 'mickey',
        'age': '22'
        }
    return render(request, 'index.html', context)

