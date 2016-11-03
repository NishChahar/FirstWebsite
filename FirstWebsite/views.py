from django.shortcuts import render


def base(request):
    return render(request, 'Home/index.html', {})
