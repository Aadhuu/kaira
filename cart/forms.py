from shop import Forms

from cart.views import Order


class CheckoutForm(forms.Form):
    class Meta:
        model = Order
        fields =['address','phone','payment_method']