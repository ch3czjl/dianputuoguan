from django.shortcuts import render
from django.views.generic import FormView, RedirectView
from .forms import bangdingForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib import auth
# from dianptg.accounts import BlogUser

# Create your views here.
def post_list(request):
    return render(request, "post_list.html", {})

class bangdingview(FormView):
    form_class = bangdingForm
    template_name = 'dianptg/post_list.html'
    # template_name = 'dianptg/paimaipin.html'

def adddianpudatebase(request):
    id_dianpu = dianpuid
    print(id_dianpu)
    return HttpResponseRedirect('/bangdinghou/')

def bangdinghou(request):
    # print(request.POST.get('bangding'))
    return render(request,'bangdinghou.html')
    # return render(request,"bangdinghou.html",{})