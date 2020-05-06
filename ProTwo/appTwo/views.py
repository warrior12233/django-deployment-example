from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import Topic,Webpage,AccessRecord,User
from appTwo.forms import User_form
# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    dict = {'insert_me': "Now I am coming from first_app/index.html!"}
    return render(request,'appTwo/index.html',context=date_dict)

def help(request):
    dict = {'welcome':'This is the help page from django'}
    return render(request,'appTwo/help_page.html',dict)

def users(request):
    user_list = User.objects.order_by('last_name')
    form = User_form()
    if request.method == 'POST':
        form = User_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('form invalid')
    user_dict = {'users':user_list,'form':form}
    return render(request,'appTwo/users.html',user_dict)