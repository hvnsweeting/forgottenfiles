from django.shortcuts import render

from .models import Directory
from .utils import get_human_time, get_newest_files


def index(request):
    directories = Directory.objects.all()
    files = {}

    for d in directories:
        top_files = [(f, get_human_time(f))
                     for f in get_newest_files(d.fullpath, 10)]
        files[d.name] = {'fullpath': d.fullpath,
                         'files': top_files,
                         }

    context = {'files': files}
    return render(request, 'files/index.html', context)
