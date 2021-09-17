from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import *
from .forms import UserRegisterForm,PostForm,CommentForm
# Create your views here.

class HomeView(ListView):
    paginate_by = 3
    model = Post
    template_name = 'principal/feed.html'
    cats = Category.objects.all()
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

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

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'principal/category_list.html', {'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'principal/categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm 
    template_name = 'principal/add_category.html'
    fields = '__all__'
    #fields = '__all__'
    #fields = ('title', 'body')




