from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class index_2(TemplateView):
    template_name = 'second_task/class_template.html'

def index_1(request):
    return render(request, 'second_task/func_template.html')