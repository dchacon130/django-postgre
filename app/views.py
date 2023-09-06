from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegistration
from .models import User

# Create your views here.
def index(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            number = fm.cleaned_data['number']
            firstname = fm.cleaned_data['firstname']
            lastname = fm.cleaned_data['lastname']
            birtday = fm.cleaned_data['birtday']
            language = fm.cleaned_data['language']
            country = fm.cleaned_data['country']
            reg = User(
                number=number, firstname=firstname, lastname=lastname,
                birtday=birtday, language=language, country=country)
            reg.save()
            fm = UserRegistration()
    else:
        fm = UserRegistration()
    stud = User.objects.all()
    
    return render(request, 'index.html', {
        'form': fm, 'stu':stud
    })

def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = UserRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = UserRegistration(instance=pi)

    return render(request, 'update.html', {
        'form': fm
    })

def delete(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()

    return HttpResponseRedirect('/')