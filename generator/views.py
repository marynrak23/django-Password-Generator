from django.shortcuts import render
from django.http import HttpResponse
import random



def home(request):
    passLength = range(8, 23)

    return render(request, 'generator/home.html', {'passLength': passLength})


def password(request):
    charactersLower = list('qwertyuioplkjhgfdsazxcvbnm')
    charactersUpper = [item.upper() for item in charactersLower]
    numbers = list('1234567890')
    specialCharacters = list('!@#$%^&*()_+-~"№;:?')
    length = int(request.GET.get('length', 12))
    generatedPassword = ''

    if request.GET.get('uppercase'):
        charactersLower.extend(charactersUpper)

    if request.GET.get('number'):
        charactersLower.extend(numbers)

    if request.GET.get('special'):
        charactersLower.extend(specialCharacters)

    for x in range(length):
        generatedPassword += random.choice(charactersLower)

    return render(request, 'generator/password.html', {'password': str(generatedPassword)})


def about(request):
    return HttpResponse('<h1>About Page</h1>')

