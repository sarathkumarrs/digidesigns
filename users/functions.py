from django.contrib.auth.models import User

from users.models import Customer


def create_user(username, password):
    user = User.objects.create_user(
        username=username,
        password=password,
        is_active=True
    )
    return user


def get_form_field(form, field):
    return form.cleaned_data[field]


def get_customer(user):
    return Customer.objects.get(user=user)
