from django import forms
from django.contrib import admin
from django_select2 import fields
from blog.models import Post, Category, UserProfile, Comment, Page, Slide, Slider
from ckeditor.widgets import CKEditorWidget

from redactor.widgets import RedactorEditor

#class PostAdmin(admin.ModelAdmin):
#	prepopulated_fields = {'slug': ('title',)}
#	list_display = ('title', 'category', 'author', 'status')
#	search_fields = ['title']

class PostAdminForm(forms.ModelForm):
    class Meta:
		model = Post
		fields = '__all__'
		widgets = {
           'body': RedactorEditor(),
        }

class PostAdmin(admin.ModelAdmin):
	form = PostAdminForm
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'category', 'author', 'status')
	search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "created"]

class SlideInline(admin.TabularInline):
    model = Slide
    extra = 1


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    inlines = [SlideInline, ]


admin.site.register(Slider, SliderAdmin)


# Page and Post actions


def publish_item(model_admin, request, queryset):
    queryset.update(status=models.ITEM_STATUS_PUBLISHED)


publish_item.short_description = "Publish selected items"


def hide_item(model_admin, request, queryset):
    queryset.update(status=models.ITEM_STATUS_HIDDEN)


hide_item.short_description = "Hide selected items"

# Page


class PageAdmin(admin.ModelAdmin):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Page
        fields = '__all__'

admin.site.register(Page, PageAdmin)

admin.site.register(UserProfile)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
