from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView

from furry_funnies.author.forms import AuthorCreateForm
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
        context['last_update'] = last_update
        return context
