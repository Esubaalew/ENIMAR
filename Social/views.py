from django.shortcuts import render
from .models import Post, Comment
from django.shortcuts import get_object_or_404


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'social/post/detail.html', {'post': post})
