
from django.contrib import admin
from django.urls import path
from newconsumer.consumerapi.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register_user),
    path('validate/',auth_user),
    path('logout/',logout),
    path('add/',add_product),
    path('getall/',show_all_products),
    path('delete/<int:itid>',delete_product),
    path('prod/delete/',deleteproduct)
]
