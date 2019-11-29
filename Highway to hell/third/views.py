from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator ##9번째
from third.models import Restaurant, Review ## 8번째
from third.forms import Restaurant, RestaurantForm, ReviewForm
from django.http import HttpResponseRedirect


# Create your views here.
def list(request):      ##4번째
    restaurant = Restaurant.objects.all()   ##9번쨰
    paginator = Paginator(restaurant, 5)

    page = request.GET.get('page')  ## third/list?page=1
    items = paginator.get_page(page)

    context = {
        'restaurants': items ##8번쨰
    }
    return render(request, 'third/list.html', context)


def create(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/third/list/')
    form = RestaurantForm()
    return render(request, 'third/create.html', {'form': form})


def update(request):
    if request.method == 'POST' and 'id' in request.POST:
        item = get_object_or_404(Restaurant, pk=request.POST.get('id'))
        # item = Restaurant.objects.get(pk=request.POST.get('id'))
        form = RestaurantForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
    elif request.method == 'GET':
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        # item = Restaurant.objects.get(pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form': form})
    return HttpResponseRedirect('/third/list')


def detail(request, id):
    if id is not None:
        item = get_object_or_404(Restaurant, pk=id)
        reviews = Review.objects.filter(restaurant=item).all()
        return render(request, 'third/detail.html', {'item': item, 'reviews': reviews})
    return HttpResponseRedirect('/third/list')


def delete(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item.delete()
    return HttpResponseRedirect('/third/list')


def review_create(request, restaurant_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('restaurant-detail', id=restaurant_id)

    item = get_object_or_404(Restaurant, pk=restaurant_id)
    form = ReviewForm(initial={'restaurant': item})
    return render(request, 'third/review_create.html', {'form': form, 'item': item})


def review_delete(request, restaurant_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()

    return redirect('restaurant-detail', id=restaurant_id)
