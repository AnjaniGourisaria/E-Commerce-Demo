#THis Site is A Ecommerce Site TO get work with fix some bug like validate and make it responseive for mobile and desktop User Using the things you can add on to your cravity 
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
    
TO get public ip
    
    https://stackoverflow.com/questions/391979/how-to-get-clients-ip-address-using-javascript
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
    $.get('https://www.cloudflare.com/cdn-cgi/trace', function(data) {
    // Convert key-value pairs to JSON
    // https://stackoverflow.com/a/39284735/452587
    data = data.trim().split('\n').reduce(function(obj, pair) {
    pair = pair.split('=');
    return obj[pair[0]] = pair[1], obj;
    }, {});
    console.log(data);  
    });
    
    
