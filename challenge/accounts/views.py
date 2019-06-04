from django.contrib.auth.forms import UserCreationForm
from django.views import generic

class SignUp(generic.CreateView):
    form_class = UserCreationForm
