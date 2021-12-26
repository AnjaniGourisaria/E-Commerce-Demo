#TO Redirect To login if that feature is only accessd by login
from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login/')
