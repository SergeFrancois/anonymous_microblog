from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import models

def show_posts_or_create_new(request):
    if request.method == "POST":
        post_form = models.PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, "index.html", { 'posts' : models.Post.objects.all().order_by('-id'),
                                               'post_form': models.PostForm() })