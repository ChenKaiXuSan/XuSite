from django.contrib import admin
from blog.models import Blog, Author

# 将模块注册到管理工具中
# admin.site.register(Blog)

# 使用装饰器修饰模块
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # 在列表中排列显示信息
    list_display = ('first_name', 'last_name', 'email')
    

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'author', 'blog_pub_date')
