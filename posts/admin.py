from django.contrib import admin
from posts.models import Author, Categoty, Post

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "user")

admin.site.register(Author)


admin.site.register(Categoty)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author","published_date","short_description")

admin.site.register(Post, PostAdmin)