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
        'stripe_public_key': 'pk_test_51JKToXFEaVTvtYDF1hL0ncQN4XkV4Sug2p2s2al5rGDGK6vp5R3eFkUggY0T6WZRJo3PQyucuHPI4NRNNfHVah5Z00aS2lgR1v',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)