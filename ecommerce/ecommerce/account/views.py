from django.contrib.auth import get_user_model
from django.shortcuts import render, HttpResponseRedirect, reverse

from .forms import UserNameChangeForm

User = get_user_model()

def view_account(req):
    return render(req, 'account/view_account_details.html')


def change_username(req):
    if req.method == 'POST':
        user = User.objects.get(id = req.user.id)
        form = UserNameChangeForm(instance=user, data=req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('view_account'))

    else:
        user = User.objects.get(id = req.user.id)
        form = UserNameChangeForm(instance=user)

    return render(req, 'account/change_name.html', {'form': form})
