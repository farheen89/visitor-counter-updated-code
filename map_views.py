from django.shortcuts import render

from swk.HelloAnalytics import print_response, initialize_analyticsreporting, get_report

# Create your views here.

def Map(request):
   analytics = initialize_analyticsreporting()
   response = get_report(analytics)
   recd_response = print_response(response)
   context = {
      'Visitor_count': recd_response
   }
   return render(request,"map/map.html",context)      
 
