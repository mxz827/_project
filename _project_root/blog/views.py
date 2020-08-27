from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import myBlog
from django.contrib.auth.decorators import login_required
from . import forms

def blog_list(request):
    blogs = myBlog.objects.all().order_by('date')
    return render(request,'blog/blog_list.html',{'blogs':blogs})

def blog_detail(request,slug):
    #return HttpResponse(slug)
    myblog = myBlog.objects.get(slug=slug)
    return render(request,'blog/blog_detail.html',{'myblog':myblog})

@login_required(login_url = '/accounts/login/')
def blog_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            #save article to database
            ins = form.save(commit=False)
            ins.author = request.user
            ins.save()
            return redirect('blog:list')
    else:
        form = forms.CreateArticle()
    return render(request,'blog/blog_create.html',{'form':form})

# Create your views here.
