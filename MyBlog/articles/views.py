from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView

from MyBlog.articles.forms import AddPostForm
from MyBlog.articles.models import Article


UserModel = get_user_model()


class DetailsPostView(DetailView):
    template_name = 'articles/details-post-page.html'
    model = Article


class AddPostView(CreateView):
    template_name = 'articles/add-post-page.html'
    model = Article
    form_class = AddPostForm

    success_url = reverse_lazy('index')


# TODO to see code below how to rewrite get and post in CBV:
# class FileUploadView(View):
#     form_class = MyForm
#     success_url = reverse_lazy('home')
#     template_name = 'file_upload.html'
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(self.success_url)
#         else:
#             return render(request, self.template_name, {'form': form})


class EditPostView(UpdateView):
    template_name = 'articles/edit-post-page.html'
    model = Article
    fields = ('category', 'title', 'body', 'post_image')

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
