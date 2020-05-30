from django.shortcuts import render
from .models import UserFile
from .forms import PostForm
# Create your views here.


def homepage(request):
    context = {}
    return render(request, "html/index.html", context=context)


def upload_file(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            info = "Файл успешно загружен."
            print(info)

            return render(request, 'html/index.html', {'form': form, 'info': info})
    else:
        form = PostForm()
        print("No")
    return render(request, 'html/index.html', {'form': form})
