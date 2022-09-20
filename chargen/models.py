from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_pic = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.category_name


class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    summary = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="char_posts"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    story = models.TextField(blank=False)
    notes = models.TextField(blank=True)
    character_image = CloudinaryField('image', default='placeholder')
    post_category = models.ForeignKey(
        Category, on_delete=models.PROTECT,
        related_name='post_category',
        null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    library = models.ManyToManyField(
        User, related_name='story_library', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name

    def number_of_libraries(self):
        return self.library.count()


class Comment(models.Model):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE,
        related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
