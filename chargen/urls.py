from . import views
from django.urls import path

urlpatterns = [
    path("", views.StoryList.as_view(), name="home"),
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('categories/edit/<int:pk>/', views.CategoryEdit.as_view(), name='category_edit'),
    path('categories/delete/<int:pk>/', views.CategoryDelete.as_view(), name='category_delete'),
    path('categories/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('stories/create/', views.StoryCreate.as_view(), name='story_create'),
    path('<slug:slug>/', views.StoryDetail.as_view(), name='story_detail'),
    path('library/<slug:slug>', views.LibraryAdd.as_view(), name='library_add'),
    path('library/view/', views.LibraryList.as_view(), name='library_view'),
    # path("library/", views.StoryLibrary.as_view(), name="library"),
    # path('category/character/', views.CategoryDetail.as_view(), name='category_detail'),
]
