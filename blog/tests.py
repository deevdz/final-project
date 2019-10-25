from django.test import TestCase
from django.test.client import Client
from django.shortcuts import render, get_object_or_404, redirect, reverse
from allauth.utils import get_user_model
from .models import Blog, Category, Comment

class TestBlogModel(TestCase):

    def test_can_create_a_featured_blog_post(self):
        blog = Blog(title='Create a Test Blog', content='This is a test blog post', featured=True, tags='Test', user_id=1)
        user = get_user_model().objects.create(username='testuser')
        blog.save()
        self.assertEqual(blog.title, 'Create a Test Blog')
        self.assertEqual(blog.content, 'This is a test blog post')
        self.assertEqual(blog.tags, 'Test')
        self.assertEqual(blog.user_id, 1)

    def test_can_create_a_category(self):
        category = Category(title='Health')
        category.save()
        self.assertEqual(category.title, 'Health')
    
    def test_can_create_a_comment(self):
        comment = Comment(user_id=1, content='Testing', blog_id=2, approved=False)
        comment.save()
        self.assertEqual(comment.user_id, 1)
        self.assertEqual(comment.content, 'Testing')
        self.assertEqual(comment.blog_id, 2)
        self.assertEqual(comment.approved, False)
        
class TestBlogViews(TestCase):

    def test_get_blog_page(self):
        page = self.client.get('/blog/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'blog.html')
        
    def test_get_blog_post_page(self):
        test = Blog.objects.create(title='Test Blog', slug='testing-2',featured=True,user_id=1,image='test.png',)
        page = self.client.get(reverse('blog_detail', args=(test.slug,)))
        #print('Response content : ' + str(page.content))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'blog_post.html') 
        
    def test_get_category_page(self):
        test = Category.objects.create(title='Test Category', slug='health',)
        page = self.client.get(reverse('list_blog_by_category', args=(test.slug,)))
        #print('Response content : ' + str(page.content))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'category_detail.html')   
     