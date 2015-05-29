from django.contrib import admin

from blog.models import Post, Category, UserProfile, Comment

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'category', 'author', 'status')
	search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "created"]

admin.site.register(UserProfile)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)