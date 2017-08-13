from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^buy_product$', views.buy_product),
    url(r'^checkout$', views.checkout),
]
