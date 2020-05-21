from django.shortcuts import render, reverse
from ghostpost.models import Post
from ghostpost.forms import add_post_forms
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone


# Create your views here.
def index_view(request):
    posts = Post.objects.all().order_by('-submit_time')
    return render(request, 'main_page.html', {'posts': posts})


def add_post_view(request):
    if request.method == 'POST':
        form = add_post_forms(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            Post.objects.create(
                post_type=data['post_type'],
                message=data['message'],
            )

            return HttpResponseRedirect(reverse('home'))
        else:
            print(add_post_forms.errors)
    form = add_post_forms()
    return render(request, 'postadd.html', {'form': form})


def upvotes(request, id):
    vote = Post.objects.get(id=id)
    vote.upvotes += 1
    vote.save()
    return HttpResponseRedirect(reverse('home'))


def downvotes(request, id):
    vote = Post.objects.get(id=id)
    vote.downvotes += 1
    vote.save()
    return HttpResponseRedirect(reverse('home'))


def viewup(request):
    up = Post.objects.all().order_by('-upvotes')
    return render(request, 'main_page.html', {'up': up})


def viewdown(request):
    down = Post.objects.values().order_by('-downvotes')
    return render(request, 'main_page.html', {'down': down})


def roast(request):
    roast = Post.objects.filter(post_type=False).order_by('-date')
    return render(request, 'main_page.html', {'roast': roast})


def boast(request):
    boast = Post.objects.filter(post_type=True).order_by('-date')
    return render(request, 'main_page.html', {'boast': boast})
