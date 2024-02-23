from django.shortcuts import render
from .forms import ImageForm
from .models import Image

def uploader(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    context =  {'form' : form, 'img' : img}
    return render(request,'pexels.html',context)