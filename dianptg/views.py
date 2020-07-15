from django.shortcuts import render
from .forms import RegisterForm, LoginForm

# Create your views here.
def post_list(request):
    return render(request, "post_list.html", {})

def bangdingview(FormView):
    form_class = RegisterForm
    template_name = 'dianptg/paimaipin.html'