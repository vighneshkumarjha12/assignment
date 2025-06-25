from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.filter(status='published')
    return render(request, 'blog_app/blog_list.html', {'posts': posts})


def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comments.all().order_by('-timestamp')
    like_count = post.likes.count()
    return render(request, 'blog_app/blog_detail.html', {
        'post': post,
        'comments': comments,
        'like_count': like_count
    })


