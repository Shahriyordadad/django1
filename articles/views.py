from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'
    
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title','summary','body','photo',)
    template_name = 'article_edit.html'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self .request.user
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    def get_success_url(self):
        return reverse_lazy("article_list")
    def test_func(self):
        obj = self.get_object()
        return obj.author == self .request.user
        
class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title','summary','body','photo',)
    
    def form_valid(self, form):
        form.instance.author = self.requests.user
        return super().form_valid(form)
        
    def test_func(self):
       return self.request.user.is_superuser