from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    context = {"products": products}
    return render(request, "frontend/store/index.html", context)


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(name=category).get_descendants(include_self=True)
    )
    context = {"category": category, "products": products}
    return render(request, "frontend/store/category.html", context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    context = {"product": product}
    return render(request, "frontend/store/single.html", context)




def AboutPage(request):
    return render(request, 'frontend/about-us.html')


def ContactPage(request):
    return render(request, 'frontend/contact.html')


def LoginPage(request):
    return render(request, 'frontend/login.html')



def UserDashPage(request):
    return render(request, 'frontend/users/home.html')