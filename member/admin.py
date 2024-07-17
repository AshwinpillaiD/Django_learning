from django.contrib import admin
from .models import Blog_commmad,Blogmodel
# Register your models here.

class BlogmodelAdmin(admin.ModelAdmin):

    list_display = ('name', 'author', 'description')    # fields to display in the list view
    list_filter  = ('author',)                          # add filters in the right sidebar
    search_fields = ('author__username', )              # add search functionality 
    # search_fields = ('author__username', )            # add search functionality And Here is an example using the first option, assuming author is a FOREIGNKEY to a User model and you want to search by the username:

    ordering = ('description',)                         # default ordering of the list view
    # ordering = ('name',)                              # default ordering by 'name' in ascending order
    # ordering = ('-name',)                             # default ordering by 'name' in descending order
    # ordering = ('author', 'name')                     # primary ordering by 'author', secondary ordering by 'name'


    # fields = ('author',)                              # fields to display in the detail view
    readonly_fields = ('author',)                       # fields to display as read-only

    list_editable = ('description', )                   # fields that can be edited directly in the list view


admin.site.register(Blogmodel,BlogmodelAdmin)
admin.site.register(Blog_commmad)


admin.site.index_title="AP BLOG"
admin.site.site_header="AP BLOG ADMIN"
admin.site.site_title="AP BLOG TITLE"

