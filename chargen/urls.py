from . import views
from django.urls import path

urlpatterns = [
    path("", views.StoryList.as_view(), name="home"),
    path('categories/', views.CategoryView.as_view(), name='add_category'),
    path('categories/<int:id>/', views.CategoryView.as_view(), name='edit_category'),
    path('<slug:slug>/', views.StoryDetail.as_view(), name='story_detail'),
    path(
        'library/<slug:slug>', views.LibraryAdd.as_view(),
        name='library_add'),
]
