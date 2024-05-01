# Create your views here.
from django.shortcuts import render,redirect
# imported our models
from django.core.paginator import Paginator
from . models import Song
from .forms import SongForm
from django.contrib import messages



def index(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    songs = Song.objects.all()  # Lấy tất cả bài hát
    context={"page_obj":page_obj, 'songs': songs,}
    return render(request,"index.html",context)

def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'index.html', {'song': song})

def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Song added successfully!')
    else:
        form = SongForm()
    return render(request, 'add_song.html', {'form': form})
