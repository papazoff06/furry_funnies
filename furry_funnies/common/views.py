from django.shortcuts import render
from django.views.generic import TemplateView

from furry_funnies.author.models import Author
from furry_funnies.utils import get_author


# Create your views here.
class ShowHomePageView(TemplateView):
    template_name = 'common/index.html'
    model = Author
    author = get_author()