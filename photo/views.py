from django.shortcuts import render
from django.http import HttpResponse, Http404# responsible for returning a response to a user
import datetime as dt
from .models import Image,Location,Photographer,Category


# Create your views here.
def fashion(request):
    images = Image.objects.all()
    return render(request, 'fashion.html',{'images':images})

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_photos = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photo/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photo/search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photo/image.html", {"image":image})
# def filter_by_location(request,location_name):
#    """
#    Function that filters images by location
#    """
#    images = Image.filter_by_location(location_name = )
#    return render (request, 'all-photo/location.html', {"images":images})   
def location(request,location_id):
    italy = Image.objects.filter(location_id=location_id)
    return render(request,'all-photo/location.html',{"locations:locations"})
