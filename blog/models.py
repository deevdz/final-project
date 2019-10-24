from django.db import models
from django.conf import settings
from django.utils import timezone
from tinymce import HTMLField
from django.urls import reverse
from taggit.managers import TaggableManager

# Create Categories for Blog Items with slugs
class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=250, unique=True)
    blurb = models.TextField(default='',blank=True, null=True,)
    
    class Meta:
        ordering = ('title'),
        verbose_name = 'category',
        verbose_name_plural = 'categories'
        
    def get_absolute_url(self):
        return reverse('list_blog_by_category', args=[self.slug])

    def __str__(self):
        return self.title

#Create Blog Items with slugs
class Blog(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published','Published'),
        )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    content = HTMLField()
    created_date = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')
    seo_title = models.CharField(max_length=250, blank=True, null=True)
    seo_description = models.CharField(max_length=250, blank=True, null=True)
    views = models.IntegerField(default=0)
    tags = TaggableManager()
    image = models.ImageField(upload_to="img")
    featured = models.NullBooleanField(blank=False)
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.slug])
        
    def get_update_post_url(self):
        return reverse('blog_update', args=[self.slug])
        
    def get_delete_post_url(self):
        return reverse('blog_delete', args=[self.slug])        
        
    @property
    def get_comments(self):
        return self.comments.order_by('-timestamp').filter(approved=True)

#Create comments for blog items
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    blog = models.ForeignKey(
        'Blog', related_name='comments', on_delete=models.CASCADE)
    approved = models.BooleanField()
    
    def __str__(self):
        return self.user.username
