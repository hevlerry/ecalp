from django.shortcuts import render, redirect
from .models import Product
from .forms import PostProductForm

def newsfeed(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'newsfeed/templates/newsfeed.html', {'products': products})


def post_product(request):
    if request.method == 'POST':
        form = PostProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('newsfeed')
    else:
        form = PostProductForm()
    return render(request, 'newsfeed/post_product.html', {'form': form})

