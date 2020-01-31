from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, mail_admins
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.template.defaultfilters import slugify
from django.template.loader import get_template
from django.utils import timezone
from .forms import CommentForm, BlogForm
from .models import Blog, Category, Comment
from taggit.models import Tag
from django.views.generic import (View, ListView,
DetailView, CreateView, UpdateView, DeleteView)


# Searching the Blog
def search_blog(request):
    queryset = Blog.objects.filter(status='published')
    query = request.GET.get('q')

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
        count_published = queryset.count()
    else:
        queryset = Blog.objects.filter(status='published')
        count_published = queryset.count()

    category_count = get_category_count()
    context = {
        'query': query,
        'queryset': queryset,
        'category_count': category_count,
        'count_published': count_published
    }
    return render(request, 'search_blog.html', context)


# Page where Blog Posts are displayed by Cateory
# Pagination in place with 4 posts displayed per page
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
    return render(request, 'category_detail.html', context)


# Count the number of posts in each category
def get_category_count():
    queryset = Blog \
        .objects \
        .filter(status='published') \
        .values('categories__title', 'categories__slug') \
        .annotate(Count('categories__title'))
    return queryset


# A view that displays all the blog pots on a blog page
# Pagination in place with 4 posts displayed per page
def blog(request):
    category_count = get_category_count()
    blog_items = Blog.objects.filter(status='published').order_by('-published')
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
        'category_count': category_count,
        'count_published': count_published,
    }
    return render(request, 'blog.html', context)


# Create a view that returns a single blog post based on the post
# slug and render it to the 'blog_post.html' template.
# Or return a 404 error if the post is not found
def blog_detail(request, slug):
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
            # Send an email to site administrator to flag comment 
            current_site = get_current_site(request)
            context = {
                'blog': blog,
                'current_site': current_site,
            }
            
            template = get_template('new_comment.txt')
            content = template.render(context)
            subject = 'Comment Awaiting approval'
            mail_admins(subject, content, fail_silently=True)
            messages.success(request, "Your comment has been submitted and is awaiting approval.")
            return redirect(reverse('blog_detail',
                            kwargs={'slug': blog.slug}))

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
        'category_count': category_count,
        'form': form,
    }

    return render(request, 'blog_post.html', context)


# Filter Posts by their tag
def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
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
        'tag': tag,
        'queryset': paginated_queryset,
        'category_count': category_count,
        'count_tags': count_tags,
    }
    return render(request, 'tag_detail.html', context)


# Allow Admin to create a blog through the site
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
            return redirect(reverse('blog_detail',
                            kwargs={'slug': form.instance.slug}))

    context = {
        'page_title': page_title,
        'form': form
    }
    return render(request, 'blog_create.html', context)


# Allow Admin to create a update through the site
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
            return redirect(reverse('blog_detail',
                            kwargs={'slug': form.instance.slug}))

    context = {
        'page_title': page_title,
        'form': form
    }
    return render(request, 'blog_create.html', context)


# Allow Admin to delete a blog post through the site
def blog_delete(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.delete()
    return redirect(reverse('blog'))
