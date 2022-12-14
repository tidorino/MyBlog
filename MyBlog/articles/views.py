from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView

from MyBlog.accounts.models import Profile
from MyBlog.articles.forms import AddPostForm
from MyBlog.articles.models import Article


UserModel = get_user_model()


class DetailsPostView(DetailView):
    template_name = 'articles/details-post-page.html'
    model = Article


class AddPostView(CreateView):

    template_name = 'articles/add-post-page.html'
    model = Article
    # fields = ('category', 'title', 'slug', 'body', 'image_url')
    form_class = AddPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['user'] = self.object.author == self.request.user

        return context

    success_url = reverse_lazy('index')
# # @login_required
# def add_post(request):
#
#     if request.method == 'GET':
#         form = AddPostForm()
#     else:
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             article = form.save(commit=False)
#             article.user = request.user
#             article.save()
#             return redirect('index')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'articles/add-post-page.html', context)


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
