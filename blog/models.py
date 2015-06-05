from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from utils import helpers

BLOG_ITEM_STATUS = (
        ('0', 'Dratf'),
        ('1', 'Published'),
        ('2', 'Not Published'),
)

ITEM_STATUS_PUBLISHED = 1
ITEM_STATUS_HIDDEN = 2
ITEM_STATUS_CHOICES = (
    (ITEM_STATUS_PUBLISHED, "Published"),
    (ITEM_STATUS_HIDDEN, "Hidden"),
)

def get_blog_file_name(instance, filename):
    return helpers.get_file_filename(instance, filename, "blog")

class Slider(models.Model):
    status = models.IntegerField(choices=ITEM_STATUS_CHOICES, default=ITEM_STATUS_PUBLISHED)
    title = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return self.__str__()


class Slide(models.Model):
    status = models.IntegerField(choices=ITEM_STATUS_CHOICES, default=ITEM_STATUS_PUBLISHED)
    title = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(max_length=1024, null=True, blank=True, upload_to=get_blog_file_name)
    related_slider = models.ForeignKey(Slider)

    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return self.__str__()

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.name

class Post(models.Model):
	category = models.ForeignKey(Category)
	author = models.ForeignKey(User)
	title = models.CharField(max_length=128)
	slug   = models.SlugField(unique=True)
	body = models.TextField()
	url = models.URLField()
	views = models.IntegerField(default=0)
	status = models.IntegerField(choices=ITEM_STATUS_CHOICES, default=ITEM_STATUS_PUBLISHED)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['created']

	def __unicode__(self):
		return self.title

class Page(models.Model):
    status = models.IntegerField(choices=ITEM_STATUS_CHOICES, default=ITEM_STATUS_PUBLISHED)
    title = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    #content = models.TextField()
    content = RichTextField()
    #widgets = models.ManyToManyField(Widget, null=True, blank=True)
    featured_image = models.ImageField(max_length=1024, null=True, blank=True, upload_to=get_blog_file_name)
    related_slider = models.ForeignKey(Slider, null=True, blank=True)

    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return self.__str__()

#    def get_widgets(self):
#        return self.widgets.all()



class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))
