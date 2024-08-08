from django.shortcuts import render, redirect, HttpResponse
from .models import Tickets, ContactView
from .forms import ContactForm, FlightForm

# Create your views here.
def HomeView(request):
    queryset = Tickets.objects.filter(status=True)
    form = ContactForm(None)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'tickets': queryset,
        'form': form
    }
    return render(request, 'index.html', context)
def BookView(request):
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successful")
    else:
        form = FlightForm()
    return render(request, 'reservation.html', context={
        'form': form
    })

def StaffView(request):
    queryset = ContactView.objects.all()
    context = {
        'clients': queryset
    }
    return render(request, 'staff.html', context=context)

def DeleteView(request, id):
    queryset = ContactView.objects.get(id=id).delete()
    return redirect('staff')


