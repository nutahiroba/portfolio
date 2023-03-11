from django.views.generic import View
from django.shortcuts import render

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
      return render(request,"app/index.html")