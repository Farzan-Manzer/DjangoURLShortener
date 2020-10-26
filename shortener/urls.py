from django.urls import path

from .views import redirect_view, index_view


urlpatterns = [
    path('', index_view),
    path('<str:code>/', redirect_view),
]

app_name = 'shortener'
