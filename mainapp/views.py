from django.shortcuts import get_object_or_404, render, redirect
from .models import Center
from day.models import Message
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CenterForm, EditCenterForm
from django.utils import timezone


def home_view(request):
    return render(request, "mainapp/home.html")


def about_view(request):
    return render(request, "mainapp/about.html")


def center_view(request):
    centers = Center.objects.all()
    context = {'centers': centers}
    return render(request, 'mainapp/center.html', context)


@login_required
def add_center(request):
    if request.method == "POST":
        form = CenterForm(request.POST)
        if form.is_valid():
            new_center = form.save(commit=False)
            new_center.owner = request.user
            new_center.save()
            messages.success(request, 'New Center Added!',
            extra_tags = 'alert alert-success alert-dismissable fade show')
            return redirect('mainapp:center')
    else:
        form = CenterForm()
    context = {'form':form}
    return render(request, 'mainapp/add_center.html', context)


@login_required
def edit_center(request, cent_id):
    cent = get_object_or_404(Center, id=cent_id)
    # if request.user != cent.owner:
    #     return redirect('/')

    if request.method == 'POST':
        form = EditCenterForm(request.POST, instance=cent)
        if form.is_valid():
            form.save()
            messages.success(request, 
                            'Center Edited Successfully',
                            extra_tags='alert alert-success alert-dismissable fade show')
            return redirect('mainapp:center')
    else:
        form = EditCenterForm(instance = cent)
    return render(request, 'mainapp/edit_center.html', {'form':form, 'cent':cent})


@login_required
def delete_center(request, cent_id):
    cent = get_object_or_404(Center, id=cent_id)
    # if request.user != cent.owner:
    #     return redirect('/')
    if request.method == 'POST':
        cent.delete()
        messages.success(request, 
                        'Center Deleted Successfully',
                        extra_tags='alert alert-success alert-dismissable fade show')
        return redirect('mainapp:center')
    return render(request, 'mainapp/delete_center_confirm.html', {'cent':cent})


@login_required
def messages_view(request):
    msg = Message.objects.filter(date_posted__lte=timezone.now()).order_by('-date_posted')
    context = { 'msg':msg }
    return render(request, 'mainapp/messages.html', context)

@login_required
def messages_detail_view(request, id):
    msgdtl = get_object_or_404(Message, id=id)
    return render(request, 'mainapp/messagedetail.html', {'msgdtl':msgdtl})

def contact_view(request):
    return render(request, "mainapp/contact.html")

def pop_view(request):
    if request.method == 'POST':
        form = BottomForm(request.POST or None)
        if form.is_valid():
            the_form = form.save(commit=False)
            the_form.date_posted = datetime.datetime.now()
            the_form.save()

            return redirect('mainapp:home')
    else:
        form = BottomForm()
    context = {
        'form':form
    }
    return render(request, 'mainapp/trial.html', context)
