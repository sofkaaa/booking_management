from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import PCRoom, Computer
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
