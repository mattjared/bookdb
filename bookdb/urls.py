from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from collection import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about/$',TemplateView.as_view(template_name='about.html'),name='about'),
    url(r'^contact/$',TemplateView.as_view(template_name='contact.html'),name='contact'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/(?P<slug>[-\w]+)/$', views.book_detail, name='book_detail'),
    url(r'^books/(?P<slug>[-\w]+)/edit/$', views.edit_book, name='edit_book'),
    url(r'^accounts/', include('registration.backends.simple.urls'))
]