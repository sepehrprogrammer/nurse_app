from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.CreateCommunicationView.as_view(), name='createCommunication'),
    path('', views.CommunicationListView.as_view(), name='communication'),
    path('detail/<int:pk>/', views.CommunicationDetailView.as_view(), name='communication_detail'),

]