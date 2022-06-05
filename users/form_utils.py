from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse

from users.functions import get_form_field, create_user


class FormUtils:
    def __init__(self, form, model, request=None):
        self.form = form
        self.model = model
        self.request = request

    def save_user(self):
        """
        form creation
        """
        if self.form.is_valid():
            email = get_form_field(self.form, 'email')
            password = get_form_field(self.form, 'password')
            user = create_user(email, password)
            data = self.form.save(commit=False)
            data.user = user
            data.save()
            user = authenticate(username=email, password=password)
            if user:
                login(self.request, user)
            return redirect(reverse('users:dashboard'))

        else:
            return {"status": False, "message": self.form.errors}

    def save_form_datas(self, **kwargs):
        print("On saving")
        if self.form.is_valid():
            print("From vaild")
            data = self.form.save(commit=False)
            # in case of kwargs
            data.creator = self.request.user
            data.save()
            return {"status": True, "message": "Created"}
        else:
            return {"status": False, "message": self.form.errors}

    @staticmethod
    def delete_data(id, model):
        obj = model.objects.get(id=id)
        obj.delete()
        return True
