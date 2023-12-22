from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import PhotoGallery


def news_view(request):
    all_posts = Post.objects.all().order_by('-created_at')
    posts_per_page = 5
    paginator = Paginator(all_posts, posts_per_page)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    recent_posts = Post.objects.order_by('-created_at')[:5]
    gallerys = PhotoGallery.objects.all()

    return render(request, 'news_app/news.html', {'posts': posts, 'recent_posts': recent_posts, 'gallerys': gallerys})



def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()  # Retrieve all comments related to the post

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'news_app/post_detail.html', {'post': post, 'comments': comments, 'form': form})


def gallery_detail_view(request):
    gallerys = PhotoGallery.objects.all()
    return render(request, 'news_app/gallery_detail.html', {'gallerys': gallerys})



   


