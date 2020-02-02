from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def upload(request):
    context = {}
    if request.method == 'POST':
        print("Posting Image")
        uploaded_video = request.FILES['video']
        print(uploaded_video.name)
        print(uploaded_video.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_video.name, uploaded_video)
        url = fs.url(name)
        print(url)
        context['url'] = url
        context['name'] = name
        return render(request, 'uploads/upload.html', context)
    else:
        print("Get Option")
        return render(request, 'uploads/upload.html')
