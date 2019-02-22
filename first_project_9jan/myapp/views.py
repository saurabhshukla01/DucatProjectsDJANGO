from django.shortcuts import render ,HttpResponse

# Create your views here.
def homepage(request):
	a = " Hello Python Web "
	print(a)
	return HttpResponse("<h1> This is my New Site.</h1>")

def stringformate(request):
	a = " Hello Python Web "
	print(a)
	return HttpResponse(f"<h1> This is my New Site.{a}</h1>{request}")
	
def stringformatedigit(request):
	a = " Hello Python Web "
	b = 9
	c = 10
	print(a,b,c)
	return HttpResponse(f"<h1>{b} This is my New Site{b}.{c}{a}</h1>{request}")	