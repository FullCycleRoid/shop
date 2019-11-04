from django.conf.urls import url
from . import views

app_name = 'order'
urlpatterns = [
    url(r'^$', views.order_detail, name='order'),

]