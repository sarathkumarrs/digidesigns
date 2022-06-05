from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from users.form_utils import FormUtils
from users.forms import SignupForm
from users.functions import get_customer
from users.models import Customer


def sign_up(request):
    """
    signup function
    :param request:
    :return:
    """
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        form_utils = FormUtils(form, Customer, request=request)
        response = form_utils.save_user()
        return redirect(reverse('users:dashboard'))
    else:
        context = {
            "form": form,
        }
        return render(request, 'users/register.html', context=context)


@login_required()
def dashboard(request):
    """
    home dashboard view
    :param request:
    :return:
    """
    return render(request, 'users/index.html', context={})


@login_required()
def profile(request):
    """
    :param request:
    :return:
    """
    user_instance = get_customer(request.user)
    context = {
        "instance": user_instance,
    }
    return render(request, 'users/profile.html', context=context)
