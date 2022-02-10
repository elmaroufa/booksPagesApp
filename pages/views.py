#from django.shortcuts import render

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'



class SalyAbbo:
    
    work_skill = 'Backend Developer Python'
    framework = {
        'Python' : [ 'DJANGO', 'FLASK'],
        'JAVASCRIPT' : 'REACTJS',
    }
    
    def otherInfon(sefl):
        return 'I like to read about code and design thinking'