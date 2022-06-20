from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new/', views.CreateView.as_view(), name='create'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('selfPublished/', views.FilterAuthorView.as_view(), name='selfPub'),
    path('orderDate/', views.OrderDateView.as_view(), name='orderDate'),
    path('today/', views.TodayView.as_view(), name='todayDate'),
]