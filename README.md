### KPA Form Data API

This project is a Django Rest Framework (DRF) API that lets users submit and view KPA inspection form data. It uses PostgreSQL as the database. The API can be tested through Postman or Swagger UI.

### Tech Stack Used

- Python – Programming Language

- Django – Web Framework

- Django REST Framework – For building REST APIs

- DRF Spectacular – For Swagger documentation

- PostgreSQL – Database

- Swagger UI – API testing and visualization

  

### Setup Instructions

1. Clone the repository  
```bash
git clone https://github.com/yourusername/yourproject.git


# KPA Form Data API

A Django REST Framework-based API for managing railway wheel specifications and bogie checksheet forms. This system provides endpoints for creating, retrieving, and managing technical inspection data for railway components.

## Technologies & Tech Stack

- **Backend Framework**: Django 4.x with Django REST Framework (DRF)
- **Python Version**: Python 3.13.5
- **Web Server**: WSGIServer (Development)
- **API Documentation**: drf-spectacular (OpenAPI/Swagger)
- **Database**: Django ORM (SQLite by default, configurable)
- **Authentication**: Django's built-in authentication system
- **API Format**: JSON REST API

## Setup Instructions

### Prerequisites
- Python 3.13.5 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd kpa-form-data-api
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   pip install djangorestframework
   pip install drf-spectacular
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - API Base URL: `http://localhost:8000/`
   - Admin Panel: `http://localhost:8000/admin/`
   - API Documentation: `http://localhost:8000/api/docs/`
   - ReDoc Documentation: `http://localhost:8000/api/redoc/`

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

**Query Parameters**:
- `formNumber`: Filter by form number
- `submittedBy`: Filter by submitter
- `submittedDate`: Filter by submission date

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

### 3. API Documentation Endpoints

- **OpenAPI Schema**: `/api/schema/`
- **Swagger UI**: `/api/docs/`
- **ReDoc**: `/api/redoc/`

## Response Headers

All API responses include standard security headers:
- `X-Frame-Options: DENY`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: same-origin`
- `Cross-Origin-Opener-Policy: same-origin`

## Data Models

### Wheel Specification Fields
- **Technical Measurements**: Tread diameter, bearing dimensions, wheel gauge
- **Tolerance Specifications**: Various dimensional tolerances and variations
- **Metadata**: Form number, submitter, submission date

### Bogie Checksheet Structure
- **Bogie Details**: Bogie number, IOH date, maker information
- **Inspection Data**: Component conditions and status
- **BMBC Checksheet**: Brake cylinder inspection details

## Limitations & Assumptions

### Limitations
1. **Authentication**: Currently uses basic Django authentication - no token-based auth implemented
2. **Validation**: Limited field validation beyond basic type checking
3. **File Uploads**: No support for attachment uploads (images, documents)
4. **Pagination**: No built-in pagination for large datasets
5. **Search**: Basic filtering only - no full-text search capabilities
6. **Audit Trail**: No comprehensive logging of form modifications
7. **Notifications**: No automated notification system for form submissions

### Assumptions
1. **Data Format**: All dimensional data stored as strings with tolerance information
2. **User Management**: Users are managed through Django admin interface
3. **Form Numbers**: Assumed to follow specific naming conventions (e.g., "WHEEL-2025-XXX")
4. **Status Field**: All forms default to "SAVED" status
5. **Date Format**: ISO date format (YYYY-MM-DD) expected for all date fields
6. **Component Conditions**: Predefined set of condition values ("Good", "Worn", "Damaged", etc.)
7. **Single Database**: Designed for single-instance deployment
8. **Synchronous Processing**: All operations are synchronous - no background job processing

### Technical Assumptions
- SQLite database sufficient for current scale
- Single-server deployment model
- UTF-8 encoding for all text data
- JSON content-type for all API communications
- CORS not configured (same-origin policy applies)

## Future Enhancements

- Implement JWT authentication
- Add comprehensive input validation
- Include file upload capabilities
- Add pagination and advanced search
- Implement real-time notifications
- Add comprehensive audit logging
- Support for multi-language content

## Testing

Use the provided Postman collection (`KPA_form data API.postman_collection`) to test all endpoints. The collection includes:
- Sample POST requests with valid data
- GET requests with filtering examples
- Expected response formats

## Support

For technical support or questions about the API, please contact the development team or refer to the API documentation at `/api/docs/`.




