from django.shortcuts import render
from django.urls.base import set_urlconf
from django.views import generic
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .filters import PostFilter
from django.utils import timezone

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'blogs_list'

    def get_queryset(self):
        """Return all the blogs."""
        return Post.objects.all()

class SearchView(generic.ListView):
    template_name = 'blogs/search.html'
    context_object_name = 'blogs_list'

    def get_queryset(self):
        """Return all the blogs."""
        return Post.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

class CreateView(generic.edit.CreateView):
    template_name = 'blogs/create.html'
    model = Post
    fields = ['text', 'title', 'author']
    success_url = reverse_lazy('blogs:index')

class UpdateView(generic.edit.UpdateView):
    template_name = 'blogs/update.html'
    model = Post
    fields = ['text', 'title']
    success_url = reverse_lazy('blogs:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'blogs/delete.html' # override default of greetings/greeting_confirm_delete.html
    model = Post
    success_url = reverse_lazy('blogs:index')

# Filtered Pages
class FilterAuthorView(generic.ListView):
    template_name = 'blogs/filauthor.html'
    context_object_name = 'blogs_list'

    def get_queryset(self):
        """Return all the blogs."""
        me = User.objects.get(username=self.request.user)
        return Post.objects.filter(author=me)

class OrderDateView(generic.ListView):
    template_name = 'blogs/orddate.html'
    context_object_name = 'blogs_list'

    def get_queryset(self):
        """Return all the blogs."""
        return Post.objects.order_by('-published_date')


class TodayView(generic.ListView):
    template_name = 'blogs/today.html'
    context_object_name = 'blogs_list'

    def get_queryset(self):
        """Return all the blogs."""
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')