from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from blog.models import Blog, Author
from django.views.generic.detail import DetailView

# 基于类的通用视图
class BlogView(ListView):
    template_name = 'blog/index.html'
    model = Blog
    # 指定返回对象名称，未指定使用默认app名
    context_object_name = 'blog'
    
class Article(DetailView):
    template_name = 'blog/article.html'
    model = Blog
    context_object_name = 'blog'
    
    
def article(request):
    blog = get_object_or_404(Blog, pk = 1)
    context = { 'blog': blog,
               'flag': 'this is a flag '}
    print(context)
    return render (request, 'blog/article.html', context)

# 普通视图
def index(request):
    context = { 'blog_title': Blog().blog_title}
#     print(context)
    return render(request, 'blog/index.html', context)

class AuthorView(ListView): 
    template_name = 'blog/index.html'
    model = Author
    context_object_name = 'author'
   
def author(request): 
    author = get_object_or_404(Author,pk = 1)
    context = {'author' : author,              
               'author_last_name' : Author().last_name,
               'blog_title' : Blog().blog_title}
    print(context)
    return render(request, 'blog/index.html', context)

def Bootstrap(request):
    return render(request, 'blog/Bootstrap.html')



