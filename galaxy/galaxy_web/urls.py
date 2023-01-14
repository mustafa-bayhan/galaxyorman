from django.urls import path
from . import views

urlpatterns=[ 
    path('',views.index,name='index'),
    path('about-us',views.about,name='about'),
    path('contact-us',views.contact,name='contact'),
    path('news',views.news,name='news'),
    path('news/<slug:slug>',views.single_news,name='single-news'),
    path('products/<slug:slug>',views.single_product,name='single-product')
]