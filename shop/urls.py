from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name="ProductByCategory"),
    url(r'^(?P<slug>[-\w]+)/(?P<id>\d+)/$', views.product_detail, name='ProductDetail'),
    url(r'^$', views.product_list, name="product_list")
]