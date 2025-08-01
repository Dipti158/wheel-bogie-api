
from rest_framework import serializers
from .models import WheelSpecification, BogieChecksheet
from datetime import datetime

class WheelSpecFieldsSerializer(serializers.Serializer):

    """Serializer for wheel specification fields"""

    treadDiameterNew = serializers.CharField(max_length=100)
    lastShopIssueSize = serializers.CharField(max_length=100)
    condemningDia = serializers.CharField(max_length=100)
    wheelGauge = serializers.CharField(max_length=100)
    variationSameAxle = serializers.CharField(max_length=50)
    variationSameBogie = serializers.CharField(max_length=50)
    variationSameCoach = serializers.CharField(max_length=50)
    wheelProfile = serializers.CharField(max_length=100)
    intermediateWWP = serializers.CharField(max_length=100)
    bearingSeatDiameter = serializers.CharField(max_length=100)
    rollerBearingOuterDia = serializers.CharField(max_length=100)
    rollerBearingBoreDia = serializers.CharField(max_length=100)
    rollerBearingWidth = serializers.CharField(max_length=100)
    axleBoxHousingBoreDia = serializers.CharField(max_length=100)
    wheelDiscWidth = serializers.CharField(max_length=100)

class WheelSpecificationCreateSerializer(serializers.Serializer):

    """Serializer for creating wheel specifications"""

    formNumber = serializers.CharField(max_length=50)
    submittedBy = serializers.CharField(max_length=100)
    submittedDate = serializers.CharField()  # Will be parsed as date
    fields = WheelSpecFieldsSerializer()
    
    def validate_formNumber(self, value):

        """Check if form number already exists"""
        if WheelSpecification.objects.filter(form_number=value).exists():
            raise serializers.ValidationError("Form number already exists")
        return value
    
    def validate_submittedDate(self, value):

        """Validate and parse submitted date"""
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()

        except ValueError:
            raise serializers.ValidationError("Invalid date format. Use YYYY-MM-DD")
    
    def create(self, validated_data):

        """Create a new wheel specification"""
        fields_data = validated_data.pop('fields')
        
        wheel_spec = WheelSpecification.objects.create(
            form_number=validated_data['formNumber'],
            submitted_by=validated_data['submittedBy'],
            submitted_date=validated_data['submittedDate'],
            fields=fields_data
        )
        return wheel_spec

class WheelSpecificationSerializer(serializers.ModelSerializer):

    """Serializer for wheel specification model"""

    formNumber = serializers.CharField(source='form_number')
    submittedBy = serializers.CharField(source='submitted_by')
    submittedDate = serializers.DateTimeField(source='submitted_date', format='%Y-%m-%d')
    
    class Meta:
        model = WheelSpecification
        fields = ['formNumber', 'submittedBy', 'submittedDate', 'fields', 'status']

class BogieDetailsSerializer(serializers.Serializer):

    """Serializer for bogie details"""

    bogieNo = serializers.CharField(max_length=50)
    makerYearBuilt = serializers.CharField(max_length=100)
    incomingDivAndDate = serializers.CharField(max_length=100)
    deficitComponents = serializers.CharField(max_length=200)
    dateOfIOH = serializers.CharField()

class BogieChecksheetFieldsSerializer(serializers.Serializer):

    """Serializer for bogie checksheet fields"""

    bogieFrameCondition = serializers.CharField(max_length=50)
    bolster = serializers.CharField(max_length=50)
    bolsterSuspensionBracket = serializers.CharField(max_length=50)
    lowerSpringSeat = serializers.CharField(max_length=50)
    axleGuide = serializers.CharField(max_length=50)

class BMBCChecksheetSerializer(serializers.Serializer):

    cylinderBody = serializers.CharField(max_length=50)
    pistonTrunnion = serializers.CharField(max_length=50)
    adjustingTube = serializers.CharField(max_length=50)
    plungerSpring = serializers.CharField(max_length=50)

class BogieChecksheetCreateSerializer(serializers.Serializer):

    """Serializer for creating bogie checksheets"""

    formNumber = serializers.CharField(max_length=50)
    inspectionBy = serializers.CharField(max_length=100)
    inspectionDate = serializers.CharField()
    bogieDetails = BogieDetailsSerializer()
    bogieChecksheet = BogieChecksheetFieldsSerializer()
    bmbcChecksheet = BMBCChecksheetSerializer()
    
    def validate_formNumber(self, value):
        """Check if form number already exists"""
        if BogieChecksheet.objects.filter(form_number=value).exists():
            raise serializers.ValidationError("Form number already exists")
        return value
    
    def validate_inspectionDate(self, value):
        """Validate and parse inspection date"""
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            raise serializers.ValidationError("Invalid date format. Use YYYY-MM-DD")
    
    def create(self, validated_data):

    
        """Create a new bogie checksheet"""
        bogie_details = validated_data.pop('bogieDetails')
        bogie_checksheet = validated_data.pop('bogieChecksheet')
        bmbc_checksheet = validated_data.pop('bmbcChecksheet')
        
        bogie = BogieChecksheet.objects.create(
            form_number=validated_data['formNumber'],
            inspection_by=validated_data['inspectionBy'],
            inspection_date=validated_data['inspectionDate'],
            bogie_details=bogie_details,
            bogie_checksheet=bogie_checksheet,
            bmbc_checksheet=bmbc_checksheet
        )
        return bogie

class BogieChecksheetSerializer(serializers.ModelSerializer):
    """Serializer for bogie checksheet model"""
    formNumber = serializers.CharField(source='form_number')
    inspectionBy = serializers.CharField(source='inspection_by')
    inspectionDate = serializers.DateTimeField(source='inspection_date', format='%Y-%m-%d')
    
    class Meta:
        model = BogieChecksheet
        fields = ['formNumber', 'inspectionBy', 'inspectionDate', 
                 'bogie_details', 'bogie_checksheet', 'bmbc_checksheet', 'status']


 