TO Redirect To login if that feature is only accessd by login https://docs.djangoproject.com/en/4.0/topics/auth/default/

    from django.contrib.auth.decorators import login_required #import this to use the feature
    @login_required(login_url='/accounts/login/') # @login_requried replace with this in views.py(home/views.py) 

Message Framework

    https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
    {% if messages %}
    <ul class="messages">
    {% for message in messages %}
    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
    {% endfor %}
    </ul>
    {% endif %}
