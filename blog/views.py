from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
from .forms import CommentForm, BlogForm
from .models import Blog, Category, Comment
from taggit.models import Tag
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

# Searching the Blog
def search_blog(request):
    queryset = Blog.objects.filter(status = 'published')
    query = request.GET.get('q')
    
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
        count_published = queryset.count()
    else:
        queryset = Blog.objects.filter(status = 'published')
        count_published = queryset.count()
        
    category_count = get_category_count()
    context = {
        'query':query,
        'queryset': queryset,
        'category_count': category_count,
        'count_published': count_published
    }
    return render(request, 'search_blog.html', context)


#Page where Blog Posts are displayed by Cateory
def list_blog_by_category(request, slug):
    categories = Category.objects.all()
    category_count = get_category_count()
    blog_items = Blog.objects.filter(status='published')
    
    if slug:
        category = get_object_or_404(Category, slug=slug)
        blog_items = blog_items.filter(categories=category).distinct()
        count_published = blog_items.count()
        paginator = Paginator(blog_items, 4)
        page_request_var = 'page'
        page = request.GET.get(page_request_var)
        paginated_queryset = ''
    
        if blog_items:
            try:
                paginated_queryset = paginator.page(page)
            except PageNotAnInteger:
                paginated_queryset = paginator.page(1)
            except EmptyPage:
                paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'categories': categories,
        'queryset': paginated_queryset,
        'category': category,
        'category_count': category_count
    }
    return render(request,'category_detail.html', context )

# Count the number of posts in each category
def get_category_count():
    queryset = Blog \
        .objects \
        .filter(status='published') \
        .values('categories__title', 'categories__slug') \
        .annotate(Count('categories__title'))
    return queryset


def blog(request):
    """A view that displays all the blog Stories on a blog Page"""
    category_count = get_category_count()
    blog_items = Blog.objects.filter(status='published').order_by('-created_date')
    count_published = blog_items.count()
    paginator = Paginator(blog_items, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    paginated_queryset = ''
    
    if blog_items:
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'category_count' : category_count,
        'count_published': count_published,
    }
    return render(request, 'blog.html', context)

def blog_detail(request, slug):
    """
    Create a view that returns a single
    blog post based on the post slug and
    render it to the 'blog_post.html' template.
    Or return a 404 error if the post is
    not found
    """
    blog = get_object_or_404(Blog, slug=slug)
    blog.views += 1
    blog.save()
    category_count = get_category_count()
    
    form = CommentForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.blog = blog
            form.instance.approved = False
            form.save()
            return redirect(reverse('blog_detail', kwargs={'slug': blog.slug
            }))    
    
    try:
        next_blog = blog.get_next_by_created_date()
    except Blog.DoesNotExist:
        next_blog = None
    try:
        previous_blog = blog.get_previous_by_created_date()
    except Blog.DoesNotExist:
            previous_blog = None
    
    context = {
        'blog': blog,
        'next_blog': next_blog,
        'previous_blog': previous_blog,
        'category_count' : category_count,
        'form' : form,
    }
    
    return render(request, 'blog_post.html', context)
    
def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    blog_items = Blog.objects.filter(tags=tag, status='published')
    count_tags = blog_items.count()
    category_count = get_category_count()
    paginator = Paginator(blog_items, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    paginated_queryset = ''
    
    if blog_items:
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'tag':tag,
        'queryset':paginated_queryset,
        'category_count': category_count,
        'count_tags': count_tags,
    }
    return render(request, 'tag_detail.html', context)
    
def blog_create(request):
    page_title = 'Create Blog Post'
    form = BlogForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.slug = slugify(newpost.title)
            newpost.user = request.user
            newpost.save()
            form.save_m2m()
            return redirect(reverse('blog_detail', kwargs={'slug': form.instance.slug
            }))
    
    context = {
        'page_title': page_title,
        'form': form
    }
    return render(request, 'blog_create.html', context)
            

def blog_update(request, slug):  
    page_title = 'Update Blog Post'
    blog = get_object_or_404(Blog, slug=slug)
    form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
    if request.method == 'POST':
         if form.is_valid():
            newpost = form.save(commit=False)
            newpost.slug = slugify(newpost.title)
            newpost.user = request.user
            newpost.save()
            form.save_m2m()
            return redirect(reverse('blog_detail', kwargs={'slug': form.instance.slug
            }))
    
    context = {
        'page_title': page_title,
        'form': form
    }
    return render(request, 'blog_create.html', context)

def blog_delete(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.delete()
    return redirect(reverse('blog'))