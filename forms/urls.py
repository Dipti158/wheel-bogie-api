
from django.urls import path
from .views import WheelSpecificationAPIView, BogieChecksheetAPIView

app_name = 'forms'

urlpatterns = [
   
    
    # Wheel specifications
    path('api/forms/wheel-specifications/', 
         WheelSpecificationAPIView.as_view(), 
         name='wheel_specifications'),
    
    # Bogie checksheets
    path('api/forms/bogie-checksheet/', 
         BogieChecksheetAPIView.as_view(), 
         name='bogie_checksheet'),
]