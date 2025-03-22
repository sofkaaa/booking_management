from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import PCRoom, Computer , UProfile , BookedPCRoom
from django.urls import reverse
# Create your views here.

def pcroom_list(request:HttpRequest):
    pcrooms = PCRoom.objects.all()

    context = {"pcroom": pcrooms}

    return render(request, "booking/pcroom_list.html" )

def computer_list(request:HttpRequest, pcroom_id: int):

    computers = Computer.objects.filter(pcroom__id = pcroom_id)

    context = {"computer": computers}

    return render(request, "booking/computer_list.html", context= context )

def create_pcroom(request: HttpRequest):
    if request.method == "GET":
        return render(request, "booking/create_room.html")
    if request.method == "POST":
        pcroom_number = request.POST.get("pcroom_number")
        computer_num = request.POST.get("computer_num", 0)

        PCRoom.objects.create(number=pcroom_number, computer_num= computer_num)

        return redirect(reverse("pcrooms-list"))


def book_pcroom(request: HttpRequest):
    if request.method == "GET":
        return render(request, "booking/book_pcroom.html")
    if request.method == "POST":
        pcroom_number = request.POST.get("pcroom_num")
        user_name = request.POST.get("user")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        email = request.POST.get("email")

        pcroom = PCRoom.objects.get(number=pcroom_number)
        uprofile, new = UProfile.objects.get_or_create(name=user_name)

        
        if BookedPCRoom.objects.filter(pcroom=pcroom, start_time__lt=end_time, end_time__gt=start_time).exists():
            return HttpResponse("Ця кімната вже заброньована на цей період")

        
        try:
            new_booked_pcroom = BookedPCRoom.objects.create(pcroom=pcroom, uprofile=uprofile, start_time=start_time, end_time=end_time, email=email)
        except IntegrityError:
            return HttpResponse("Ця кімната вже заброньована на цей період")

        return redirect(reverse("pcroom-list"))
    
def book_computer(request: HttpRequest):
    if request.method == "GET":
        return render(request, "booking/book_computer.html")
    if request.method == "POST":
        computer_id = request.POST.get("pcroom_num")
        user_name = request.POST.get("user")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")

        computer = Computer.objects.get(id = computer_id)

        uprofile, new = UProfile.objects.get_or_create(name=user_name)

        new_booked_pcroom = BookedPCRoom.objects.create(computer = computer, uprofile = uprofile, start_time= start_time, end_time=end_time )

        return redirect(reverse("computer-list"))
    