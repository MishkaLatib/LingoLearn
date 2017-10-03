from django.conf.urls import include, url
from . import views

app_name = 'LingoLearn'

urlpatterns =(
    url(r'^$', views.WelcomePage, name='WelcomePage'),
    url(r'^Categories/$', views.CategoriesPage.as_view(), name='CategoriesPage'),
    url(r'^Categories/(?P<category_id>[0-9])/$', views.item_list, name='items')
)