from django.conf.urls import include, url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout


app_name = 'LingoLearn'

urlpatterns =(
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^$', views.WelcomePage, name='WelcomePage'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^ProfilePage/$', views.ProfileView.as_view(), name='ProfilePage'),
    url(r'^Categories/$', views.CategoriesPage.as_view(), name='CategoriesPage'),
    url(r'^Categories/(?P<category_id>[0-9])/$', views.item_list.as_view(), name='items'),
    url('^', include('django.contrib.auth.urls'))
)
