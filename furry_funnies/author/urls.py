from django.urls import path

from furry_funnies.author import views

urlpatterns = [
    path('create/', views.CreateAuthorView.as_view(), name='create-author'),
    path('details/', views.AuthorDetailView.as_view(), name='author-details'),
]