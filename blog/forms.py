from django import forms
from tinymce import TinyMCE
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from .models import Blog, Comment

#Form generated for creating blog posts
class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'content', 'status', 'seo_title', 'seo_description',
                  'tags', 'image', 'categories', 'featured')


#Form generated for adding comments to blog posts
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': '',
        'id': 'usercomment',
        'rows': '4',
        'value': ''
        }), label='')

    class Meta:
        model = Comment
        fields = ('content', )
