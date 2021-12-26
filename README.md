# E-Commerce-Demo
This is demo site
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
