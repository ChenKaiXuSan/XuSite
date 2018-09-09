from django.db import models

#===============================================================================
# 数据库模型
# 创建数据库表
#===============================================================================

class Author(models.Model):
    '''
    数据库中作者字段
    '''
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    email = models.EmailField(blank = True)
    
    # 返回名字全称
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
    def get_name(self):
        return self.__str__()
# 博客
#===============================================================================
class Blog(models.Model):
    # 博客标题
    blog_title = models.CharField(max_length = 100)
    # 博客创建日期
    blog_pub_date =models.DateTimeField('date published')
    # 博客创建时的天气
    weather = models.CharField(max_length = 10)
    # 博客创建者
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # 博客正文
    blog_content = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.blog_title    
 
    def get_all(self):
        return self.blog_title + self.author.__str__()