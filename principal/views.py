from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import *
from .forms import UserRegisterForm,PostForm,CommentForm
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'principal/feed.html'

class PostDetailView(DetailView):
    model=Post
    
    template_name='principal/post_detail.html'

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        form = UserRegisterForm()

    context = { 'form' : form}
    return render(request, 'principal/register.html',context)

def profile(request):
    return render(request, 'principal/profile.html')

class AddPost(CreateView):
    model=Post
    form_class=PostForm
    template_name='principal/crear.html'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'principal/actualizar.html'
    fields = ['title','content']

class DeletePostView(DeleteView):
    model = Post
    template_name='principal/post_delete.html'
    success_url = reverse_lazy('home')

class AddCommentView(CreateView):
    model=Comentario
    form_class=CommentForm
    template_name='principal/add_comment.html'
    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')



