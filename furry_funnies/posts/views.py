from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from furry_funnies.author.models import Author
from furry_funnies.posts.forms import CreatePostForm, EditPostForm, DeletePostForm
from furry_funnies.posts.models import Post
from furry_funnies.utils import get_author


# Create your views here.
class CreatePostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')


    def form_valid(self, form):
        # Get the current author, e.g., from request.user
        author = get_author()  # Assuming this function works correctly
        form.instance.author = author
        return super().form_valid(form)
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

class PostEditView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'posts/edit-post.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('dashboard')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    form_class = DeletePostForm
    model = Post
    template_name = 'posts/delete-post.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('dashboard')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
