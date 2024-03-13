from .models import Post, Comment
from django.shortcuts import get_object_or_404 , render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST


# Create your views here.
# def post_list(request):
#     post_list=Post.published.all()
#     paginator = Paginator(post_list, 3)
#     page_number = request.GET.get('page', 1)
#     try:
#         posts = paginator.page(page_number)

#     except PageNotAnInteger:
#         posts = paginator.page(1)
    
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)

#     return render(request, 'list.html', {'posts': posts})

"""alternative post list view"""

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'list.html'


def post_detail(request, years, month, day, post):
    post= get_object_or_404(Post, status=Post.Status.PUBLISHED, slug = post, publish__year = years, publish__month = month, publish__day = day)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request, 'details.html',{'post':post, 'comments':comments, 'form':form})

#creating a view for the post form\
def post_share(request, post_id):
    #retrievinng post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == "POST":
        form=EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recomends your read"  f"{post.title}"
            message= f"Read {post.title} at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'trickish@gmail.com', [cd['to']]) 
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'share.html', {'post':post, 'form': form, 'sent': sent})

#adding ModelForm in views
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form= CommentForm(data=request.POST)
    if form.is_valid():
        comment=form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'comment.html', {'post':post, 'form':form, 'comment':comment})