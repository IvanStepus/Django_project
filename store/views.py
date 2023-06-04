from django.shortcuts import render


def cart_view(request):  #request - http packet
    return render(request, 'cart_page.html')

def sale_view(request):  #request - http packet
    return render(request, 'enpty_page.html')

def promo_view(request):  #request - http packet
    return render(request, 'enpty_page.html')