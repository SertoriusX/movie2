from django.urls import path
from .views import movieview,detailmovies,detaillastmovies,search,lastmovies,singup,login_old,firstPage,logout_old,myaccounts,contact
from django.contrib.auth import views

urlpatterns = [
    path('',firstPage),
    path('movie/', movieview, name='movie'),
    path('detail-1/<slug:slug>/', detailmovies, name='detail-1'),
    path('detail-2/<slug:slug>/',detaillastmovies, name='detail-2'),
    path('search/', search, name='search'),
    path('movies/',lastmovies, name='movies'),
    path('singup/', singup, name='singup'),
    path('logout/', logout_old, name='logout'),

    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('login/',login_old,name='logins'),
    path('myaccounts/', myaccounts,name='myaccounts'),
    path('contact/', contact, name='contact')
]