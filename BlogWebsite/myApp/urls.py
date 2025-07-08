from django.urls import path
from .views import PostListView, PostDetailView
from django.views.generic import TemplateView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('contact/', TemplateView.as_view(template_name='contact_us.html'), name='contact_us'),
    path('report/', TemplateView.as_view(template_name='report.html'), name='report'),
    path('<slug:slug>/', PostDetailView.as_view(), name='blog_detail'),
]