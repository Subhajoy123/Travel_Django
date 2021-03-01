from django.shortcuts import render
from django.http import HttpResponse
from .models import destination
# Create your views here.
def index(request):
  #  des=destination()
   # des1=destination()
   # des2=destination()
   # des.name='Mumbai'
   # des.desc='The city that never sleeps'
    #des.price=700
    #des.offer= False
    #des.img='destination_1.jpg'
    #des1.name='Delhi'
    #des1.desc='The capital city '
    #des1.price=900
    #des1.offer=True
   # des1.img='destination_2.jpg'
    #des2.name='Kolkata'
    #des2.desc='The city of dreams'
    #des2.price=900
    #des2.img='destination_3.jpg'
   # des2.offer=False
    #dess=[des,des1,des2] 
    dess =destination.objects.all()

    return render(request, 'index.html', {'dess':dess})

