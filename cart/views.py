from django.shortcuts import render, redirect
from django.views import View
from shop.models import Product
from cart.models import Cart




class Addtocart(View):
    def get(self,request,i):
        u=request.user
        p=Product.objects.get(id=i)

        try:
            c=Cart.objects.get(user=u,product=p)
            c.quantity+=1
            c.save()
        except:
            c=Cart.objects.create(user=u,product=p,quantity=1)
            c.save()

        return redirect('cart:cartview')

class CartView(View):
    def get(self,request):
        c=Cart.objects.filter(user=request.user)
        total=0
        for i in c:
            total=total+i.subtotal()

        context={'cart':c,'total':total}
        return render(request,'cart.html',context)

class Cartdecrement(View):
    def get(self,request,i):
        c=Cart.objects.get(id=i)
        if(c.quantity>1):
           c.quantity-=1
           c.save()
        else:
            c.delete()
        return redirect('cart:cartview')

class Cartremove(View):
    def get(self,request,i):
        c=Cart.objects.get(id=i)
        c.delete()
        return redirect('cart:cartview')

from cart.forms import CheckoutForm
class Checkout(View):
    def post(self,request):
        form_instance=CheckoutForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return render(request,'payment.html')

    def get(self,request):
        form_instance=CheckoutForm()
        context={'form':form_instance}
        return render(request,'checkout.html',context)


