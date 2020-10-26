__all__ = ['index_view', 'redirect_view']

from django.shortcuts import redirect, render

from .models import ShortURL


def index_view(request):
    return render(request, 'shortener/index.html')


def redirect_view(request, code):
    try:
        short_url = ShortURL.objects.get(code=code)
        return redirect(short_url.url)
    except ShortURL.DoesNotExist:
        return render(request, 'shortener/NotFound404.html')
