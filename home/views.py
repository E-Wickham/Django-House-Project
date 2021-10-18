from django.shortcuts import render
from .models import Listing
from django.http import JsonResponse
from django.core import serializers

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('Date')
    return render(request, "index.html", {'listings': listings})

def pivot_data(request):
    dataset = Listing.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)