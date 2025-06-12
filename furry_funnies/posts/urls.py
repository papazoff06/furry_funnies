from django.urls import path
from django.urls.conf import include

from furry_funnies.posts import views

urlpatterns = [
    path('create/', views.CreatePostView.as_view(), name='create-post'),
    path('<post_id>/', include([
        path('details/', views.PostDetailView.as_view(), name='details-post'),
        path('edit/', views.PostEditView.as_view(), name='edit-post'),
        path('delete/', views.PostDeleteView.as_view(), name='delete-post'),
    ]))
]