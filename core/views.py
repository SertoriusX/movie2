from django.shortcuts import render,get_object_or_404,redirect
from .models import movie,Tag,lastmovie,Tag_s
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth import logout
from django.contrib import messages
from .form import RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Contact


# Create your views here.

def firstPage(reqest):
    return render(reqest,'core/frontpage-1.html')
def movieview(request):
    movies = movie.objects.all()
    tags = Tag.objects.all()
    lastmovies = lastmovie.objects.all()
    paginator = Paginator(lastmovies,2)
    page = request.GET.get('page')
    lastmovies = paginator.get_page(page)
    tagss = Tag_s.objects.all()
    return  render(request,'core/frontpage.html',{'movies':movies,'tags':tags,'lastmovies':lastmovies,'tagss':tagss})

def detailmovies(request,slug):
    movies = get_object_or_404(movie,slug=slug)
    return render(request,'core/movie-detail.html',{'movies':movies})

def detaillastmovies(request,slug):
    lastmovies = get_object_or_404(lastmovie,slug=slug)
    return render(request, 'core/movie-detail1.html',{'lastmovies':lastmovies})

def search(request):
    query = request.GET.get('query', '')

    posts = lastmovie.objects.filter(Q(name__icontains=query))

    return render(request, 'core/search.html', {'posts': posts, 'query': query})
def lastmovies(request):
    lastmovies = lastmovie.objects.all()
    paginator = Paginator(lastmovies,2)
    page = request.GET.get('page')
    lastmovies = paginator.get_page(page)
    return render(request,'core/Movie.html',{'lastmovies':lastmovies})

def singup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('movie')

    else:
        form = RegistrationForm()
    return render(request,'core/singup.html',{'form':form})

def login_old(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')

            return redirect('movie')
        else:
            messages.success(request, 'There was an error with your username or password')
            return redirect('login')
    else:
        return render(request, 'core/login.html',{})

def logout_old(request):
    logout(request)
    return redirect('/')

@login_required
def myaccounts(request):

    return render(request,'core/myaccount.html')




def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
    return render(request,'core/contact.html',)


