"""yogastudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from home.views import index, about, contact, bikram_hot_yoga, meditation, pregnancy_yoga, reformer_bed, timetable, total_barre, what_do_i_need, yogalates
from blog import urls as urls_blog
from products import urls as urls_products
from checkout.views import checkout, payment, charge, order_view
from products.views import products
from cart.views import add_to_cart, decrease_cart, view_cart, remove_from_cart
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^about/', about, name='about'),
    url(r'^contact/', contact, name='contact'),
    url(r'^what-do-i-need/', what_do_i_need, name='what-do-i-need'),
    url(r'^reformer-bed/', reformer_bed, name='reformer-bed'),
    url(r'^yogalates/', yogalates, name='yogalates'),
    url(r'^total-barre/', total_barre, name='total-barre'),
    url(r'^bikram-hot-yoga/', bikram_hot_yoga, name='bikram-hot-yoga'),
    url(r'^pregnancy-yoga/', pregnancy_yoga, name='pregnancy-yoga'),
    url(r'^meditation/', meditation, name='meditation'),
    url(r'^timetable/', timetable, name='timetable'),    
    url(r'^blog/', include(urls_blog)),
    url(r'^workshops/', include(urls_products)),
    url(r'^shop/', products, name='products'),
    url(r'^cart/', view_cart, name='view_cart'), 
    url(r'^add/(?P<slug>[-\w]+)/$', add_to_cart, name='add_to_cart'),
    url(r'^remove/(?P<slug>[-\w]+)/$', remove_from_cart, name='remove_from_cart'),     
    url(r'^decrease/(?P<slug>[-\w]+)/$', decrease_cart, name='decrease_cart'),
    url(r'^checkout/', checkout, name='checkout'),
    url(r'^payment/', payment, name='payment'),
    url(r'^charge/', charge, name='charge'),  
    url(r'^orders/', order_view, name='order_view'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}) 
]
