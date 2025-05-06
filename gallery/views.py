from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import json
from .forms import MemoryImageForm, MemoryVideoForm, LinkForm
from .models import MemoryImage, MemoryVideo, Note, Link

@login_required
def images(request):
    if request.method == 'POST':
        form = MemoryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = MemoryImageForm()

    images = MemoryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery/images.html', {'form': form, 'images': images})

@login_required
def image_detail(request, image_id):
    image = get_object_or_404(MemoryImage, id=image_id)
    return render(request, 'gallery/image_detail.html', {'image': image})

@login_required
def delete_image(request, image_id):
    image = get_object_or_404(MemoryImage, id=image_id)
    if request.method == 'POST':
        image.image.delete()
        image.delete()
        return redirect('images')
    return redirect('image_detail', image_id=image_id)

def home(request):
    return render(request, 'gallery/home.html')

@login_required
def videos(request):
    if request.method == 'POST':
        form = MemoryVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = MemoryVideoForm()

    videos = MemoryVideo.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery/videos.html', {'form': form, 'videos': videos})

@login_required
def video_detail(request, video_id):
    video = get_object_or_404(MemoryVideo, id=video_id)
    return render(request, 'gallery/video_detail.html', {'video': video})

@login_required
def delete_video(request, video_id):
    video = get_object_or_404(MemoryVideo, id=video_id)
    if request.method == 'POST':
        if video.video_file:
            video.video_file.delete()
        video.delete()
        return redirect('videos')
    return redirect('video_detail', video_id=video_id)

@login_required
def links(request):
    links = Link.objects.all().order_by('-id')
    return render(request, 'gallery/links.html', {'links': links})

@login_required
def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('links')
    else:
        form = LinkForm()
    return render(request, 'gallery/add_link.html', {'form': form})

@login_required
def link_detail(request, link_id):
    link = get_object_or_404(Link, id=link_id)
    return render(request, 'gallery/link_detail.html', {'link': link})

# Custom Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the credentials are the same as the custom ones
        if username == "ArsMan" and password == "a0425m":
            user = authenticate(request, username=username, password=password)
            if user is None:
                user = User.objects.create_user(username=username, password=password)  # Create user if it doesn't exist

            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to homepage after login
        else:
            error_message = "Invalid credentials, please try again."
            return render(request, 'gallery/login.html', {'error_message': error_message})
    else:
        return render(request, 'gallery/login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')

# Removed notes_list view as per user request
# @login_required
# def notes_list(request):
#     notes = Note.objects.order_by('-created_at')
#     return render(request, 'gallery/notes_list.html', {'notes': notes})

@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'gallery/note_detail.html', {'note': note})

@login_required
def add_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(title=title, content=content)
        return redirect('notes')
    return render(request, 'gallery/add_note.html')

from django.views.decorators.csrf import csrf_exempt

@login_required
@csrf_exempt
def update_note_position(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            note_id = data.get('note_id')
            pos_x = data.get('pos_x')
            pos_y = data.get('pos_y')
            note = Note.objects.get(id=note_id)
            note.pos_x = pos_x
            note.pos_y = pos_y
            note.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('notes_list')

@login_required
def notes_view(request):
    notes = Note.objects.all()
    return render(request, 'gallery/notes.html', {'notes': notes})

# Additional imports for forms
from .forms import MemoryImageForm, NoteForm, MemoryVideoForm, LinkForm

@login_required
def edit_image(request, image_id):
    image = get_object_or_404(MemoryImage, id=image_id)
    if request.method == 'POST':
        form = MemoryImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('image_detail', image_id=image.id)
    else:
        form = MemoryImageForm(instance=image)
    return render(request, 'gallery/edit_image.html', {'form': form})

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', pk=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'gallery/edit_note.html', {'form': form})

@login_required
def edit_video(request, video_id):
    video = get_object_or_404(MemoryVideo, id=video_id)
    if request.method == 'POST':
        form = MemoryVideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('video_detail', video_id=video.id)
    else:
        form = MemoryVideoForm(instance=video)
    return render(request, 'gallery/edit_video.html', {'form': form})

@login_required
def edit_link(request, link_id):
    link = get_object_or_404(Link, id=link_id)
    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            return redirect('link_detail', link_id=link.id)
    else:
        form = LinkForm(instance=link)
    return render(request, 'gallery/edit_link.html', {'form': form})
