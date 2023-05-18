from django.shortcuts import render
from django.contrib.auth import get_user_model #사용자가 있는지 검사하는 함수



def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html') # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/user/sign-in') # 회원가입이 완료되었으므로 로그인 페이지로 이동
# 회원 가입시, 이미 존재하는 유저이다 > 회원 가입 할 필요 없음
# 이미 존하는 유저가 아니다 > 회원 가입 시켜야함
# user/views.py

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)  # 사용자 불러오기
        if me is not None:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            auth.login(request, me)
            return HttpResponse("로그인 성공")
        else:
            return redirect('/user/sign-in')  # 로그인 실패
    elif request.method == 'GET':
        return render(request, 'user/signin.html')
