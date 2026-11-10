from django.urls import path

from . import views

app_name = 'ice_cream'

urlpatterns = [
    path('list/', views.ice_cream_list, name='ice_cream_list'),
    path('<int:pk>/', views.ice_cream_detail, name='ice_cream_detail'),
    path('<int:pk>/edit/', views.ice_cream_list, name='edit'),
    path('<int:pk>/delete/', views.ice_cream_list, name='delete')
]