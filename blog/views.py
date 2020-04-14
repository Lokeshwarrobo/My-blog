from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,DetailView
from django.views.generic.edit import UpdateView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'blog'
    ordering = ['-date']
    paginate_by = 3

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'entries/signup.html'
    success_url = reverse_lazy('login')
class Baseview(ListView):
    model = Post
    template_name='entries/index.html'
class PostDetailView(DetailView):
    model = Post
    template_name = 'entries/detail.html'
    context_object_name = 'blog'
class PostCreateView(CreateView):
    model = Post
    template_name = 'entries/newpost.html'
    fields = ['title','text']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    model = Post
    template_name = 'entries/post_delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('home')
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'entries/post_edit.html'
    fields = ['title','text']
    success_url = reverse_lazy('home')

def lok(request):
    return render(request,'entries/nav.html')