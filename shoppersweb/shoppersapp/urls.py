from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.landing_page,name='landing_page'),
    url(r'^mobiles$',views.mobiles_page,name='mobiles_page'),
    url(r'^cars$',views.cars_page,name='cars_page'),
    url(r'^motorcycles$',views.motorcycles_page,name='motorcycles_page'),
    url(r'^bicycles$',views.bicycles_page,name='bicycles_page'),
    url(r'^laptops$',views.laptops_page,name='laptops_page'),
    url(r'^apartments$',views.apartments_page,name='apartments_page'),

]
