from django.shortcuts import render


def  index(request):
    data = {
        'title': 'Main page',
        'values': ['some', 'hello', '123'],
        'obj': {
            'car': 'bmw',
            'age': '39',
            'hobby': 'diving',
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'About us'
    }
    return render(request, 'main/about.html', data)


def contacts(request):
    data = {
        'title': 'Contacts'
    }
    return render(request, 'main/contacts.html', data)