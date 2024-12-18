# Vishal_Admin_Dashboard_Using_Django

# COMPANY_API

This project is an **Admin Dashboard** built using **Django**, with a focus on providing RESTful API services and leveraging **SQLite3** as the database. It offers functionalities to manage and monitor administrative tasks efficiently.

## Features

- Admin dashboard for managing and monitoring data.
- RESTful APIs for seamless interaction with data.
- User authentication and authorization.
- Lightweight database setup using SQLite3.
- Custom admin interface for managing:
  - **Companies**
  - **Employees**
  - **Groups**
  - **Users**

## Technologies Used

- **Django**: Backend framework for rapid development.
- **Django REST Framework (DRF)**: To build and consume RESTful APIs.
- **SQLite3**: Database for data storage and retrieval.

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd COMPANY_API
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Admin Dashboard

The custom admin dashboard includes the following sections:

1. **API Management**:
   - **Companies**: Add, view, and manage company-related data.
   - **Employees**: Add, view, and manage employee records.

2. **Authentication and Authorization**:
   - **Groups**: Manage user groups.
   - **Users**: Add, view, and manage user accounts.

### Admin Access

To access the admin dashboard:
- Visit: `http://127.0.0.1:8000/admin/`
- Use your superuser credentials (created during setup):
   ```bash
   python manage.py createsuperuser
   ```

## API Endpoints

The project exposes several REST API endpoints. Below are examples of typical endpoints:

- **Authentication**:
  - `POST /api/token/`: Obtain a JWT token.
  - `POST /api/token/refresh/`: Refresh the JWT token.

- **Resources**:
  - `GET /api/companies/`: Fetch a list of companies.
  - `POST /api/companies/`: Create a new company.
  - `GET /api/employees/`: Fetch a list of employees.
  - `POST /api/employees/`: Create a new employee.

Refer to the API documentation or browse through the source code for more details on available endpoints.

## Usage

- **Admin Panel**: Access the admin dashboard at `/admin/`.
- **API Testing**: Use tools like Postman or cURL to test the REST API endpoints.

## Project Structure

- **app/**: Main application directory containing core functionality.
- **templates/**: HTML templates for the frontend (if any).
- **db.sqlite3**: SQLite3 database file.
- **manage.py**: Django management script.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## View Of Web

### Admin_Dashboard
![Admin_Dashboard](https://github.com/Vishal3550/Vishal_Admin_Dashboard_Using_Django/blob/main/Admin_Dashboard_1.png)

### Select_Company_To_Change
![Select_Company_To_Change](https://github.com/Vishal3550/Vishal_Admin_Dashboard_Using_Django/blob/main/Select_Comp_Change_2.png)

### Change_Company
![Change_Company](https://github.com/Vishal3550/Vishal_Admin_Dashboard_Using_Django/blob/main/Change_Comp_3.png)

### Select_Emp_To_Change
![Select_Emp_To_Change](https://github.com/Vishal3550/Vishal_Admin_Dashboard_Using_Django/blob/main/Select_Emp_Change_4.png)

### Change_Emp
![Change_Emp](https://github.com/Vishal3550/Vishal_Admin_Dashboard_Using_Django/blob/main/Change_Emp_5.png)

### Select_Grp_To_Change
![Select_Grp_To_Change](https://github.com/Vishal3550/Vishal_Admin_Dashboard_Using_Django/blob/main/Select_Grp_Change_6.png)

### Select_User_To_Change
![Select_User_To_Change](https://github.com/Vishal3550/Vishal_Admin_Dashboard_Using_Django/blob/main/Select_User_Chnge_7.png)

### Change_User
![Change_User](https://github.com/Vishal3550/Vishal_Admin_Dashboard_Using_Django/blob/main/Change_User_8.png)



