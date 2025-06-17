from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView, DeleteView

from furry_funnies.author.forms import AuthorCreateForm, AuthorEditForm
from furry_funnies.author.models import Author
from furry_funnies.utils import get_author


# Create your views here.
class CreateAuthorView(CreateView):
    model = Author
    template_name = 'author/create-author.html'
    form_class = AuthorCreateForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        author = get_author()
        context['author'] = author

        return context

class AuthorDetailView(TemplateView):
    model = Author
    template_name = 'author/details-author.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = get_author()
        last_update = author.posts.last().title
        context['author'] = author
        if last_update:
            context['last_update'] = last_update
        return context

class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'author/edit-author.html'
    success_url = reverse_lazy('author-details')
    author = get_author()

    def get_object(self, queryset=None):
        return self.author

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author/delete-author.html'
    success_url = reverse_lazy('home')
    author = get_author()
    def get_object(self, queryset=None):
        return self.author