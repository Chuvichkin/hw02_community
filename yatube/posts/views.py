from django.shortcuts import render, get_object_or_404
from .models import Post, Group
num_of_posts = 10


def index(request):
    text = 'Последние обновления на сайте'
    posts = Post.objects.all()[:num_of_posts]
    context = {'posts': posts, 'text': text}
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:num_of_posts]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
