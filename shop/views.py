from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = ProductForm()
    return render(request, 'shop/home.html', locals())


def test(request):
    return HttpResponse('<h1> test </h1>')
