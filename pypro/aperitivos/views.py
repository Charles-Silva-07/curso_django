from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 58479},
        'instalacao-windows': {'titulo': 'Instalação windows', 'vimeo_id': 58625},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
