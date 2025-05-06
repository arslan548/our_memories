from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MemoryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

import re
from django.db import models

class MemoryVideo(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_youtube_video_id(self):
        """
        Extract the YouTube video ID from the youtube_link field.
        Supports URLs like:
        - https://www.youtube.com/watch?v=VIDEO_ID
        - https://youtu.be/VIDEO_ID
        - https://www.youtube.com/embed/VIDEO_ID
        Returns None if no valid ID found.
        """
        if not self.youtube_link:
            return None
        from urllib.parse import urlparse, parse_qs

        url = self.youtube_link
        parsed_url = urlparse(url)

        # Handle standard YouTube URL with v parameter
        if 'youtube.com' in parsed_url.netloc:
            query_params = parse_qs(parsed_url.query)
            video_ids = query_params.get('v')
            if video_ids and len(video_ids) > 0:
                video_id = video_ids[0]
                if len(video_id) == 11:
                    return video_id
            # Handle embed URLs
            path_parts = parsed_url.path.split('/')
            if 'embed' in path_parts:
                embed_index = path_parts.index('embed')
                if len(path_parts) > embed_index + 1:
                    video_id = path_parts[embed_index + 1]
                    if len(video_id) == 11:
                        return video_id
        # Handle shortened youtu.be URLs
        elif 'youtu.be' in parsed_url.netloc:
            video_id = parsed_url.path.lstrip('/')
            if len(video_id) == 11:
                return video_id

        return None

    def get_youtube_thumbnail_url(self):
        """
        Returns the YouTube thumbnail URL if youtube_link is present, else None.
        """
        video_id = self.get_youtube_video_id()
        if video_id:
            return f"https://img.youtube.com/vi/{video_id}/0.jpg"
        return None

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    pos_x = models.IntegerField(default=0)
    pos_y = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
