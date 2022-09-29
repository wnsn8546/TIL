from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    # 1. DB에서 모든 글을 불러온다.
    posts = Post.objects.all()
    # 2. template 에 보내준다.
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def new(request):
    return render(request, "posts/new.html")


def create(request):
    # 1. paramtet로 날라온 데이터를 받아서
    title = request.GET.get("title")
    content = request.GET.get("content")

    # 2. DB에 저장
    Post.objects.create(title=title, content=content)

    context = {
        "title": title,
        "content": content,
    }

    # return render(request, "posts/create.html", context)
    return redirect("posts:index")


def update_form(request, pk):
    # pk에 해당하는 글 수정 화면 렌더
    post = Post.objects.get(id=pk)
    # title = request.GET.get("title")
    # content = request.GET.get("content")

    context = {
        "id": post.id,
        "title": post.title,
        "content": post.content,
    }
    return render(request, "posts/update-form.html", context)


# def update(request, pk):
#     # pk에 해당하는 글 수정
#     post = Post.objects.get(id=pk)
#     post.title = request.GET.get("title")
#     post.content = request.GET.get("content")
#     post.save()
#     return redirect("posts:detail")


def update(request, pk):
    # pk에 해당하는 글 수정
    post = Post.objects.get(id=pk)
    post.title = request.GET.get("title")
    post.content = request.GET.get("content")
    post.save()
    return redirect("posts:detail", pk)


def delete(request, pk):
    # pk에 해당하는 글 삭제
    Post.objects.get(id=pk).delete()

    return redirect("posts:index")


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, "posts/detail.html", context)


def edit(request, pk):
    post = Post.objects.get(id=pk)

    context = {
        "post": post,
    }
    return render(request, "posts/edit.html", context)
