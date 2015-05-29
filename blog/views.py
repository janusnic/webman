from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse 
from blog.models import Category, Post, Comment
from blog.forms import UserForm, UserProfileForm, CommentForm

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage 
from django.core.urlresolvers import reverse
import time 
from calendar import month_name 

def index(request):
	# category_list = Category.objects.order_by('name')
    category_list = Category.objects.all().order_by('name')
    # post_list = Post.objects.order_by('title')
    posts = Post.objects.all().order_by("-created") 
    # post_list = Post.objects.all().order_by('title')
    paginator = Paginator(posts, 2) 

    try: page = int(request.GET.get("page", '1')) 
    except ValueError: page = 1 

    try: 
        posts = paginator.page(page) 
    except (InvalidPage, EmptyPage): 
        posts = paginator.page(paginator.num_pages) 
	
	# context_dict = {'categories': category_list, 'posts': post_list}
	# return render_to_response('blog/index.html', context_dict)
    context_dict = {'categories': category_list, 'posts': posts, 'months':mkmonth_lst(),  'archive':True} 
    return render_to_response("blog/index.html", context_dict)
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

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'blog/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def ulogin(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
            # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/blog/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Blog account is disabled.")
        else:
       # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'blog/login.html', {})

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/blog/')

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

def add_comment(request, postslug): 
    """Add a new comment.""" 
    p = request.POST 
    if p["body"]: 
        author = request.user 
        comment = Comment(post=Post.objects.get(slug=postslug)) 
        cf = CommentForm(p, instance=comment) 
        
        cf.fields["author"].required = False 
        comment = cf.save(commit=False) 
        comment.author = author 
        comment.save() 
    return HttpResponseRedirect('/blog/')

def view(request, postslug): 
    post = Post.objects.get(slug=postslug) 
    comments = Comment.objects.filter(post=post) 
    context = {'post': post, "comments":comments,"form":CommentForm(), "user":request.user} 
    context.update(csrf(request)) 
    return render_to_response('blog/singlepost.html', context) 

def mkmonth_lst(): 
    """Make a list of months to show archive links.""" 

    if not Post.objects.count(): return [] 

    # set up vars 
    year, month = time.localtime()[:2] 
    first = Post.objects.order_by("created")[0] 
    fyear = first.created.year 
    fmonth = first.created.month 
    months = [] 

    # loop over years and months 
    for y in range(year, fyear-1, -1): 
        start, end = 12, 0 
        if y == year: start = month 
        if y == fyear: end = fmonth-1 

        for m in range(start, end, -1): 
            months.append((y, m, month_name[m])) 
    return months 

def month(request, year, month): 
    """Monthly archive.""" 

    posts = Post.objects.filter(created__year=year, created__month=month) 
    
    paginator = Paginator(posts, 2) 
      
    try: page = int(request.GET.get("page", '1')) 
    except ValueError: page = 1 

    try: 
        posts = paginator.page(page) 
    except (InvalidPage, EmptyPage): 
        posts = paginator.page(paginator.num_pages) 

    return render_to_response("blog/list.html", dict(posts=posts, user=request.user, months=mkmonth_lst(),  archive=True)) 
