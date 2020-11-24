from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import login, authenticate
from cars.forms import RegistrationForm, CarModelForm
from account.models import Account
from cars.models import CarDetails, Miles, Fuel, Body, Transmission, Features
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage
from django.core.mail import send_mail
# Create your views here.

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def faq(request):
    return render(request, 'faq.html')

def terms(request):
    return render(request, 'terms.html')

def contact_us(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # send an Email send_mail(subject,message,from email, To email)
        send_mail(name, email, message, ['shashank.bhojappa1989@gmail.com'])

        return render(request, 'contact.html', {'name' : name})
    else:
        return render(request, 'contact.html', {})

def list_cars(request):
    list_all = CarDetails.objects.all()
    p = Paginator(list_all, 3)
    #To get the number of pages
    #print('Number of Pages')
    #print(p.num_pages)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request, "index.html", {'list_all': page})

def list_all_cars(request):
    list_all = CarDetails.objects.all()
    p = Paginator(list_all, 6)
    #To get the number of pages
    #print('Number of Pages')
    #print(p.num_pages)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request, "cars.html", {'list_all': page})

def car_details(request,pk):
    details = CarDetails.objects.get(pk=pk)
    context = {
        'details' : details
    }
    return render(request,'car-details.html', context)

@login_required
def car_form_view(request):
    context = {}

    user = request.user
    #if not user.is_authenticated: (not required as we have used @login_required decorator)
    #    return redirect('login')

    form = CarModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        owner_name = Account.objects.filter(username=user.username).first()
        obj.owner_name = owner_name
        obj.save()
        form = CarModelForm()

    context['form'] = form
    return render(request,'car_form.html',context)

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = form.save()
            login(request, account,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('cars')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'users/register.html', context)

def usernamefunc(user,request):
    user = request.user.username
    name = Account.objects.filter(username=user.username)[1]
    if user == name :
        return True
    else:
        return False

#@user_passes_test(usernamefunc,login_url='login')
@login_required
def update_details(request,pk):
    user = request.user
    car_detail = get_object_or_404(CarDetails,pk=pk)
    if car_detail.owner_name != request.user:
        return HttpResponse("You are not authorized to Edit this section")

    update_car = CarDetails.objects.get(pk=pk)
    form = CarModelForm(instance=update_car)
    if request.method == "POST":
        form = CarModelForm(request.POST,request.FILES, instance=update_car)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form
    }
    return render(request,'update_car_details.html',context)

@login_required
def delete_car(request,pk):
    user = request.user
    car_delete_detail = get_object_or_404(CarDetails,pk=pk)
    if car_delete_detail.owner_name != request.user:
        return HttpResponse("You are not Authorized to Delete this section")
    item = CarDetails.objects.get(pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    context = {
        'item':item
    }
    return render(request,'delete.html',context)

def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups= Q(car_brand__icontains=query) | Q(car_model__icontains=query)
            results= CarDetails.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'search.html', context)
        else:
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')
