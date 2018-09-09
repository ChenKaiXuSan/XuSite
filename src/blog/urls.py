from django.urls import path
from . import views

'''
URL地址映射管理
'''
# 命名空间。当有多个应用存在时，用app_name来标识path中定义的name
app_name = 'blog'

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('Bootstrap', views.Bootstrap),
#     path('article', views.Article.as_view(), name='article-detail')
    path('article', views.article)
#     path('', views.AuthorView.as_view(), name='author')
    
#     the 'name' value as called by the {% url %} template tag 
#     path('', views.index, name='blog'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#     path('', views.author)
]