from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import widgets
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class bangdingForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(bangdingForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = widgets.TextInput(
            attrs={'placeholder': "username", "class": "form-control"})
