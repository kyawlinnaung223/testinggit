from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room,Topic
from .forms import CreateForm
from django.db.models import Q

# Create your views here.




#this is homepageviews
def HomepageView(request):
    p=request.GET.get('p') if request.GET.get('p') != None else ''
    rooms=Room.objects.filter(
        Q(topic__name__icontains=p)|
        Q(name__icontains=p)|
        Q(description__icontains=p)
        )
    topics=Topic.objects.all()
    room_count=rooms.count()
    context={'rooms':rooms,'topics':topics,'room_count':room_count}
    return render(request,'base/home.html',context)
#end homepageviews

#this is room
def RoompageView(request, pk):
    room=Room.objects.get(id=pk)
    context={'room':room}   
    return render (request,'base/room.html',context)
#end room


#this is room_createviews 
def RoomCreateView(request):
    form=CreateForm()
    if request.method == 'POST':
        form=CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render (request,'base/room_form.html',context)
#end room_reateViews

#this is updateviews
def updateroom(request, pk):
    room=Room.objects.get(id=pk)
    form=CreateForm(instance=room)
    if request.method == 'POST':
        form=CreateForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context={'form':form}
    return render (request, 'base/room_form.html',context)
#end updateviews

# this is delete views
def deleteviews(request, pk):
    room=Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect ('home')
    
    return render(request,'base/delete.html',{'items':room})
#end delete views





          
