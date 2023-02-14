from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView

from MyBlog.accounts.models import Profile
from MyBlog.articles.forms import AddPostForm
from MyBlog.articles.models import Article


UserModel = get_user_model()


class DetailsPostView(DetailView):
    template_name = 'articles/details-post-page.html'
    model = Article


# def add_post(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             new_post = form.save(commit=False)
#             author = Profile.objects.get(articles=request.user.id)
#             new_post.author = request.user = author
#             new_post.save()
#             return redirect('index')
#     else:
#         form = AddPostForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/add-post-page.html', context)
# class AddPostView(CreateView):
#
#     template_name = 'articles/add-post-page.html'
#     model = Article
#     # fields = ('category', 'title', 'slug', 'body', 'image_url')
#     form_class = AddPostForm
#
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         login(request, self.object)
#
#         return response
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['article_auther'] = self.object == self.request.user
#
#         return context
#
#     success_url = reverse_lazy('index')
@login_required
def add_post(request):

    if request.method == 'GET':
        form = AddPostForm()
    else:
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            author = Profile.objects.filter(user=request.user).get()
            Article.author = author

            article.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'articles/add-post-page.html', context)


class EditPostView(UpdateView):
    template_name = 'articles/edit-post-page.html'
    model = Article
    fields = ('category', 'title', 'body', 'image_url')

    def get_success_url(self):
        return reverse_lazy(
            'details post',
            kwargs={
                'slug': self.kwargs.get('slug')
            }
        )


class DeletePostView(DeleteView):
    template_name = 'articles/delete-post-page.html'
    model = Article
    success_url = reverse_lazy('index')


# def published_article(self):
#     return self.category.filter(status=True)
