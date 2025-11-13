from django.shortcuts import render, redirect
from .models import Appointment, Client, Staff, Service
from django.utils import timezone
from datetime import datetime

def calendar_view(request):
    appointments = Appointment.objects.all().order_by("start_time")
    return render(request, "appointments/calendar.html", {"appointments": appointments})

def create_appointment(request):
    clients = Client.objects.all()
    staff = Staff.objects.all()
    services = Service.objects.all()

    if request.method == "POST":
        client = request.POST["client"]
        staff_member = request.POST["staff"]
        service = request.POST["service"]
        date = request.POST["date"]
        time = request.POST["time"]

        dt = f"{date} {time}"
        start_dt = timezone.make_aware(datetime.fromisoformat(dt))

        Appointment.objects.create(
            client_id=client,
            staff_id=staff_member,
            service_id=service,
            start_time=start_dt,
        )
        return redirect("calendar_view")

    return render(request, "appointments/create_appointment.html", {
        "clients": clients,
        "staff": staff,
        "services": services,
    })
