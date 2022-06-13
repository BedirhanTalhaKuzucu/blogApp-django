from multiprocessing import context
from pickle import FALSE
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CommentForm, NewPostForm, CategoryForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Category, Post, Comment, Like, PostView
from django.shortcuts import get_object_or_404, get_list_or_404


def post_list(request):
    posts = Post.objects.all()
    for post in posts:
        post.likecount = Like.objects.filter(Post= post.id).count()
        post.viewcount = PostView.objects.filter(post=post.id).count()
        post.commentcount = Comment.objects.filter(post_id = post.id).count()


    context= {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)


def new_post(request):
    formPost = NewPostForm()
    formCategory = CategoryForm()

    if request.method == 'POST':
        formPost = NewPostForm(request.POST, request.FILES)
        formCategory = CategoryForm(request.POST)

        if formPost.is_valid() and formCategory.is_valid():
            post =  formPost.save(commit=False)
            post.user = request.user
            post.save()
            category = formCategory.save( commit=False )
            category.post = post
            category.save()

            return redirect('home')
    
    context = {
        'formPost' : formPost,
        'formCategory': formCategory, 
    }

    return render (request, 'blog/post_create.html', context)

def postUpdate(request, id):
    post = Post.objects.get(id=id)
    postCategory = Category.objects.get(post=post)
    formPost = NewPostForm(instance=post)
    formCategory = CategoryForm(instance=postCategory)
    print(post.comment_count())
    print(post.comments())


    if request.method == "POST":
        formPost = NewPostForm(request.POST, request.FILES, instance= post)
        formCategory = CategoryForm(request.POST, instance=postCategory)

        if formPost.is_valid() and formCategory.is_valid():
            formPost.save()
            formCategory.save()
            return redirect('details', id=id)
    
    context={
        'formPost': formPost,
        'formCategory': formCategory,
    }

    return render (request, "blog/post_update.html", context)

def postDelete(request, id):
    post = Post.objects.get(id=id)

    if request.method == "POST":
        post.delete()
        return redirect('home')
    
    context={
        'post':post
    }
    return render (request, 'blog/post_delete.html', context)




def post_details(request, id):
    postDetails = Post.objects.get(id=id)
    commentForm = CommentForm()
    listComment = Comment.objects.filter(post_id = id)

    checkLike = False
    if request.user.is_authenticated:
        checkLike = Like.objects.filter(User=request.user, Post=postDetails )
    
    likeCount = Like.objects.filter(Post=postDetails)
    # print(likeCount)

    # checkView = PostView.objects.filter(user=request.user, post=postDetails)
    # if not PostView.objects.filter(user=request.user, post=postDetails).exists():
    #     viewList = PostView.objects.create(user=request.user, post=postDetails)
    #     viewList.save()
    # viewCount = PostView.objects.filter(post=postDetails)

    viewList = PostView.objects.create(post=postDetails)
    viewList.save()
    viewCount = PostView.objects.filter(post=postDetails)

    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comments = commentForm.save(commit=False)
            comments.user = request.user
            comments.post = postDetails
            comments.save()
            return redirect('details', id=id)

    context={
        'postDetails' : postDetails,
        'commentForm' : commentForm,
        'listComment' : listComment,
        'checkLike' : checkLike,
        'likeCount': likeCount,
        'viewCount' : viewCount,
    }
    return render (request, 'blog/post_details.html', context)


def addLike(request, id):
    post = Post.objects.get(id=id)
    checkLike = Like.objects.filter(User=request.user, Post=post)
    if not checkLike:
        likelist= Like.objects.create(User=request.user, Post=post )
        likelist.save()
    else:
        checkLike.delete()

    return redirect('details', id=id)





