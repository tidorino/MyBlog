from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView

from MyBlog.articles.models import Article


class DetailsPostView(DetailView):
    template_name = 'articles/details-post-page.html'
    model = Article


class AddPostView(CreateView):

    # TODO:
    #
    # 1.    http: // 127.0    .0    .1: 8000 / articles / add / -
    # to    change    'author' -
    # to    show    'full name'    of    user,
    # not 'email'

    template_name = 'articles/add-post-page.html'
    model = Article
    fields = '__all__'

    success_url = reverse_lazy('index')


class EditPostView(UpdateView):
    template_name = 'articles/edit-post-page.html'
    model = Article
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy(
            'details post',
            kwargs={
                'slug': self.kwargs.get('slug')
            }
        )


class DeletePostView(DeleteView):
    pass

