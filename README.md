TO Redirect To login if that feature is only accessd by login

    from django.contrib.auth.decorators import login_required #import this to use the feature
    @login_required(login_url='/accounts/login/') # @login_requried replace with this in views.py(home/views.py) 
