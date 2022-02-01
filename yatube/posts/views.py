from django.shortcuts import render, get_object_or_404
from .models import Post, Group
NUM_OF_POSTS = 10


def index(request):
    text = 'Последние обновления на сайте'
    posts = Post.objects.all()[:NUM_OF_POSTS]
    context = {'posts': posts, 'text': text}
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:NUM_OF_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
