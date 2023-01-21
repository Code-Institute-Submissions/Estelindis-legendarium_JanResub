from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy
from .models import Story, Category
from .forms import CategoryForm, CommentForm


# class StoryAccessMixin(LoginRequiredMixin, UserPassesTestMixin):
#     model = Story

#     def test_func(self):
#         if self.request.user.is_superuser:
#             return True
#         if self.request.user == story.author:
#             return True

#     # def handle_no_permission(self):
#     #     return JsonResponse(
#     #         {'message': 'You may not rewrite this story'}
#     #     )


class AdminMixin(UserPassesTestMixin):
    """
    Via this mixin, view access is restricted to admins.
    This mixin is presented applied to the category views:
    CategoryCreate, CategoryDelete, CategoryEdit, & CategoryList.
    Non-admins thus cannot alter categories, even via direct link.
    """
    
    def test_func(self):
        return self.request.user.is_superuser


class StoryList(generic.ListView):
    model = Story
    queryset = Story.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class StoryEdit(generic.edit.UpdateView):
    model = Story
    fields = ('name', 'summary', 'story', 'notes', 'story_image', 'story_category', 'status')
    template_name_suffix = '_update'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            raise PermissionDenied

        return super().form_valid(form)


class StoryDelete(DeleteView):
    model = Story
    success_url = reverse_lazy('home')


class StoryCreate(LoginRequiredMixin, CreateView):
    """
    To access this template, a user must be logged in.
    Via a form, a user can add a story to the database.
    """
    model = Story
    fields = ('name', 'summary', 'story', 'notes', 'story_image', 'story_category', 'status')
    template_name_suffix = '_create'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name + "-" + form.instance.summary)
        form.instance.author = self.request.user

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


class CategoryList(AdminMixin, generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "categories.html"


class CategoryEdit(AdminMixin, generic.edit.UpdateView):
    """
    To access this template, a user must be logged in.
    Via a form, a superuser can edit an existing category.
    """
    model = Category
    fields = ('category_name', 'category_pic',)
    template_name_suffix = '_update'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            raise PermissionDenied

        return super().form_valid(form)


class CategoryDelete(AdminMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')


class CategoryCreate(AdminMixin, CreateView):
    """
    To access this template, a user must be logged in.
    Via a form, a superuser can add a category to the database.
    """
    model = Category
    fields = ('category_name', 'category_pic',)
    template_name_suffix = '_create'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.category_name)
        if not self.request.user.is_superuser:
            raise PermissionDenied

        return super().form_valid(form)

