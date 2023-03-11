
from django.contrib import admin
from django.urls import path
from my_crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index,name='home'),
    path('add',views.Add,name='add'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('update/edit/<int:id>',views.edit,name='edit'),
    path('search',views.search,name='search')
]
