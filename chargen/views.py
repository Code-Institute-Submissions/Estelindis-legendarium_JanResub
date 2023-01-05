from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.text import slugify
from django.urls import reverse,reverse_lazy
from .models import Story, Category
from .forms import CategoryForm, CommentForm


class StoryList(generic.ListView):
    model = Story
    queryset = Story.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class StoryDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Story.objects.filter(status=1)
        story = get_object_or_404(queryset, slug=slug)
        comments = story.comments.filter(approved=True).order_by("created_on")
        in_library = False
        if story.library.filter(id=self.request.user.id).exists():
            in_library = True

        return render(
            request,
            "story_detail.html",
            {
                "story": story,
                "comments": comments,
                "commented": False,
                "in_library": in_library,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Story.objects.filter(status=1)
        story = get_object_or_404(queryset, slug=slug)
        comments = story.comments.filter(approved=True).order_by("created_on")
        in_library = False
        if story.library.filter(id=self.request.user.id).exists():
            in_library = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.story = story
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "story_detail.html",
            {
                "story": story,
                "comments": comments,
                "commented": True,
                "in_library": in_library,
                "comment_form": CommentForm()
            },
        )


class LibraryAdd(View):

    def post(self, request, slug):
        story = get_object_or_404(Story, slug=slug)

        if story.library.filter(id=request.user.id).exists():
            story.library.remove(request.user)
        else:
            story.library.add(request.user)

        return HttpResponseRedirect(reverse('story_detail', args=[slug]))


# class CategoryView(View):

#     def get(self, request, id, *args, **kwargs):
#         categories = Category.objects.all()
#         category = get_object_or_404(categories, pk=id)
#         form = CategoryForm(instance=category)
#         template = 'add_category.html'
#         context = {
#             'form': form,
#             'categories': categories,
#             'id': id,
#         }
#         return render(request, template, context)

#     def post(self, request, *args, **kwargs):
#         form = CategoryForm(data=request.POST)
#         if form.is_valid():
#             form.instance.slug = slugify(form.instance.category_name)
#             category = form.save(commit=False)
#             category.save()
#             return HttpResponseRedirect(reverse('add_category'))
#         template = 'add_category.html'
#         context = {
#             'form': form,
#         }
#         return render(request, template, context)


class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "categories.html"


class CategoryEdit(generic.edit.UpdateView):
    model = Category
    fields = ('category_name', 'category_pic',)
    template_name_suffix = '_update'
    success_url = reverse_lazy('category_list')


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')


class CategoryCreate(CreateView):
    model = Category
    fields = ('category_name', 'category_pic',)
    template_name_suffix = '_create'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.category_name)

        return super().form_valid(form)

