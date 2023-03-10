from . import views
from django.urls import path

urlpatterns = [
    path("", views.StoryList.as_view(), name="home"),
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('categories/edit/<int:pk>/', views.CategoryEdit.as_view(), name='category_edit'),
    path('categories/delete/<int:pk>/', views.CategoryDelete.as_view(), name='category_delete'),
    path('categories/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('stories/create/', views.StoryCreate.as_view(), name='story_create'),
    path('stories/edit/<int:pk>/', views.StoryEdit.as_view(), name='story_edit'),
    path('stories/delete/<int:pk>/', views.StoryDelete.as_view(), name='story_delete'),
    path('<slug:slug>/', views.StoryDetail.as_view(), name='story_detail'),
    path('library/<slug:slug>', views.LibraryAdd.as_view(), name='library_add'),
]
