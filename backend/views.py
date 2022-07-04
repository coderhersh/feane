from django.shortcuts import redirect, render
from backend.models import FoodItem, BookTable

# Create your views here.
def index(request):
    return render(request, 'index.html', {'FoodItems' : FoodItem.objects.all()})

def menu(request):
    return render(request, 'menu.html', {'FoodItems' : FoodItem.objects.all()})

def book(request):
    return render(request, 'book.html')

def submit(request):
    if request.method == 'POST':
        name = request.POST["Name"]
        email_address = request.POST["Email"]
        phone_number = int(request.POST["Phone_Number"])
        number_of_persons = int(request.POST["number"])
        date = request.POST["Date"]

        BookTable(name=name, email=email_address, phone_number=phone_number,
        number_of_persons=number_of_persons, date=date).save()
        print(name, email_address, phone_number, number_of_persons, date)

    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
