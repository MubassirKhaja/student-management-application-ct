from django.shortcuts import render
from .forms import StudForm, Ssearch
from .models import stud, school, books
import csv

# Create your views here.

def show(request):
    return render(request, "home.html")

def register(request):
    title = "Add New Student manually"

    form = StudForm(request.POST or None)

    if form.is_valid():
        UID =	form.cleaned_data['ID']
        firstname	=	form.cleaned_data['first_name']
        lastname	=	form.cleaned_data['last_name']
        mail	=	form.cleaned_data['email']
        gender	=	form.cleaned_data['gender']
        school	=	form.cleaned_data['school']
        books = form.cleaned_data['books']

        p = stud(ID = UID, first_name = firstname, last_name = lastname, email = mail, gender = gender, school = school, books= books)
        p.save()
        return render(request, 'success.html',{"title" : f"Student {firstname} Registered Succesfully"})


    context = {
        "title" : title,
        "form" : form
    }
    return render(request, 'register.html',context)

def registered_students(request):
    title = "Registered Students"
    queryset = stud.objects.all()
    # queryset1 = school.objects.all()
    # print(queryset1)
    lst = []
    qs2 =list(queryset)
    print(qs2)

    mydict = {"ID":[],
            "first_name":[],
            "last_name":[],
            "email":[],
            "gender":[],
            "school":[],
            "books":[],
            "phone":[],
    
            }

    for i in qs2:
        # print(i.ID)
        x = school.objects.filter(school=i.school)
        for j in x:
            mydict["ID"].append( i.ID)
            mydict["first_name"].append( i.first_name)
            mydict["last_name"].append( i.last_name)
            mydict["email"].append( i.email)
            mydict["gender"].append( i.gender)
            mydict["school"].append( i.school)
            mydict["books"].append( i.books)
            mydict["phone"].append( j.phone)
            # print(j.phone)
            # i['phone'] = j.phone
            # qs2.append(i.phone)
            # i.append(j.phone)
    print(mydict.values())

    

    context = {
        "title":title,
        "queryset":queryset,
        # "queryset1":lst,

       
    }
    return render(request,"registered_students.html",context)

def search(request):
    title  = " Search for a student in database"
    form = Ssearch(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['first_name']
        id = form.cleaned_data['ID']
        print(type(name),id)
        if (str(id)) != "None" and (str(name))  != "":
            return render(request, 'success.html',{"title" : f"Please enter any one value"})
        global queryset

        if  (str(name)) != "" :
            queryset = stud.objects.filter(first_name = name)
        else:
            queryset = stud.objects.filter(ID = id)

            

        
        print(queryset)
        if len(queryset) == 0 :
            return render(request, "success.html", {"title": " No details found"})
        else:

            context = {
                "title": "Search Results",
                "queryset" : queryset  
            }
            return render(request, "registered_students.html", context)

    context = {
        "title" : title,
        "form" : form
    }

    return render(request,"search.html", context)

def upload(request):
    if request.method == 'POST':

        uploaded_file =  request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        print(uploaded_file)
        for i in uploaded_file:
            # print(i)
            x = i.decode().split(",")
            # print(x[0])
            if x[0] != "ID":
                print(x[1])
                p = stud(ID = x[0], first_name = x[1], last_name = x[2], email = x[3], gender = x[4], school = x[5], books= x[6])
                p.save()
        return render(request, 'success.html',{"title" : f"Data in file uploaded Succesfully"})
    context = {"title" : "Students CSV - Upload File"}
    return render(request,"upload.html", context)

def upload_school(request):
    if request.method == 'POST':

        uploaded_file =  request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        print(uploaded_file)
        for i in uploaded_file:
            # print(i)
            x = i.decode().split(",")
            # print(x[0])
            if x[0] != "REGIONID":
                print(x[1])
                p = school(REGIONID = x[0],school = x[1], email = x[2], principal = x[3], phone = x[4], address2 = x[5])
                p.save()
        return render(request, 'success.html',{"title" : f"School Data in file uploaded Succesfully"})
    context = {"title" : " School CSV - Upload File"}
    return render(request,"upload.html", context)

def books_upload(request):
    if request.method == 'POST':

        uploaded_file =  request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        print(uploaded_file)
        for i in uploaded_file:
            x = i.decode().split(",")
            if str(x[0]) != "Title":
                print(x[1])
                p = books(Title = x[0], Author_Name = x[1], Date_of_Publication = x[2], Number_of_Pages = x[3])
                p.save()
        return render(request, 'success.html',{"title" : f"Books Data in file uploaded Succesfully"})
    context = {"title" : "Books CSV - Upload File"}
    return render(request,"upload.html", context)


def registered_books(request):
    title = "Registered Books"
    queryset = books.objects.all()

    context = {
        "title":title,
        "queryset":queryset,
    }
    return render(request,"books.html",context)

def registered_schools(request):
    title = "Registered Schools"
    queryset = school.objects.all()

    context = {
        "title":title,
        "queryset":queryset,
    }
    return render(request,"schools.html",context)