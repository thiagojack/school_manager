from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Grid
from apps.subjects.models import Subject
# Create your views here.
'''
class GridView(View):
    template_name = 'grids/grids.html'
    
    def get(self, request):
        grids = Grid.objects.filter(code, name, situation)
        context = {
            'grids': grids,
        }
        return render(request, self.template_name, context)
'''