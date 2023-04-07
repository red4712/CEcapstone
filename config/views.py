from django.shortcuts import render
from django.views.generic import TemplateView
import json
# Create your views here.
class HomeView(TemplateView):
  template_name = 'index.html'

class About(TemplateView):
  template_name = 'About.vue'

def index(request):
    with open('./data/data.json', 'r') as f:
        json_dict = json.loads(f.read())
    return render(request, 'index.html', {'json_dict': json_dict})