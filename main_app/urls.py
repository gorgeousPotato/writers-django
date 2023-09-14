from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('writers/', views.writers_index, name='index'),
  path('writers/<int:writer_id>', views.writers_detail, name='detail'),
  path('writers/create/', views.WriterCreate.as_view(), name='writer_create'),
  path('writers/<int:pk>/update/', views.WriterUpdate.as_view(), name='writer_update'),
  path('writers/<int:pk>/delete/', views.WriterDelete.as_view(), name='writer_delete'),
  path('writers/<int:writer_id>/add_book/', views.add_book, name='add_book')
]