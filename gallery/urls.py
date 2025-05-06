from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('images/', views.images, name='images'),
    path('images/<int:image_id>/', views.image_detail, name='image_detail'),
    path('images/<int:image_id>/delete/', views.delete_image, name='delete_image'),
    path('videos/', views.videos, name='videos'),
    path('links/', views.links, name='links'),
    path('images/<int:image_id>/edit/', views.edit_image, name='edit_image'),
    path('notes/<int:note_id>/edit/', views.edit_note, name='edit_note'),
    path('videos/<int:video_id>/edit/', views.edit_video, name='edit_video'),
    path('links/<int:link_id>/edit/', views.edit_link, name='edit_link'),
    path('add_link/', views.add_link, name='add_link'),
    path('links/<int:link_id>/', views.link_detail, name='link_detail'),
    path('notes/', views.notes_view, name='notes'),
    # Removed notes_list URL as per user request
    # path('notes_list/', views.notes_list, name='notes_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('videos/<int:video_id>/', views.video_detail, name='video_detail'),
    path('videos/<int:video_id>/delete/', views.delete_video, name='delete_video'),
    path('add/', views.add_note, name='add_note'),
    path('<int:pk>/', views.note_detail, name='note_detail'),
    path('<int:pk>/delete/', views.delete_note, name='delete_note'),
    path('add_note/', views.add_note, name='add_note'),  # if you have a form to add notes
    path('update_note_position/', views.update_note_position, name='update_note_position'),
]
