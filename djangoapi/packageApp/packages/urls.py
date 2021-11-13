from django.contrib import admin
from django.urls import path
from packages import views

urlpatterns = [
    path('project2/package/<id>', ),
    path('project2/package/byName/<name>', ),
    #path('project2/authenticate', ),
    path('project2/reset', ),
    #path('project2/packages?offset=2'),
    path('project2/package')
]