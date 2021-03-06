from django.shortcuts import render, redirect
from accounts.forms import UserAdminCreationForm


def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    return render(req, 'registration/register.html', {'form': form})