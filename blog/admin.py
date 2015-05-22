from django.contrib import admin

from blog.models import Post, Category, UserProfile

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'category', 'author', 'status')
	search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(UserProfile)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)