from django.http import HttpResponse
from django.views.generic import TemplateView


def homePageView(req):
    return HttpResponse("Hello, World")


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
