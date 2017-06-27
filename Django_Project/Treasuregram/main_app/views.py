from django.shortcuts import render
from .models import Treasure
"""If you want to import a specific class from your current app,
you can leave off the package and type the following:
from .module import class (or function)"""

# Create your views here.
def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures':treasures})


"""class Treasure:
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url

treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM", 'static/imgs/gold.png'),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO", 'static/imgs/fools_gold.jpg'),
    Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA', 'static/imgs/cof_cup.png'),
]"""
