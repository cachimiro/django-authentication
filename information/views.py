from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

# Create your views here.
def info(request):
     Post = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
     return render(request, "info.html", {'posts': posts})

def info_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "infodetail.html", {'post': post})


def create_or_edit_info(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(info_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'infopostform.html', {'form': form})
