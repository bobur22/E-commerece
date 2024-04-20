from django.shortcuts import render, redirect
from .models import contactModel, productModel
from django.core.mail import send_mail
from django.core.paginator import Paginator

def homeView(request):
    product_m = productModel.objects.order_by('?')[:8]
    product_e = productModel.objects.order_by('?')[:8]
    return render(request, template_name="index.html", context={"product_m":product_m, "product_e":product_e})

def shopView(request):
    product_m = productModel.objects.all()
    paginator = Paginator(product_m, 4)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, template_name='shop.html', context={"page_obj": page_obj})

def productdetailView(request, id):
    product_d = productModel.objects.get(id=id)
    product_m = productModel.objects.order_by('?')[:4]

    return render(request, template_name='sproduct.html', context={"product_d":product_d, "product_m":product_m})

def addcartprdView(request, id):
    cart = request.session.get('cart', default=[])
    cart.append(id)

    request.session['cart'] = cart

    return redirect('e_commerce:pdetail', id=id)

def addcarthomeView(request, id):
    cart = request.session.get('cart', default=[])
    cart.append(id)

    request.session['cart'] = cart

    return redirect('e_commerce:home')
def blogView(request):
    return render(request, template_name='blog.html')

def aboutView(request):
    return render(request, template_name='about.html')

def contactView(request):
    contact_m = contactModel.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        message_all = "Your messsage was confirmed."

        contactm_1 = contactModel(name=name, email=email, subject=subject, message=message)
        contactm_1.save()

        send_mail('Contact Form', message_all, 'settings.EMAIL_HOST_USER', [email], fail_silently=False)

        return redirect("e_commerce:contact")

    return render(request, template_name='contact.html', context={"contact_m":contact_m})

def addcartView(request, id):
    cart = request.session.get('cart', default=[])
    cart.append(id)

    request.session['cart'] = cart

    return redirect('e_commerce:shop')

def removecartView(request, id):
    cart = request.session.get('cart', default=[])
    cart.remove(id)

    request.session['cart'] = cart

    return redirect('e_commerce:cart')

def cartView(request):
    cart = request.session.get('cart', default=[])
    product = productModel.objects.filter(id__in=cart)
    subtotal = 0
    total = 35
    for i in product:
        subtotal += i.price
    total += subtotal
    return render(request, template_name='cart.html', context={"product":product, "subtotal":subtotal, "total":total})

def emailUpdate(request):
    if request.method == "POST":
        email = request.POST["email"]
        message_all = "Your messsage was confirmed.You will get E-mail updates about our latest shop and special offers."

        send_mail('Contact Form', message_all, 'settings.EMAIL_HOST_USER', [email], fail_silently=False)

        return redirect("e_commerce:home")

    return render(request, template_name='layouts/footer.html')
