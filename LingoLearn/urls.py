from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.WelcomePage, name='Welcome'),
    url(r'^Categories/$', views.CategoriesPage, name='CategoriesPage'),
    url(r'^Categories/(?P<category_id>[0-9])/$', views.item_list, name='items')
]
