from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Story
from .forms import CommentForm


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
