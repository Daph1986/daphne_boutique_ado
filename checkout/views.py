from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JJdxhLOSkUOoR6L3p8G1NSYYvdinbI5Yld9I5KjT1qbqXS3zEgBE7EfdU271FpLcJSK7nkgK1MGSaJcd57Hhl7U00tK8e8xEG',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)