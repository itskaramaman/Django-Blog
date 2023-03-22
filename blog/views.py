from django.shortcuts import render

posts = [
    {
        id: 1,
        'title': 'POST 1',
        'author': 'Corey MS',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2018'
    },
    {
        id: 2,
        'title': 'POST 2',
        'author': 'Khushwant Singh',
        'content': 'Khalistan and its Motives',
        'date_posted': 'June 6, 1984'
    },
    {
        id: 3,
        'title': 'POST 3',
        'author': 'Bhai Harjinder Singh Ji',
        'content': 'Prabh Dori Hath Tumhare',
        'date_posted': 'August 27, 1700'
    }
]

def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def user(request, name):
    return render(request, 'blog/user.html', {'name': name})