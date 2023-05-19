from django.shortcuts import render, redirect
from .models import TweetModel # 글쓰기 모델 -> 가장 윗부분에 적어주세요!


# Create your views here.
def home(request):
    user = request.user.is_authenticated  # 사용자가 인증을 받았는지 (로그인이 되어있는지)
    if user:
        return redirect('tweet')
    else:
        return redirect('sign-in')


def tweet(request):
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면3
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html', {'tweet': all_tweet})
        else:  # 로그인이 되어 있지 않다면
            return redirect('sign-in')
    elif request.method == 'POST':  # 요청 방식이 POST 일때
        user = request.user  # 현재 로그인 한 사용자를 불러오기
        my_tweet = TweetModel()  # 글쓰기 모델 가져오기
        my_tweet.author = user  # 모델에 사용자 저장
        my_tweet.content = request.POST.get('my-content','')  # 모델에 글 저장
        my_tweet.save()
        return redirect('tweet')

def delete_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('tweet')
