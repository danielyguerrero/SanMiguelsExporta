from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^$', views.index, name="dashboard"),
    url(r'^$', views.landing, name="home"),
    url(r'^products$', views.products, name="products"),
]