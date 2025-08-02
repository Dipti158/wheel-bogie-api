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
   git clone <your-repository-url>
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

4. **Set up PostgreSQL Database**
   
   **Option A: Create database manually**
   ```sql
   CREATE DATABASE kpa_db;
   ```
   
   **Option B: Use existing database**
   - Ensure PostgreSQL is running
  
     

5. **Create environment variables file**
   Create a `.env` file in the project root:
   ```env
   # Database Configuration
   DB_NAME=kpa_db
   DB_USER=postgres
   DB_PASSWORD=your_password_here
   DB_HOST=localhost
   DB_PORT=5432
   
   # Django Configuration
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   
   # CORS Configuration
   CORS_ALLOW_ALL_ORIGINS=True
   ```

6. **Configure database settings**
   Verify your `settings.py` contains:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': os.getenv('DB_NAME', 'kpa_db'),
           'USER': os.getenv('DB_USER', 'postgres'),
           'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
           'HOST': os.getenv('DB_HOST', 'localhost'),
           'PORT': os.getenv('DB_PORT', '5432'),
       }
   }
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
         "rimThickness": "32 mm",
        "materialType": "Forged Steel",
        "axleSize": "120 mm",
        "brakeDiscType": "Solid",
        "treadDiameterNew": "915 (900-1000)",
        "lastShopIssueSize": "837 (800-900)",
        "wheelMaterial": "Alloy Steel",
        "rimType": "Flat Rim",
        "inspectionDate": "2025-06-30",
        "inspectedBy": "Inspector_456",
        "remarks": "Slight wear on outer edge, within tolerance",
        "location": "Assembly Line 3"
      },
      "status": "SAVED"
    }
  ]
}
```

### 2. Bogie Checksheet API

**Endpoint**: `/api/forms/bogie-checksheet/`

#### POST - Create Bogie Checksheet
Creates a new bogie checksheet form.

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


## Limitations

1. **Authentication**: Currently not implemented
2. **Validation**: Limited field validation 
3. **File Uploads**: No supported
4. **Search**: Basic query parameter filtering only





## Postman Collection

This project includes a complete Postman collection for testing the implemented APIs.

`KPA_form data API.postman_collection`

### How to Use
1. Open **Postman**.
2. Click **Import**.
3. Select the file `KPA_form data API.postman_collection` from the root of this project.
4. You'll see grouped API requests.

