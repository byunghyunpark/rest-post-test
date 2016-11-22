from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic.detail import SingleObjectMixin

from post.forms import CommentForm
from post.models import Post, Comment


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/photo_list.html'
    queryset = Post.objects.order_by('-created_date')


class PostCommentFormView(SingleObjectMixin, FormView):
    template_name = 'post/post_detail.html'
    form_class = CommentForm
    model = Post

    def form_valid(self, form):
        self.object = self.get_object()
        content = form.cleaned_data['content']
        Comment.objects.create(
            post=self.object,
            author=self.request.user,
            content=content,
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_view:post_detail', kwargs={'pk': self.object.pk})


class PostDisplay(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class PostDetail(View):
    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostCommentFormView.as_view()
        return view(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class PostAdd(CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('post_view:post_list')
    template_name = 'post/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
