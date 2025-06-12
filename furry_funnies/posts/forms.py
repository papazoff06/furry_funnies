from django import forms

from furry_funnies.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CreatePostForm(PostBaseForm):
    class Meta:
        model = Post
        exclude = ['author', 'updated_at']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "Put an attractive and unique title..." },),
            'image_url': forms.TextInput(attrs={'helptext': " Share your funniest furry photo URL!" },),
            'content': forms.Textarea(attrs={'placeholder': "Share some interesting facts about your adorable pets..." })

        }
        error_messages = {
            'title': {
                'unique': "Oops! That title is already taken. How about something fresh and fun?",
            }
        }
        labels = {
            'image_url': 'Post Image URL',
            'content': 'Content',
        }

class EditPostForm(PostBaseForm):
    class Meta:
        model = Post
        exclude = ['author', 'updated_at']

class DeletePostForm(PostBaseForm):
    class Meta:
        model = Post
        exclude = ['author', 'updated_at']
        widgets = {
            'title': forms.TextInput(attrs={'readonly': True },),
            'image_url': forms.TextInput(attrs={'readonly': True },),
            'content': forms.Textarea(attrs={'readonly': True })
        }
