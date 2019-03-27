from django.shortcuts import render
from .forms import NewFieldForm
from basic_app.models import Field_Book
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def register(request):
    form = NewFieldForm()

    if request.method == "POST":
        form = NewFieldForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return success(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'basic_app/register.html',{'form':form})

def index(request):
    return render(request,'basic_app/index.html')

def contact(request):
    return render(request,'basic_app/contact.html')

def apeo_login(request):
    return render(request,'basic_app/apeo_login.html')

def details(request):
    return render(request,'basic_app/details.html')

def success(request):
    return render(request,'basic_app/success.html')

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                field_list = Field_Book.objects.all()
                field_dict = {'field_record':field_list}
                return render(request,"basic_app/special.html",field_dict)
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basic_app/apeo_login.html', {})


@login_required
def special(request):
    field_list = Field_Book.objects.all()
    field_dict = {'field_record':field_list}
    return render(request,'basic_app/special.html',field_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def field_entry(request):
    field_list = Field_Book.Objects
    field_dict = {'field_record':field_list}

def on_click(request):
    if request.method == "POST":
        decision = request.POST.get("on_click")
        status = request.POST.get("status")
        if decision == 'Accept':
            status = "Accepted"
        elif decision == "Reject":
            status = "Rejected"

        else:
            return render(request,'basic_app/special.html')
