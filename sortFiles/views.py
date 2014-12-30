from django.shortcuts import render
from sortFiles.mp3Collection import mp3Collection
from sortFiles.trackedShow import trackedShow

from sortFiles.models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'sortFiles/index.html', context)

def mp3TorrentList(request):
    mediaDirectory = '/media/hd0/Torrents'

    torrentDirectoryList = mp3Collection.getMusicFromDirectory(mediaDirectory)
    context = {'torrentDirectoryList': torrentDirectoryList}
    return render(request, 'sortFiles/torrentList.html', context)

def showList(request):
    context = {'tvShow': trackedShow}
    return render(request, 'sortFiles/showList.html', context)