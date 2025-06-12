from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from furry_funnies.author.models import Author
from furry_funnies.posts.models import Post

from furry_funnies.utils import get_author


# Create your views here.
class ShowHomePageView(TemplateView):
    template_name = 'common/index.html'



def dashboard_page_view(request):
    posts = Post.objects.all()
    author = get_author()

    context = {
        'posts': posts,
        'author': author
    }

    return render(request, 'common/dashboard.html', context=context)



