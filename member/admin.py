from django.contrib import admin
from .models import Blog_commmad,Blogmodel
# Register your models here.



admin.site.register(Blogmodel)
admin.site.register(Blog_commmad)


admin.site.index_title="AP BLOG"
admin.site.site_header="AP BLOG ADMIN"
admin.site.site_title="AP BLOG TITLE"

