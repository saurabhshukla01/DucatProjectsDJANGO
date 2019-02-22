from django.shortcuts import render
from properties.models import Property

# Create your views here.


def index(request):
    properties = Property.objects.order_by('-list_date').filter(is_published=True)[:3]
    count = 1
    cities = []
    states = []
    for i in properties:
        city = i.city
        state = i.state
        if city not in cities:
            cities.append(city)
        if state not in states:
            states.append(state)
        # if count == 2:
        #    images = i.images.all()
        #    count = count+1
        #    print(images)
        # print(i.images.all())
        # print(states)

    return render(request, 'pages/index.html',{'properties':properties,'cities':cities,'states':states})


def about(request):
    # sellers = Seller.objects.order_by('-register_date')
    return render(request, 'pages/about.html')








def search(request):
    query_list = Property.objects.all()

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        query_list = Property.objects.filter(name__icontains=keywords)

    if 'state' in request.GET:
        state = request.GET['state']
        print(state)
        query_list = Property.objects.filter(state__iexact=state)

    print(query_list)
    return render(request,'pages/search.html',{'query_list':query_list})
