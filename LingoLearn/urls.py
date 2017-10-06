from django.conf.urls import include, url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout


app_name = 'LingoLearn'

urlpatterns =(
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout),
    url(r'^$', views.WelcomePage, name='WelcomePage'),
    url(r'^CategoryChoice/(?P<category_id>[0-9])/GamePlay/GainPoint/$',views.GainPoints,name='GainPoints' ),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^Score/$', views.getScore, name='score'),
    url(r'^SetScore/$', views.GainPoints, name='gain'),
    url(r'^ProfilePage/$', views.ProfileView.as_view(), name='ProfilePage'),
    url(r'^Categories/$', views.CategoriesPage.as_view(), name='CategoriesPage'),
    url(r'^Categories/(?P<category_id>[0-9])/$', views.item_list.as_view(), name='items'),
    url(r'^CategoryChoice/$', views.GameCategoriesPage.as_view(), name='GameCategoriesPage'),
    url(r'^CategoryChoice/(?P<category_id>[0-9])/GamePlay/$', views.GamePlay.as_view(), name='GamePlay'),
    url('r^', include('django.contrib.auth.urls'))

)
