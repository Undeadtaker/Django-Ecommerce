from django.shortcuts import render

def view_account(req):
    return render(req, 'account/view_account_details.html')
