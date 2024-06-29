from django.urls import path
from . import views


urlpatterns = [
    #path('', ArticleListView.as_view(), name='article_list'),
    path('',views.article_list,name='article_list'),
    #path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>',views.article_detail,name='article_detail'),
    #path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/edit/',views.article_update,name='article_update'),
    #path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/delete/',views.article_delete,name='article_delete'),
    #path('new/', ArticleCreateView.as_view(), name='article_create'),
    path('new/',views.article_create,name='article_create'),
]