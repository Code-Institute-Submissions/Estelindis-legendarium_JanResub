from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy
from .models import Story, Category
from .forms import CategoryForm, CommentForm


class LibraryList(generic.ListView):
    model = Story
    
    def get_user_library(self, request):
        username = self.request.user
        stories_in_lib = username.story_library.all()
        return stories_in_lib

    template_name = "library.html"


# class LibraryView(CreateView):

#     def get(self, request, *args, **kwargs):
#         user_lib = Story.objects.filter(story_library=request.user)
#         return render(
#             request, 'library.html', {
#                 'user_lib': user_lib,
#             })


# class StoryLibrary(View):

#     def get(self, request, *args, **kwargs):
#         user_stories_in_lib = self.request.user.story_library.all()
#         return render(
#             request,
#             "library.html",
#             {
#                 "user_stories_in_lib": user_stories_in_lib,
#             },
#         )

#     def post(self, request, *args, **kwargs):
#          user_stories_in_lib = self.request.user.story_library.all()
#          return render(
#             request,
#             "library.html",
#             {
#                 "user_stories_in_lib": user_stories_in_lib,
#             },
#         )


class StoryList(generic.ListView):
    model = Story
    queryset = Story.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class StoryCreate(CreateView):
    model = Story
    fields = ('name', 'summary', 'story', 'notes', 'story_image', 'story_category', 'status')
    template_name_suffix = '_create'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name + "-" + form.instance.summary)
        form.instance.author = self.request.user
        # if not self.request.user.is_superuser:
        #     raise PermissionDenied

        return super().form_valid(form)


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

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            raise PermissionDenied

        return super().form_valid(form)


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')

    # def form_valid(self, form):
    #     if not self.request.user.is_superuser:
    #         raise PermissionDenied

    #     return super().form_valid(form)


class CategoryCreate(CreateView):
    model = Category
    fields = ('category_name', 'category_pic',)
    template_name_suffix = '_create'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.category_name)
        if not self.request.user.is_superuser:
            raise PermissionDenied

        return super().form_valid(form)

