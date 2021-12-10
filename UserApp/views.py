from django.shortcuts import render,redirect,HttpResponse
from AdminApp.models import Category,Cake
from UserApp.models import UserInfo,MyCart,MyAccount,OrderMaster
from datetime import datetime
from django.contrib import messages
# Create your views here.
def hello(request):
    c1 = Cake.objects.get(id=4)
    return render(request,"UserApp/hello.html",{"c1":c1})

def home(request):
    #Fetch all Categories
    cats = Category.objects.all()
    #Fetch all cakes
    cakes = Cake.objects.all()
    return render(request,"master.html",{"cats":cats,"cakes":cakes})

def showCakes(request,id):
    cats = Category.objects.all()
    cat = Category.objects.get(id=id)
    #This approach is wrong ->Error
    #cakes = Cake.objects.filter(category = id)
    cakes = Cake.objects.filter(category = cat)
    return render(request,"master.html",{"cats":cats,"cakes":cakes})

def ViewDetails(request,id):
    cats = Category.objects.all()
    cake = Cake.objects.get(id=id)
    return render(request,"UserApp/ViewDetails.html",{"cake":cake,"cats":cats})

def deals(request):
    return render(request,"UserApp/Deals.html",{})

def signUp(request):
    if(request.method=="GET"):
        cats = Category.objects.all()
        return render(request,"UserApp/SignUp.html",{"cats":cats})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        email = request.POST["email"]

        #Check if username already exists
        try:
            user = UserInfo.objects.get(unamename = uname)
        except:
            user = UserInfo(uname,pwd,email)
            user.save()
        else:
            return HttpResponse("User name already present")
        return redirect(home)


def login(request):
    if(request.method == "GET"):
        cats = Category.objects.all()
        return render(request,"UserApp/Login.html",{"cats":cats})
    else:
        #Check username and password
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            user = UserInfo.objects.get(username=uname,password=pwd)
        except:
            return redirect(login)

        #If login is successful store user name in session
        request.session["uname"] = uname
        return redirect(home)


def logout(request):
    request.session.clear()
    return redirect(home)

def AddToCart(request):
    if(request.method=="POST"):
        if("uname" in request.session):
            #User has logged in
            #add to cart
            #Collect the user object
            #Dont insert directly, first check for already existing item
            user = UserInfo.objects.get(username=request.session["uname"])
            cake = Cake.objects.get(id=request.POST["cakeid"])
            try:
                c = MyCart.objects.get(user=user,cake=cake)
            except:
                qty = request.POST["qty"];
                cart = MyCart()
                cart.user = user
                cart.cake = cake
                cart.qty = qty
                cart.save()
                #return HttpResponse("Add to cart")
                messages.success(request,"Item added successfully to cart!!")                
            messages.error(request,"Item already in cart")
            return redirect(deals)
        else:
            #User is not logged in so
            #redirect him to login screen
            return redirect(login)
        

def ShowAllCartItems(request):
    if("uname" not in request.session):
        return redirect(login)
    else:
        user = UserInfo.objects.get(username=request.session["uname"])
        #Get rows for logged in user
        cart_items = MyCart.objects.filter(user=user)
        cats = Category.objects.all()
        total = 0
        for cart in cart_items:
            total += cart.cake.price * cart.qty
        
        request.session["total"] = total
        return render(request,"UserApp/ShowAllCartItems.html",{"cats":cats,"carts":cart_items})


def UpdateCart(request):
    if(request.method == "POST"):
        action = request.POST["action"]
        cakeid= request.POST["cakeid"]
        user = UserInfo.objects.get(username=request.session["uname"])
        cake = Cake.objects.get(id=cakeid)
        #Find the cake
        cartitem = MyCart.objects.get(cake=cake,user=user)
        
        if(action=="remove"):            
            cartitem.delete()
        elif(action == "update"):
            cartitem.qty = request.POST["qty"]
            cartitem.save()
        return redirect(ShowAllCartItems)


def MakePayment(request):
    if(request.method=="GET"):
        return render(request,"UserApp/MakePayment.html",{})
    else:
        cardno = request.POST["cardno"];
        cvv =request.POST["cvv"]
        expiry = request.POST["expiry"]
        
        try:
            buyer = MyAccount.objects.get(cardno=cardno,cvv=cvv,expiry=expiry)
            owner = MyAccount.objects.get(cardno="333",cvv="333",expiry="12/2030")
        
            owner.balance += request.session["total"]
            buyer.balance -= request.session["total"]

            owner.save()
            buyer.save()

            #Update orderMAster
            order = OrderMaster()
            order.user =  user = UserInfo.objects.get(username=request.session["uname"])
            #this will give current date
            order.dateOfOrder = datetime.now().date()
            order.amount = request.session["total"]
            order.save()

            #Delete info from cart that user's products            
            cartitems = MyCart.objects.filter(user= UserInfo.objects.get(username=request.session["uname"]))
            for cart in cartitems:
                cart.delete()
            
            return HttpResponse("Payment done successfully")
        except:
            return HttpResponse("Invalid Card Details")

        



        
