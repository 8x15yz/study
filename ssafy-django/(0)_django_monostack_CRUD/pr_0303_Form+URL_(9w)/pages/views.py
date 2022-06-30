from django.shortcuts import render



def index(request):
    # Template Namespace : 템플릿 호출 시 이름
    # template 이름을 작성
    # => templates 폴더를 전부 찾음
    # => 찾는 순서 == 앱 등록된 순서
    # 같은 이름의 html 파일이 있으면 문제 발생
    # 해결 방법
    # => 폴더 중첩 구조 => 구조 형태로 작성
    # pages/
    #     templates/
    #         pages/
    #             index.html
    return render(request, 'pages/index.html')