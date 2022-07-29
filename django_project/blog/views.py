from django.shortcuts import render

posts = [
    {
        'author': 'Louis',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 29th 2022'
    },
    {
        'author': 'Yoda',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 30th 2022'

    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
