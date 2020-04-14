from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.PostListView.as_view(),name='home'),
    path('lp/',views.Baseview.as_view(),name='lp'),
    path('detail/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    path('newpost/',views.PostCreateView.as_view(),name = 'newpost'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('blog/<int:pk>/delete',views.ArticleDeleteView.as_view(),name='post_delete'),
    path('blog/<int:pk>/edit', views.PostUpdateView.as_view(), name='post_edit'),
    path('',views.lok,name='lok')

]