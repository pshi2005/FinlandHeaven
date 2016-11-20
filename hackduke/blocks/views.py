from django.shortcuts import render
from django import template
from django.http import HttpResponse
from .models import Userlogin
from .forms import PostForm
getuser_html = \
'''
{% extends 'layouts/base.html' %}
{% block title %}Contact - {{ block.super }}{% endblock %}

{% block content %}
<h1>Contact</h1>
<form role="form" action="" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
{% endblock %}
'''

def hello(request):
    return HttpResponse("Hello world")

# def getuser(request):
    # t = template.Template(getuser_html)
    # c = template.Context({'name': 'Nige'})
    # return HttpResponse(t.render(c))

def post_new(request):
    form = PostForm()
    usr = form.usr
    # if request.method == 'POST':
    #     post_data = [('name', 'Gladys'), ]  # a sequence of two element tuples
    #     result = urllib2.urlopen('http://example.com',
    #                              urllib.urlencode(post_data))
    #     content = result.read()
    return render(request, 'blocks/post_edit.html', {'form': form, 'usr':
        usr})