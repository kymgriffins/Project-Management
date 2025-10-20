# Construction Project Management API Documentation

## Overview

This comprehensive construction project management platform provides a unified real-time system that connects all stakeholders—architects, foremen, supervisors, contractors, and clients—throughout the entire construction lifecycle from planning to invoicing. The platform digitizes and streamlines construction operations, prevents costly rework, reduces material waste, and ensures project profitability.

## Base URL
```
/api/
```

## Authentication

The API uses JWT (JSON Web Token) authentication for secure access control.

### Authentication Endpoints

#### Register User
```http
POST /auth/register/
```

**Request Body:**
```json
{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secure_password123",
    "roles": [1]
}
```

**Response:**
```json
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "roles": [
        {
            "id": 1,
            "name": "architect",
            "permissions": []
        }
    ]
}
```

#### Get JWT Token
```http
POST /auth/token/
```

**Request Body:**
```json
{
    "email": "john@example.com",
    "password": "secure_password123"
}
```

**Response:**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

#### Refresh JWT Token
```http
POST /auth/token/refresh/
```

**Request Body:**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

## Project Management

### Projects

#### List All Projects
```http
GET /projects/
```

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response:**
```json
[
    {
        "id": 1,
        "client_name": "ABC Construction Ltd",
        "client_email": "client@abc.com",
        "coordinates": "40.7128,-74.0060",
        "topology": "Urban area with moderate elevation",
        "flora_fauna": "Minimal vegetation, urban environment",
        "accessibility": "Good road access, public transport nearby",
        "site_boundaries": "Property lines clearly marked",
        "utilities_availability": "All utilities available at site",
        "zoning_regulations": "Commercial zoning approved",
        "permits_approvals": "Building permit obtained",
        "safety_security": "Security fencing installed",
        "staging_storing": "Designated storage area allocated",
        "cultural_influences": "None significant",
        "local_contacts": "Local authorities notified",
        "current_phase": "designing",
        "name": "Downtown Office Complex",
        "description": "Modern 20-story office building",
        "location": "123 Main Street, City",
        "start_date": "2024-01-15",
        "end_date": "2025-06-30",
        "phases": "finishes",
        "current_budget": "1500000.00",
        "estimated_budget": "2000000.00",
        "supervisor": 2,
        "architect": 1,
        "foreman": 3,
        "created_at": "2024-01-15T10:30:00Z",
        "updated_at": "2024-01-20T14:45:00Z",
        "created_by": 1,
        "is_approved": true,
        "blueprints": [],
        "renders": [],
        "mep": [],
        "architecturals": [],
        "qs": [],
        "structurals": [],
        "legals": []
    }
]
```

#### Create New Project
```http
POST /projects/
```

**Request Body:**
```json
{
    "client_name": "XYZ Corporation",
    "client_email": "contact@xyz.com",
    "coordinates": "34.0522,-118.2437",
    "topology": "Coastal area with slight slope",
    "current_phase": "designing",
    "name": "Residential Tower Project",
    "description": "Luxury residential complex",
    "location": "456 Ocean Drive, Beach City",
    "start_date": "2024-03-01",
    "end_date": "2025-12-31",
    "phases": "designing",
    "estimated_budget": "5000000.00",
    "supervisor": 2,
    "architect": 1,
    "foreman": 3,
    "created_by": 1
}
```

#### Get Project Details
```http
GET /project/{id}/
```

#### Update Project
```http
PUT /project/{id}/
PATCH /project/{id}/
```

#### Delete Project
```http
DELETE /project/{id}/
```

#### Get Project Daily Records
```http
GET /projectsrecords/{id}/
```

**Response:**
```json
[
    {
        "id": 1,
        "project": 1,
        "date": "2024-01-15",
        "work_completed": "Foundation excavation completed",
        "work_planned": "Foundation pouring scheduled",
        "issues": "Weather delay due to rain",
        "workers_pay": "2500.00",
        "total_spendings": "5000.00",
        "materials": [],
        "documents": [],
        "created_at": "2024-01-15T18:00:00Z",
        "updated_at": "2024-01-15T18:00:00Z",
        "is_achieved": false
    }
]
```

## Daily Records Management

### Daily Records

#### List All Daily Records
```http
GET /dailyrecords/
```

#### Create Daily Record
```http
POST /dailyrecords/
```

**Request Body:**
```json
{
    "project": 1,
    "work_completed": "Concrete foundation poured",
    "work_planned": "Steel frame installation",
    "issues": "Material delivery delayed",
    "workers_pay": "3200.00",
    "total_spendings": "8500.00"
}
```

#### Get/Update/Delete Daily Record
```http
GET /dailyrecord/{id}/
PUT /dailyrecord/{id}/
PATCH /dailyrecord/{id}/
DELETE /dailyrecord/{id}/
```

## Material Management

### Materials

#### List All Materials
```http
GET /materials/
```

**Response:**
```json
[
    {
        "id": 1,
        "name": "Reinforced Concrete",
        "description": "High-strength concrete with steel reinforcement",
        "unit_cost": "150.00",
        "unit": "cubic meter"
    },
    {
        "id": 2,
        "name": "Steel Beams",
        "description": "Structural steel beams for framework",
        "unit_cost": "800.00",
        "unit": "ton"
    }
]
```

#### Create Material
```http
POST /materials/
```

**Request Body:**
```json
{
    "name": "Aluminum Windows",
    "description": "Energy-efficient aluminum window frames",
    "unit_cost": "450.00",
    "unit": "piece"
}
```

#### Get/Update/Delete Material
```http
GET /material/{id}/
PUT /material/{id}/
PATCH /material/{id}/
DELETE /material/{id}/
```

### Material Usage

#### List Material Usage Records
```http
GET /material/used/
```

#### Create Material Usage Record
```http
POST /material/used/
```

**Request Body:**
```json
{
    "material": 1,
    "daily_record": 1,
    "quantity_used": "25.5"
}
```

#### Get/Update/Delete Material Usage
```http
GET /material/used/{id}/
PUT /material/used/{id}/
PATCH /material/used/{id}/
DELETE /material/used/{id}/
```

## Task Management

### Todos/Tasks

#### List All Tasks
```http
GET /todos/
```

**Response:**
```json
[
    {
        "id": 1,
        "title": "Complete Foundation Inspection",
        "assigned_to": [2, 3],
        "due_date": "2024-01-25T10:00:00Z",
        "tags": "high",
        "description": "Final inspection of foundation before proceeding to next phase",
        "project": 1,
        "created_at": "2024-01-20T09:00:00Z",
        "isComplete": false,
        "isDeleted": false,
        "comments": [],
        "budget": "5000.00",
        "companyearnings": "15000.00",
        "facilitation": "2000.00",
        "labour": "8000.00",
        "notes": "Requires structural engineer approval",
        "spendings": "12000.00"
    }
]
```

#### Create Task
```http
POST /todos/
```

**Request Body:**
```json
{
    "title": "Install Electrical Systems",
    "assigned_to": [4, 5],
    "due_date": "2024-02-15T16:00:00Z",
    "tags": "site",
    "description": "Complete electrical installation for floors 1-5",
    "project": 1,
    "budget": "25000.00",
    "labour": "15000.00"
}
```

#### Get/Update/Delete Task
```http
GET /todos/{id}/
PUT /todos/{id}/
PATCH /todos/{id}/
DELETE /todos/{id}/
```

## Document Management

### Blueprints

#### List/Upload Blueprints
```http
GET /blueprint/
POST /blueprint/
```

**Upload Request (multipart/form-data):**
```
image: [file]
project: 1
```

### Renders

#### List/Upload Renders
```http
GET /renders/
POST /renders/
```

#### Get/Update/Delete Render
```http
GET /renders/{id}/
PUT /renders/{id}/
PATCH /renders/{id}/
DELETE /renders/{id}/
```

### MEP (Mechanical, Electrical, Plumbing)

#### List/Upload MEP Documents
```http
GET /mep/
POST /mep/
```

#### Get/Update/Delete MEP Document
```http
GET /mep/{id}/
PUT /mep/{id}/
PATCH /mep/{id}/
DELETE /mep/{id}/
```

### Structural Documents

#### List/Upload Structural Documents
```http
GET /structurals/
POST /structurals/
```

#### Get/Update/Delete Structural Document
```http
GET /structurals/{id}/
PUT /structurals/{id}/
PATCH /structurals/{id}/
DELETE /structurals/{id}/
```

### Quantity Survey (QS) Documents

#### List/Upload QS Documents
```http
GET /qs/
POST /qs/
```

#### Get/Update/Delete QS Document
```http
GET /qs/{id}/
PUT /qs/{id}/
PATCH /qs/{id}/
DELETE /qs/{id}/
```

### Architectural Documents

#### List/Upload Architectural Documents
```http
GET /architecturals/
POST /architecturals/
```

#### Get/Update/Delete Architectural Document
```http
GET /architecturals/{id}/
PUT /architecturals/{id}/
PATCH /architecturals/{id}/
DELETE /architecturals/{id}/
```

### Legal Documents

#### List/Upload Legal Documents
```http
GET /legals/
POST /legals/
```

#### Get/Update/Delete Legal Document
```http
GET /legals/{id}/
PUT /legals/{id}/
PATCH /legals/{id}/
DELETE /legals/{id}/
```

### Record Pictures

#### List/Upload Record Pictures
```http
GET /record_pic/
POST /record_pic/
```

## Invoice Management

### Invoices

#### List All Invoices
```http
GET /invoices/
```

**Response:**
```json
[
    {
        "id": 1,
        "project": 1,
        "amount": "50000.00",
        "is_paid": false,
        "invoices": [
            {
                "id": 1,
                "item_type": "material",
                "content": "",
                "materials": {
                    "id": 1,
                    "name": "Reinforced Concrete",
                    "description": "High-strength concrete with steel reinforcement",
                    "unit_cost": "150.00",
                    "unit": "cubic meter"
                },
                "quantity": 100,
                "amount": "15000.00"
            },
            {
                "id": 2,
                "item_type": "text",
                "content": "Labor charges for foundation work",
                "materials": null,
                "quantity": 1,
                "amount": "35000.00"
            }
        ],
        "date_created": "2024-01-20T10:00:00Z",
        "created_by": 1,
        "name": "ABC Construction Ltd",
        "phone": "+1-555-0123",
        "email": "billing@abc.com"
    }
]
```

#### Create Invoice
```http
POST /invoices/
```

**Request Body:**
```json
{
    "project": 1,
    "amount": "75000.00",
    "created_by": 1,
    "name": "XYZ Corporation",
    "phone": "+1-555-0456",
    "email": "billing@xyz.com",
    "invoices": [1, 2, 3]
}
```

#### Get/Update/Delete Invoice
```http
GET /invoices/{id}/
PUT /invoices/{id}/
PATCH /invoices/{id}/
DELETE /invoices/{id}/
```

### Invoice Items

#### List All Invoice Items
```http
GET /invoice-items/
```

#### Create Invoice Item
```http
POST /invoice-items/
```

**Request Body:**
```json
{
    "item_type": "material",
    "content": "",
    "materials": 1,
    "quantity": 50,
    "amount": "7500.00"
}
```

## Communication

### Comments

#### List All Comments
```http
GET /comments/
```

#### Create Comment
```http
POST /comments/
```

**Request Body:**
```json
{
    "user": 1,
    "comment": "Foundation work completed successfully. Ready for next phase."
}
```

#### Get/Update/Delete Comment
```http
GET /comment/{id}/
PUT /comment/{id}/
PATCH /comment/{id}/
DELETE /comment/{id}/
```

## Building Information

### Buildings

#### List/Create Buildings
```http
GET /building/
POST /building/
```

**Request Body:**
```json
{
    "floors": 20,
    "square_feet": "150000.00",
    "owner": 1,
    "project": 1
}
```

## Project Phases

The system supports the following project phases:

- **designing**: Initial design phase
- **approvals**: Regulatory approvals and permits
- **ground_breaking**: Site preparation and excavation
- **substructure**: Foundation and basement construction
- **superstructure**: Main building structure
- **finishes**: Interior and exterior finishing
- **handing_over**: Project completion and handover

## Task Tags

Tasks can be categorized with the following tags:

- **team**: Team-related tasks
- **low**: Low priority tasks
- **high**: High priority tasks
- **site**: On-site tasks

## Payment Status

Payment records can have the following statuses:

- **received**: Payment received
- **pending**: Payment pending
- **overdue**: Payment overdue

## Error Responses

### Common Error Codes

- **400 Bad Request**: Invalid request data
- **401 Unauthorized**: Authentication required
- **403 Forbidden**: Insufficient permissions
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server error

### Error Response Format
```json
{
    "error": "Error message description",
    "details": {
        "field_name": ["Specific field error"]
    }
}
```

## Rate Limiting

API requests are rate-limited to prevent abuse. Current limits:
- **Authentication endpoints**: 5 requests per minute
- **General endpoints**: 100 requests per hour

## Webhooks

The API supports webhooks for real-time notifications:

- **Project phase changes**
- **Task completion**
- **Payment status updates**
- **Document uploads**

## SDK and Integration

### Python SDK Example
```python
import requests

class ConstructionAPI:
    def __init__(self, base_url, access_token):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

    def get_projects(self):
        response = requests.get(f'{self.base_url}/projects/', headers=self.headers)
        return response.json()

    def create_daily_record(self, project_id, data):
        data['project'] = project_id
        response = requests.post(
            f'{self.base_url}/dailyrecords/',
            json=data,
            headers=self.headers
        )
        return response.json()

# Usage
api = ConstructionAPI('https://api.construction-mgmt.com', 'your_access_token')
projects = api.get_projects()
```

### JavaScript SDK Example
```javascript
class ConstructionAPI {
    constructor(baseUrl, accessToken) {
        this.baseUrl = baseUrl;
        this.headers = {
            'Authorization': `Bearer ${accessToken}`,
            'Content-Type': 'application/json'
        };
    }

    async getProjects() {
        const response = await fetch(`${this.baseUrl}/projects/`, {
            headers: this.headers
        });
        return await response.json();
    }

    async createDailyRecord(projectId, data) {
        const response = await fetch(`${this.baseUrl}/dailyrecords/`, {
            method: 'POST',
            headers: this.headers,
            body: JSON.stringify({ ...data, project: projectId })
        });
        return await response.json();
    }
}

// Usage
const api = new ConstructionAPI('https://api.construction-mgmt.com', 'your_access_token');
const projects = await api.getProjects();
```

## Support and Contact

For API support and integration assistance:
- **Email**: api-support@construction-mgmt.com
- **Documentation**: https://docs.construction-mgmt.com
- **Status Page**: https://status.construction-mgmt.com

## Changelog

### Version 1.0.0 (Current)
- Initial API release
- Full CRUD operations for all entities
- JWT authentication
- File upload support
- Real-time project tracking
- Comprehensive document management
- Invoice and payment tracking
- Task management system
