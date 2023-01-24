from django.urls import path
from . import views

urlpatterns=[ 
    path('',views.index,name='index'),    
    path('en',views.en,name='en'),
    path('hakkimizda',views.about,name='about'),
    path('about-us',views.about_en,name='about-en'),
    path('iletisim',views.contact,name='contact'),
    path('contact-us',views.contact_en,name='contact-en'),
    path('duyurular',views.news,name='news'),
    path('news',views.news_en,name='news-en'),
    path('duyurular/<slug:slug>',views.single_news,name='single-news'),
    path('news/<slug:slug>',views.single_news_en,name='single-news-en'),
    path('urunler/<slug:slug>',views.single_product,name='single-product'),
    path('products/<slug:slug>',views.single_product_en,name='single-product-en')
]
