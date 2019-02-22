from django.shortcuts import render, redirect
from .models import Property
from .forms import PropertyForm
from django.views.generic import CreateView,UpdateView
from django.views.generic.edit import ModelFormMixin
from django.utils.decorators import method_decorator
from .decorator import user_authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def listing(request, id):
    # property = Property.objects.get(id=id)
    # images = property.images.all()

    context={
        'property': property,
        # 'images':images

    }
    return render(request,'properties/listing.html',context)


def listings(request):
    properties = Property.objects.all()
    # count = 1
    # images = []
    # for i in properties:
    #     if count == 1:
    #         images = i.images.all()
    #         count = count + 1
    #  print(images[0].image)
    return render(request, 'properties/listings.html', {'properties': properties,})
@method_decorator(user_authenticate, name='dispatch')
class SaveProperty(CreateView):
  model = Property
  form_class = PropertyForm
  template_name = 'properties/propertyform.html'
  success_url = '/'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.profile = self.request.user
    self.object.save()
    return super(SaveProperty, self).form_valid(form)