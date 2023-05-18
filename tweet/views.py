# tweet/views.py
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    user = request.user.is_authenticated  # 사용자가 인증을 받았는지 (로그인이 되어있는지)
    if user:
        return redirect('/tweet')
    else:
        return redirect('/user/sign-in')


def tweet(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'tweet/home.html')
        else:
            return redirect('/user/log-in')
