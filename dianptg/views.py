from django.shortcuts import render
from django.views.generic import FormView, RedirectView
from .forms import bangdingForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib import auth

# Create your views here.
def post_list(request):
    return render(request, "post_list.html", {})

class bangdingview(FormView):
    form_class = bangdingForm
    template_name = 'dianptg/post_list.html'
    # template_name = 'dianptg/paimaipin.html'
