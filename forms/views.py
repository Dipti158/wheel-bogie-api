


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db import transaction
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from .models import WheelSpecification, BogieChecksheet
from .serializers import (
    WheelSpecificationCreateSerializer,
    WheelSpecificationSerializer,
    BogieChecksheetCreateSerializer,
    BogieChecksheetSerializer
)

class WheelSpecificationAPIView(APIView):
    """
    API for managing Wheel Specifications
    """
    
    @extend_schema(
        request=WheelSpecificationCreateSerializer,
        responses={201: WheelSpecificationSerializer},
        description="Create a new wheel specification form"
    )
    def post(self, request):

        """Create a new wheel specification"""
        try:
            with transaction.atomic():
                serializer = WheelSpecificationCreateSerializer(data=request.data)
                
                if serializer.is_valid():
                    wheel_spec = serializer.save()
                    
                    response_data = {
                        "success": True,
                        "message": "Wheel specification submitted successfully.",
                        "data": {
                            "formNumber": wheel_spec.form_number,
                            "submittedBy": wheel_spec.submitted_by,
                            "submittedDate": wheel_spec.submitted_date.strftime('%Y-%m-%d'),
                            "status": wheel_spec.status
                        }
                    }
                    
                    return Response(response_data, status=status.HTTP_201_CREATED)
                
                else:
                    return Response({
                        "success": False,
                        "message": "Validation failed",
                        "errors": serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
                    
        except Exception as e:
            return Response({
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @extend_schema(
        parameters=[
            OpenApiParameter("formNumber", OpenApiTypes.STR, description="Filter by form number"),
            OpenApiParameter("submittedBy", OpenApiTypes.STR, description="Filter by submitted by"),
            OpenApiParameter("submittedDate", OpenApiTypes.DATE, description="Filter by submitted date"),
        ],
        responses={200: WheelSpecificationSerializer(many=True)},
        description="Get wheel specifications with optional filters"
    )
    def get(self, request):
        """Get wheel specifications with optional filters"""
        try:
            queryset = WheelSpecification.objects.all()
            
            # Apply filters
            form_number = request.query_params.get('formNumber')
            submitted_by = request.query_params.get('submittedBy')
            submitted_date = request.query_params.get('submittedDate')
            
            if form_number:
                queryset = queryset.filter(form_number=form_number)
            if submitted_by:
                queryset = queryset.filter(submitted_by=submitted_by)
            if submitted_date:
                queryset = queryset.filter(submitted_date__date=submitted_date)
            
            serializer = WheelSpecificationSerializer(queryset, many=True)
            
            response_data = {
                "success": True,
                "message": "Filtered wheel specification forms fetched successfully.",
                "data": serializer.data
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BogieChecksheetAPIView(APIView):
    """
    API for managing Bogie Checksheets
    """
    
    @extend_schema(
        request=BogieChecksheetCreateSerializer,
        responses={201: BogieChecksheetSerializer},
        description="Create a new bogie checksheet form"
    )
    def post(self, request):
        """Create a new bogie checksheet"""
        try:
            with transaction.atomic():
                serializer = BogieChecksheetCreateSerializer(data=request.data)
                
                if serializer.is_valid():
                    bogie_checksheet = serializer.save()
                    
                    response_data = {
                        "success": True,
                        "message": "Bogie checksheet submitted successfully.",
                        "data": {
                            "formNumber": bogie_checksheet.form_number,
                            "inspectionBy": bogie_checksheet.inspection_by,
                            "inspectionDate": bogie_checksheet.inspection_date.strftime('%Y-%m-%d'),
                            "status": bogie_checksheet.status
                        }
                    }
                    
                    return Response(response_data, status=status.HTTP_201_CREATED)
                
                else:
                    return Response({
                        "success": False,
                        "message": "Validation failed",
                        "errors": serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
                    
        except Exception as e:
            return Response({
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @extend_schema(
        parameters=[
            OpenApiParameter("formNumber", OpenApiTypes.STR, description="Filter by form number"),
            OpenApiParameter("inspectionBy", OpenApiTypes.STR, description="Filter by inspection by"),
            OpenApiParameter("inspectionDate", OpenApiTypes.DATE, description="Filter by inspection date"),
        ],
        responses={200: BogieChecksheetSerializer(many=True)},
        description="Get bogie checksheets with optional filters"
    )
    def get(self, request):
        """Get bogie checksheets with optional filters"""
        try:
            queryset = BogieChecksheet.objects.all()
            
            # Apply filters
            form_number = request.query_params.get('formNumber')
            inspection_by = request.query_params.get('inspectionBy')
            inspection_date = request.query_params.get('inspectionDate')
            
            if form_number:
                queryset = queryset.filter(form_number=form_number)
            if inspection_by:
                queryset = queryset.filter(inspection_by=inspection_by)
            if inspection_date:
                queryset = queryset.filter(inspection_date__date=inspection_date)
            
            serializer = BogieChecksheetSerializer(queryset, many=True)
            
            response_data = {
                "success": True,
                "message": "Filtered bogie checksheet forms fetched successfully.",
                "data": serializer.data
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    
    
