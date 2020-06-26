from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def battle_manager(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'battle_manager/battle_manager.html', context)

