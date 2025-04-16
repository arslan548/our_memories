from django.contrib import admin
from .models import Image, Video, MemoryImage, MemoryVideo, Note, Link

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url', 'uploaded_at')
    search_fields = ('title',)

@admin.register(MemoryImage)
class MemoryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)

@admin.register(MemoryVideo)
class MemoryVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'youtube_link', 'uploaded_at')
    search_fields = ('title',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'pos_x', 'pos_y')
    search_fields = ('title',)

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    search_fields = ('title',)
