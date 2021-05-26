from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name='home'),
    path('<int:pk>',views.CandidateView.as_view(),name='candidate')
] 
