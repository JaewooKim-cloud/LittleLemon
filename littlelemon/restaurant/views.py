from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    #def get_queryset(self):
    #    return Menu.objects.all()

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer