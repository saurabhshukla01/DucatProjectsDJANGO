from django.shortcuts import render

def index(request):
    print(request.method)
    if request.method=='POST':
        n = request.POST['fullname']
        return render(request,'index.html',{'name':n})
    return render(request, 'index.html')
# Create your views here.
