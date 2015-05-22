from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse 
from blog.models import Category, Post

import datetime


def index(request):
	# category_list = Category.objects.order_by('name')
	category_list = Category.objects.all().order_by('name')
	# post_list = Post.objects.order_by('title')
	post_list = Post.objects.all().order_by('title')
	context_dict = {'categories': category_list, 'posts': post_list}
	return render_to_response('blog/index.html', context_dict)
	# return render(request, 'blog/index.html', context_dict)

def view(request, postslug):
	post = Post.objects.get(slug=postslug)
	context = {'post': post}
	return render_to_response('blog/singlepost.html', context)

def category(reqeust, categoryslug):
	name = Category.objects.get(slug=categoryslug)
	posts = Post.objects.filter(category=name)
	context = {'posts': posts}
	return render_to_response('blog/singlecategory.html', context)
	#return render_to_response('blog/singlecategory.html')

class MyStruct(object):
	pass

def index1(request):
	#category_list = Category.objects.order_by('name')
	#page_list = Page.objects.order_by('title')
	c = MyStruct()
	c.company = 'Cool Star'
	c.title = 'Cool Star Blog'
	c.author_name = 'Jhon Smith'
	c.pub_date = datetime.datetime.now()
	c.article_list = [{'title':'Title1','text':'text1'},{'title':'Title2','text':'text2'},{'title':'Title3','text':'text3'}]
	
	return render(request, 'blog/index.html', c.__dict__)
	#context_dict = {'title': "It's my blog", 'boldmessage': "I'am bold font from the context", 'datet':datet, 'first':first,'second':second,'article_list':article_list }
	#return render(request, 'blog/index.html', context_dict)
	#return render(request, 'blog/index.html')
	# context = '<h2>Tango Blog is cool</h2> '+'Now is: '+str(datetime.datetime.now())  
	# return HttpResponse(context) 


def show(request):
	#category_list = Category.objects.order_by('name')
	#page_list = Page.objects.order_by('title')
	c = MyStruct()
	c.company = 'Cool Star'
	c.title = 'Cool Star Blog'
	c.author_name = 'Jhon Smith'
	c.pub_date = datetime.datetime.now()
	c.article_list = [{'title':'Title1','text':'text1'},{'title':'Title2','text':'text2'},{'title':'Title3','text':'text3'}]
	
	return render(request, 'blog/article.html', c.__dict__)
