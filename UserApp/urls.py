from django.urls import path,include
from . import views
urlpatterns = [
    path('hello',views.hello),
    path('',views.home),
    path('deals',views.deals),
    path('ShowCakes/<id>',views.showCakes),
    path('ViewDetails/<id>',views.ViewDetails),
    path('SignUp',views.signUp),
    path('Login',views.login),
    path('Logout',views.logout),
    path('AddToCart',views.AddToCart),
    path('ShowAllCartItems',views.ShowAllCartItems),
    path('UpdateCart',views.UpdateCart),
    path('MakePayment',views.MakePayment),
]
