from django.urls import path

from furry_funnies.common import views

urlpatterns = [
    path('', views.ShowHomePageView.as_view(), name='home'),
    path('dashboard/', views.dashboard_page_view, name='dashboard'),
]