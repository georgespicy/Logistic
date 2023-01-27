from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'logistic/home.html')

def about(request):
    return render(request, 'logistic/about.html')

def service(request):
    return render(request, 'logistic/service.html')

def contact(request):
    return render(request, 'logistic/contact.html')

# def RequestQuote(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         contact_number = request.POST['contact_number']
#         catagories_one = request.POST['catagories_one']
#         catagories_two = request.POST['catagories-two']
#         catagories_three = request.POST['catagories-three']
#         catagories_four = request.POST['catagories-four']
#         city_of_departure = request.POST['city_of_departure']
#         incoterms = request.POST['incoterms']
#         weight = request.POST['weight']
#         height = request.POST['height']
#         width = request.POST['width']
#         length = request.POST['length']
#         freight = request.POST['freight']
#         express_delivery = request.POST['express-delivery']
#         insurance = request.POST['insurance']
#         packaging = request.POST['packaging']

#         RequestQuote.objects.create(
#              name=name,
#              email=email,
#              contact_number=contact_number,
#              catagories_one=catagories_one,
#              catagories_two=catagories_two,
#              catagories_three=catagories_three,
#              catagories_four=catagories_four,
#              city_of_departure=city_of_departure,
#              incoterms=incoterms,
#              weight=weight,
#              height=height,
#              width=width,
#              length=length,
#              freight=freight,
#              express_delivery=express_delivery,
#              insurance=insurance,
#              packaging=packaging,
#         )
#         return redirect(request.META.get('HTTP_REFERER'))
    
def incoterms(request):
    if request.method == 'POST':
        incoterms = request.POST['incoterms']
        Incoterms.objects.create(
            incoterms=incoterms
        )
        return redirect(request.META.get('HTTP_REFERER'))