from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from app.models import Testing, NewsApi
from newsapi import NewsApiClient
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator



newsapi = NewsApiClient(api_key='9399cb5d33a841cf9932cf56e214fa67')
top_headlines = newsapi.get_top_headlines(language='en', country='us')


# def test(request):
#     return render(request, "templates/index.html")
#     # current_user = request.user
#     # return HttpResponse("<center><h1>Hi How are you; {{ request.user }}</h1></center>")
#     # return HttpResponse("<center><h1>Hi How are you; {{ request.user.username }}</h1></center>")
#     # return HttpResponse(id+"Hi Id")
#     # return HttpResponse("<center><h1>Hi How are you; {{ request.user.username() }}</h1></center>")

# Extra test For debut errors
def test(request):
    return HttpResponse("<center><h2 style='margin-top: 60px;'>This is A Homepage...</h2></center>")

# import os
# def test2(request):
#     # View code here...
#     t = loader.get_template('index.html')
#     ls = os.environ.get()
#     c = {"user":ls}
#     return HttpResponse(t.render(c, request))



# def test3(request, id):
#     return HttpResponse(f'<center><h1>{id}</h1></center>')


# def test4(request, id):
#     return HttpResponse(f'<center><h1>{id}</h1></center>')


# def test5(request, id):
#     return HttpResponse(f'<center><h1>{id}</h1></center>')


# def test6(request, id):
#     return HttpResponse(f'<center><h1>{id}</h1></center>')


# def test7(request, id):
#     return HttpResponse(f'<center><h1>{id}</h1></center>')


# def test8(request):
#     return HttpResponse(f'<center><h1>{request}</h1></center>')



# import base64
# def test9(request):
#     auth_header = request.META['HTTP_AUTHORIZATION']
#     encoded_credentials = auth_header.split(' ')[1]  # Removes "Basic " to isolate credentials
#     decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8").split(':')
#     username = decoded_credentials[0]
#     password = decoded_credentials[1]
#     return HttpResponse(f"<center><h1>{username, password}</h1><center>")



# def test10(request, username):
#     return HttpResponse(f'<center><h1>{username}</h1></center>')



# def test11(request):
#     headers = request.META["USERNAME"]
#     return HttpResponse(f'<center><h1>{str(headers)}</h1></center>')



# def test12(request):
#     print(request.headers)
#     return HttpResponse("Nothing")




# def test13(request):
#     data = {
#         "php": "backend language",
#         "python": "best language",
#         "django": "Python library/framework",
#         "plist": ["php", "python", "django"],
#         "user_list": [
#             {"name":"HackerZ", "age": "17"},
#             {"name":"HackerZ X", "age": "18"}
#         ]
#     }
#     return render(request, "index.html", data)



# def test14(request):
#     return render(request, "index.html")



# def test15(request):
#     return render(request, "index.html")



# def test16(request):
#     return redirect('/test15/')



# def test17(request):
#     return HttpResponse('<kbd>Ctrl</kbd><kbd>+</kbd>')



# def test18(request):
#     finalans = 0
#     try:
#         if request.method == "POST":
#             n1 = int(request.POST.get('num1'))
#             n2 = int(request.POST.get('num2'))
#             finalans = n1 + n2
#     except:
#         pass
#     return render(request, "forms.html", {"output": finalans})



# from .forms import UserForm
# def test19(request):
#     finalans = 0
#     fr = UserForm()
#     try:
#         if request.method == "POST":
#             n1 = int(request.POST.get('num1'))
#             n2 = int(request.POST.get('num2'))
#             finalans = n1 + n2
#     except:
#         pass
#     return render(request, "forms.html", {"output": finalans, "fr":fr})
    


# from .forms import UserForm
# def test20(request):
#     finalans = 0
#     fr = UserForm()
#     try:
#         if request.method == "POST":
#             n1 = eval(request.POST.get('num1'))
#             n2 = eval(request.POST.get('num2'))
#             n3 = request.POST.get('opt')
#             if n3 == 'add':
#                 finalans = n1 + n2
#             elif n3 == 'sub':
#                 finalans = n1 - n2
#             elif n3 == 'mul':
#                 finalans = n1 * n2
#             elif n3 == 'div':
#                 finalans = n1 / n2
#             else:
#                 finalans = 0
#     except:
#         pass
#     data = {"output": finalans, "fr":fr}
#     return render(request, "forms.html", data)




# B = Testing(Name='Name6')
# B.save()


def RegisterTesting(Name, Title, Desc, request):
    checkName = Testing.objects.filter(Name=Name).exists()
    checkTitle = Testing.objects.filter(Title=Title).exists()
    checkDesc = Testing.objects.filter(Desc=Desc).exists()
    
    if checkName:
        messages.info(request, "Name Is Already In Database")
    elif checkTitle:
        messages.info(request, "Title Is Already In Database")
    elif checkDesc:
        messages.info(request, "Desc Is Already In Database")
    else:
        B = Testing(User=request.user.username, Name=Name, Title=Title, Desc=Desc)
        B.save()


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pass1 = request.POST.get('pass1')
        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
            auth_login(request, user)
            user.last_login
            user.save()
            messages.success(request, 'Login Successfully')
            return redirect('test21')
    
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    messages.warning(request, 'Logout SuccessFully')
    return redirect('test21')
    
        

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        try:
            if pass1 == pass2 and User.objects.filter(username=uname).exists() is not True:
                u = User.objects.create_user(username = uname, email = email, password = pass1)
                u.first_name = fname
                u.lastname = lname
                u.save()
                return redirect('test21')
            if User.objects.filter(username=uname).exists():
                messages.warning(request, 'Username Already Taken')
            if User.objects.filter(email=email).exists():
                messages.warning(request, mark_safe('This Email Is Already Registered Please <a href=\'/login/\' class=\'btn btn-outline-info btn-sm\'> Login</a>'))
            if pass1 is not pass2:
                messages.warning(request, 'Password Not Matched')
        
        except Exception as e:
            messages.success(request, e)


    return render(request, 'register.html')




def search(request):
    

    if request.method == 'GET':
        searchVal = request.GET.get('search')
        if searchVal:
            if request.user.is_authenticated:
                servicePageMain = Testing.objects.filter(User=request.user.username).all()
                servicePageN = Testing.objects.filter(User=request.user.username, Name__icontains=searchVal).exists()
                servicePageT = Testing.objects.filter(User=request.user.username, Title__icontains=searchVal).exists()
                servicePageD = Testing.objects.filter(User=request.user.username, Desc__icontains=searchVal).exists()
                if servicePageN:
                    servicePageMain = Testing.objects.filter(User=request.user.username, Name__icontains=searchVal).all()
                elif servicePageT:
                    servicePageMain = Testing.objects.filter(User=request.user.username, Title__icontains=searchVal).all()
                elif servicePageD:
                    servicePageMain = Testing.objects.filter(User=request.user.username, Desc__icontains=searchVal).all()
                else:
                    servicePageMain = ''
            
            else:
                servicePageMain = Testing.objects.filter(User='other').all()
                servicePageEN = Testing.objects.filter(User='other', Name__icontains=searchVal).exists()
                servicePageET = Testing.objects.filter(User='other', Title__icontains=searchVal).exists()
                servicePageED = Testing.objects.filter(User='other', Desc__icontains=searchVal).exists()
                if servicePageEN:
                    servicePageMain = Testing.objects.filter(User='other', Name__icontains=searchVal).all()
                elif servicePageET:
                    servicePageMain = Testing.objects.filter(User='other', Title__icontains=searchVal).all()
                elif servicePageED:
                    servicePageMain = Testing.objects.filter(User='other', Desc__icontains=searchVal).all()
                else:
                    servicePageMain = ''
                
    boolT = True
    data = {
        'tD': servicePageMain,
        'boolT': boolT
    }
    return render(request, 'search.html', data)



def test21(request):
    NewsApi.objects.all().delete()

    varTest = len(top_headlines['articles'])
    for i in range(varTest):
        news_title = top_headlines['articles'][i]['title']
        news_image = top_headlines['articles'][i]['urlToImage']
        news_author = top_headlines['articles'][i]['author']
        news_desc= top_headlines['articles'][i]['description']
        if news_author == None:
            news_author = ''
        if news_title == None:
             news_title = ''
        if news_desc == None:
            news_desc = ''
        if news_image == None:
            news_image = ''

        bTag = NewsApi(News_title=news_title, News_author=news_author, News_desc=news_desc, News_image=news_image)
        bTag.save()


    if request.user.is_authenticated:
        servicePage = Testing.objects.filter(User=request.user.username).all()
    else:
        servicePage = Testing.objects.filter(User='other').all()
    newsData = NewsApi.objects.all().order_by('News_title')


    if request.method == 'POST':
        if request.user.is_authenticated:
            Name = request.POST['name']
            Title = request.POST['title']
            Desc = request.POST['desc']
            RegisterTesting(Name, Title, Desc, request)
        else:
            messages.info(request, mark_safe("<a href=\"/login/\" class=\"btn btn-outline-dark\">Login</a>"))
    
    
    pageNum = request.GET.get('page')
    if request.user.is_authenticated:
        pageVar = Testing.objects.filter(User=request.user.username).all()
    else:
        pageVar = Testing.objects.filter(User='other').all()
    page = Paginator(pageVar, 2)
    servicePage = page.get_page(pageNum)
    totalPage = servicePage.paginator.num_pages
    

    boolT = True
    data = {
        "tD": servicePage,
        'nD': newsData,
        'boolT': boolT,
        'tP': [n+1 for n in range(totalPage)],
        'lastpage': totalPage
        }
    
    return render(request, "models.html", data)


def delete(request, delete_id):
    deleteID = Testing.objects.get(id=delete_id)
    deleteID.delete()
    return redirect('test21')


def edit(request, edit_id):
    if request.method == 'POST':
        editID = Testing.objects.get(id=edit_id)
        editID.Name = request.POST['name']
        editID.Title = request.POST['title']
        editID.Desc = request.POST['desc']
        editID.save()
        return redirect('test21')
    else:
        editID2 = Testing.objects.filter(id=edit_id).first()
        data = {
            'editID': editID2
        }
        return render(request, "edit.html", data)


def news(request, slug): 
    newsID = NewsApi.objects.get(News_slug=slug)
    news_data = {
        'nD': newsID
    }
    return render(request, 'news.html', news_data)
