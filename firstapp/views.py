from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
# Supersuser, username: admin and pass: admin


def say_hello(request):
    query_set1=Product.objects.all()
    for pro in query_set1:
        print(pro)

    print("*************")

    query_set2=Product.objects.count()

    print(query_set2)
    print("************")
    try:
        product1=Product.objects.get(pk=0)
    except ObjectDoesNotExist:
        print("ObjectDoesNotExists exception raised")
        product1=None
        pass
    
    print(product1)

    print("************")

    exists=Product.objects.filter(pk=0).exists()
    print(exists)
    print("***************")
    #return HttpResponse("Hello world")
    # the below query will fetch all the records having id<3
    # similary you can also write queries:
    # query_set3=Product.objects.filter(id__gt=3)
    # query_set3=Product.objects.filter(id__range=(1,2,3))
    # query_set3=Product.objects.filter(title__contains="Coffee")
    query_set3=Product.objects.filter(id__lt=3)
    print(query_set3)
    print("************")

    query_set4=Product.objects.filter(title__startswith="Pro")
    print(query_set4)
    print("************")

    return render(request,'hello.html',{'name':'Khushi','country':'Switzerland','products':list(query_set1)})

    

    


        


    # x=10
    # y=20
    # print("Request arrived")
    return render(request,'hello.html',{'name':"Khushi",'country':"Switzerland"})