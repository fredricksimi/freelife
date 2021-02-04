from django.shortcuts import render, redirect
from .forms import AddressForm
from .models import Message
from django.contrib import messages
import datetime

# Create your views here.
def home_view(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.date_posted = datetime.datetime.now()
            new_form.save()
            messages.success(request, 'Message sent succesfully!',
            extra_tags = 'alert alert-success alert-dismissable fade show')
            return redirect('day:home')
    else:
        form = AddressForm()
    context = {
        'form':form
    }
    return render(request, 'day/hello.html', context)
