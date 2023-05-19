from django.http import HttpResponse
from django.template import loader
from .models import Tourdate

# Create your views here.
def tourdates_view(request):

    # Retrieve all Tourdate objects from the database
    tourdates = Tourdate.objects.all()

    template = loader.get_template('tourdates.html')
    context = {'tourdates': tourdates}
    rendered_template = template.render(context, request)
    return HttpResponse(rendered_template)

def add_tour_dates():
    if Tourdate.objects.count() == 0:
        tourdate1 = Tourdate(date='2023-05-20', location='Tabernacle, Atlanta, Georgia')
        tourdate1.save()

        tourdate2 = Tourdate(date='2023-05-27', location='Kingston Mines, Chicago, Illinois')
        tourdate2.save()

        tourdate3 = Tourdate(date='2023-06-04', location='El Club, Detroit, Michigan')
        tourdate3.save()

        tourdate4 = Tourdate(date='2023-06-10', location='Stubbs, Austin, Texas')
        tourdate4.save()

        tourdate5 = Tourdate(date='2023-06-17', location='Kingston Mines, Chicago, Illinois')
        tourdate5.save()

add_tour_dates()