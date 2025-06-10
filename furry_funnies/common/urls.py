from django.urls import path

from furry_funnies.common import views

urlpatterns = [
    path('', views.ShowHomePageView.as_view(), name='home'),
]