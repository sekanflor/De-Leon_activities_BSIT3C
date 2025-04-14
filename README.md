# Django User Authentication API

## API Documentation

---

### Register User  
**Method:** POST  
**Endpoint URL:** /api/register/

**Expected Request Body:**
json
{
  "username": "your_name",
  "email": "your_email@example.com",
  "password": "your_password"
}
Expected Headers:
Content-Type: application/json

Sample Response (Success):

{ "message": "User registered successfully" }
Sample Response (Error - Username already exists):

{ "error": "Username already exists" }
Sample Response (Error - Missing Fields):

{ "error": "Username, email, and password are required" }
Login User
Method: POST
Endpoint URL: /api/login/

Expected Request Body:
{ "username": "john_doe", "password": "your_password" }
Expected Headers:
Content-Type: application/json

Sample Response (Success):
{ "access": "your_access_token", "refresh": "your_refresh_token" }
Sample Response (Error - Invalid Credentials):

{ "detail": "No active account found with the given credentials" }
Protected Route (Requires Authentication)
Method: GET
Endpoint URL: /api/protected/

Expected Headers:
Authorization: Bearer <access_token>

Sample Response (Success):

{ "message": "You are authenticated" }
Sample Response (Error - Unauthorized):

{ "detail": "Authentication credentials were not provided" }
Token Refresh
Method: POST
Endpoint URL: /api/token/refresh/

Expected Request Body:

{ "refresh": "your_refresh_token" }
Expected Headers:
Content-Type: application/json

Sample Response (Success):

{ "access": "your_new_access_token" }
Sample Response (Error - Invalid Token):

{ "detail": "Token is invalid or expired" }
Steps to See if Your Credentials Are Authenticated (PowerShell)
Login or register using the /api/login/ or /api/register/ endpoint.

Copy your access token from the login response.

Open PowerShell and run the following:

powershell
$headers = @{ "Authorization" = "Bearer your_access_token_here" }
Invoke-WebRequest -Uri "http://localhost:8000/api/protected/" -Headers $headers
Expected Response:

plaintext
StatusCode        : 200
StatusDescription : OK
Content           : {"message":"You are authenticated"}

Requirements
Python 3.12
Django 5.1.6
Django REST Framework
