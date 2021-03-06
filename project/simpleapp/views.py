from datetime import datetime

from django.views.generic import \
    ListView, \
    DetailView
from .models import Post


class ProductsList(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context[
            'value1'] = None
        return context


class ProductDetail(DetailView):
    model = Post
    template_name = 'post1.html'
    context_object_name = 'post1'






