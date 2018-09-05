from django.urls.conf import path

from . import views

urlpatterns =[

    path('',views.HomePageView.as_view(),name='home'),

]