from django.shortcuts import render,redirect

def index(request):
    return render(request,"amadon_store/index.html")

def buy_product(request):
    new_purchase={}
    for key,value in request.POST.items():
        if key!="csrfmiddlewaretoken":
            new_purchase[key]=value

    if new_purchase["product_id"]=="1":
        new_purchase['product']="Dojo Shirts"
        new_purchase["total"]=int(new_purchase["quantity"])*19.99
    elif new_purchase["product_id"]=="2":
        new_purchase['product']="Dojo Sweaters"
        new_purchase["total"]=int(new_purchase["quantity"])*29.99
    elif new_purchase["product_id"]=="3":
        new_purchase['product']="Dojo Cups"
        new_purchase["total"]=int(new_purchase["quantity"])*9.99
    else:
        new_purchase["product"]="Dojo Books"
        new_purchase["total"]=int(new_purchase["quantity"])*69.99

    print new_purchase

    request.session['purchase']=[]

    request.session['purchase']=new_purchase
    print request.session['purchase']

    return redirect('/checkout')


def checkout(request):
    return render(request, 'amadon_store/checkout.html')
