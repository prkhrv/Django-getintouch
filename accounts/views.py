from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib import messages

from .decorators import check_recaptcha

# model and form
from .forms import getintouchForm
from .models import getintouch
# from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'index.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@check_recaptcha
def getintouchview(request):
    form = getintouchForm()
    if request.method == 'POST':
        form = getintouchForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            form.save()
            messages.success(request, 'Your Query is Received')
            return redirect('home')
    return render(request,'form.html',{'form':form,})
