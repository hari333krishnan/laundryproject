from django.shortcuts import render, redirect

from .models import Register
# Create your views here.
def home(request):
    return render(request,'index.html')



def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        h_name = request.POST['h_name']
        city = request.POST['city']
        r_name = request.POST['r_name']
        pin = request.POST['pin']
        mobile = request.POST['mobile']
        customer = Register.objects.create(name=name, house_name=h_name, city=city, road_name=r_name, pincode=pin, mobile=mobile)
        customer.save()
        return redirect('/')
    else:
        return render(request,'register.html')
