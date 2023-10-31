from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_url, name="shorten_url"),
    path('<str:token>', views.redirect_to_original_url, name="redirect_to_original_url"),
    path('list/', views.url_list, name='url_list'),
]