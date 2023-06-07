from decimal import Decimal
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, \
                             get_object_or_404

from orders.models import Order


# создать экземпляр Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

def payment_pricess(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        success_url = request.build_adsolute_uri(
            reverse('paymen:completed')
        )


