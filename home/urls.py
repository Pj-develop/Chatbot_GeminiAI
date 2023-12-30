from django.contrib import admin
from django.urls import path, include
from .views import predict_article,input_form
from home import views
# from .views import try1

urlpatterns = [
    path("",views.index,name='home'),
    path("index",views.index,name='home'),
    path("support",views.support,name="support"),
    path("try1",input_form,name="try1"),
    path("neutralizer",views.neutralizer,name="neutralizer"),
    path('predict', predict_article, name='predict_article')
]


