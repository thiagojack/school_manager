from django.http import HttpResponse
from django.views import View
from .models import Grid
# Create your views here.

class GridView(View):
    grids = Grid.objects.all()
    
    def get(self, request):
        grid_list = []
        for grid in self.grids:
            grid_list.append(grid)
        return HttpResponse(grid_list)