from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('error', views.error, name='error'),
    path('success', views.success, name='success'),
    path('records', views.records, name='records'),
    path('error_book', views.error_book, name='error_book'),
    path('delete/<int:record_id>', views.delete_record, name='delete'),
    path('delete_success', views.delete_success, name='delete_success')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
