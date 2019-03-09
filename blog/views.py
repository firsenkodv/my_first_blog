from django.shortcuts import render
from django.utils import timezone
from . models import Post

def post_list(request):
    posts = Post.objects.all()
    return render (request, 'blog/main.html', {'posts': posts})

def main(request):
    return render(request, 'blog/main.html',{})
def news(request):
    return render (request, "blog/news.html")

from django.utils import timezone

from django.core.mail import send_mail
from .forms import SendingForm
def send(request):
    if (request.method == 'POST'):
        form = SendingForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            send_mail(
                '{} {}'.format(name, email),
                'test meassage',
                'firsenkodv@gmail.com',
                ['firsenkodv@gmail.com', email],
                fail_silently=False,
            )
            return render(request, 'blog/result.html', {
                     'name': form.cleaned_data['name'],
               'email': form.cleaned_data['email'],
        })
    else:
        form = SendingForm()
    return render(request, 'blog/send.html', {'form':form});

# Create your views here.
