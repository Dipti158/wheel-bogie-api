### KPA Form Data API

This project is a Django Rest Framework (DRF) API that lets users submit and view KPA form data. It uses PostgreSQL as the database. The API can be tested through Postman or Swagger UI.

### Tech Stack Used

- Python – Programming Language

- Django – Web Framework

- Django REST Framework – For building REST APIs

- DRF Spectacular – For Swagger documentation

- PostgreSQL – Database

- Swagger UI – API testing and visualization


## Setup Instructions

### Prerequisites
- Python 3.13.5 or higher
- pip (Python package installer)
- Virtual environment 
- Postman

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
    pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - API Base URL: `http://localhost:8000/`
   - Admin Panel: `http://localhost:8000/admin/`
   - API Documentation: `http://localhost:8000/api/docs/`

## API Endpoints

### 1. Wheel Specifications API

**Endpoint**: `/api/forms/wheel-specifications/`

**Methods**: `GET`, `POST`, `HEAD`, `OPTIONS`

#### POST - Create Wheel Specification
Creates a new wheel specification form entry.

**Request Body**:
```json
{
  "formNumber": "WHEEL-2025-005",
  "submittedBy": "Dipti",
  "submittedDate": "2025-07-30",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "lastShopIssueSize": "837 (800-900)",
    "condemningDia": "825 (800-900)",
    "wheelGauge": "1600 (+2,-1)",
    "variationSameAxle": "0.5",
    "variationSameBogie": "5",
    "variationSameCoach": "13",
    "wheelProfile": "29.4 Flange Thickness",
    "intermediateWWP": "20 TO 28",
    "bearingSeatDiameter": "130.043 TO 130.068",
    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
    "rollerBearingWidth": "93 (+0/-0.250)",
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "wheelDiscWidth": "127 (+4/-0)"
  }
}
```

**Response** (201 Created):
```json
{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-005",
    "submittedBy": "Dipti",
    "submittedDate": "2025-07-30",
    "status": "SAVED"
  }
}
```

#### GET - Retrieve Wheel Specifications
Retrieves wheel specification forms with optional filtering.

**Example**: `/api/forms/wheel-specifications/?formNumber=WHEEL-2025-001&submittedBy=user_id_123&submittedDate=2025-07-03`

**Response** (200 OK):
```json
{
  "success": true,
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "wheelGauge": "1600 (+2,-1)",
        "wheelProfile": "29.4 Flange Thickness",
        // ... other fields
      },
      "status": "SAVED"
    }
  ]
}
```

### 2. Bogie Checksheet API

**Endpoint**: `/api/forms/bogie-checksheet/`

**Methods**: `GET`, `POST`, `HEAD`, `OPTIONS`

#### POST - Create Bogie Checksheet
Creates a new bogie checksheet inspection form.

**Request Body**:
```json
{
  "formNumber": "B01",
  "submittedBy": "Dipti",
  "submittedDate": "2025-07-30",
  "inspectionBy": "Inspector Name",
  "inspectionDate": "2025-07-30",
  "bogieDetails": {
    "bogieNo": "BG123",
    "dateOfIOH": "2025-07-20",
    "deficitComponents": "None",
    "incomingDivAndDate": "WR/2025-07-19",
    "makerYearBuilt": "BEML/2018"
  },
  "bogieChecksheet": {
    "axleGuide": "Good",
    "bogieFrameCondition": "Good",
    "bolster": "OK",
    "bolsterSuspensionBracket": "Intact",
    "lowerSpringSeat": "New"
  },
  "bmbcChecksheet": {
    "adjustingTube": "Tight",
    "cylinderBody": "No damage",
    "pistonTrunnion": "Smooth",
    "plungerSpring": "New"
  }
}
```

**Response** (201 Created):
```json
{
  "success": true,
  "message": "Bogie checksheet submitted successfully.",
  "data": {
    "formNumber": "BOGIE-2025-003",
    "inspectionBy": "user_id_456",
    "inspectionDate": "2025-07-03",
    "status": "SAVED"
  }
}
```

#### GET - Retrieve Bogie Checksheets
Retrieves bogie checksheet forms with optional filtering.

**Response** (200 OK):
```json
{
  "success": true,
  "message": "Filtered bogie checksheet forms fetched successfully.",
  "data": [
    {
      "formNumber": "BOGIE-2025-004",
      "inspectionBy": "user_id_456",
      "inspectionDate": "2025-07-03",
      "bogie_details": {
        "bogieNo": "BG1234",
        "dateOfIOH": "2025-07-01",
        "makerYearBuilt": "RDSO/2018",
        "deficitComponents": "None",
        "incomingDivAndDate": "NR / 2025-06-25"
      },
      "bogie_checksheet": {
        "bolster": "Good",
        "axleGuide": "Worn",
        "lowerSpringSeat": "Good",
        "bogieFrameCondition": "Good",
        "bolsterSuspensionBracket": "Cracked"
      },
      "bmbc_checksheet": {
        "cylinderBody": "WORN OUT",
        "adjustingTube": "DAMAGED",
        "plungerSpring": "GOOD",
        "pistonTrunnion": "GOOD"
      },
      "status": "SAVED"
    }
  ]
}
```

## Limitations & Assumptions

### Limitations
1. **Authentication**: Currently no auth implemented
2. **Validation**: Limited field validation 
3. **File Uploads**: No support for attachment uploads (images, documents)
4. **Search**: Basic filtering only 









