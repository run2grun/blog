from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Blog
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def guest(request):
    blogs = Blog.objects
    return render(request,'guest.html', {'blogs':blogs})

def new(request):
    return render(request, 'new.html')

def create(request): #입력받은 함수를 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

