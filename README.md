# Form Creator API

## Overview:
A Django REST Framework-based API for form creation, designed to allow users to create, manage, and analyze custom forms with various types of questions (e.g., multiple-choice, text-based responses).

## Requirements:
Refer to the [requirements.txt file](https://github.com/AMD921/Form-Creator-API/blob/main/form_creator/requirements.txt) for the full list of dependencies needed to run the project or run the docker compose file.

## Collaborators:
- [https://github.com/YasamanRaouf](https://github.com/YasamanRaouf)
- [https://github.com/mahanmi](https://github.com/mahanmi)
- [https://github.com/Siamakka](https://github.com/Siamakka)
- [https://github.com/i-ftm](https://github.com/i-ftm)
## ERD Overview:
![Entity-Relationship Diagram](https://github.com/AMD921/Form-Creator-API/blob/main/erd.png?raw=true)

## API Endpoints:

| Endpoint                                          | Method | Description                                                                                 |
|---------------------------------------------------|--------|---------------------------------------------------------------------------------------------|
| `/users/`                                         | GET    | Retrieve a list of all users.                                                               |
| `/users/<id>/`                                    | GET    | Retrieve a specific user's information by ID.                                               |
| `/users/auth/registration/`                       | POST   | Register a new user.                                                                        |
| `/users/auth/password/reset/`                     | POST   | Request a password reset link.                                                              |
| `/users/auth/password/reset/confirm/`             | POST   | Confirm the password reset with a token and set a new password.                             |
| `/users/auth/login/`                              | POST   | Log in to obtain an authentication token.                                                   |
| `/users/auth/logout/`                             | POST   | Log out the current authenticated user and invalidate the session/token.                    |
| `/users/auth/user/`                               | GET    | Retrieve details of the currently authenticated user.                                       |
| `/users/auth/password/change/`                    | POST   | Change the password for the currently authenticated user.                                   |
| `/users/auth/token/verify/`                       | POST   | Verify if a given JWT token is valid.                                                       |
| `/users/auth/token/refresh/`                      | POST   | Refresh the JWT token to obtain a new access token.                                         |
| `/forms/questions/`                               | GET    | Retrieve a list of all questions.                                                           |
| `/forms/questions/`                               | POST   | Create a new question.                                                                      |
| `/forms/questions/<id>/`                          | GET    | Retrieve details of a specific question by ID.                                              |
| `/forms/questions/<id>/`                          | PUT    | Update a specific question by ID.                                                           |
| `/forms/questions/<id>/`                          | DELETE | Delete a specific question by ID.                                                           |
| `/forms/answers/`                                 | GET    | Retrieve a list of all answers.                                                             |
| `/forms/answers/`                                 | POST   | Create a new answer.                                                                        |
| `/forms/answers/<id>/`                            | GET    | Retrieve details of a specific answer by ID.                                                |
| `/forms/answers/<id>/`                            | PUT    | Update a specific answer by ID.                                                             |
| `/forms/answers/<id>/`                            | DELETE | Delete a specific answer by ID.                                                             |
| `/forms/categories/`                              | GET    | Retrieve a list of all categories.                                                          |
| `/forms/categories/`                              | POST   | Create a new category.                                                                      |
| `/forms/categories/<id>/`                         | GET    | Retrieve details of a specific category by ID.                                              |
| `/forms/categories/<id>/`                         | PUT    | Update a specific category by ID.                                                           |
| `/forms/categories/<id>/`                         | DELETE | Delete a specific category by ID.                                                           |
| `/forms/processes/`                               | GET    | Retrieve a list of all processes.                                                           |
| `/forms/processes/`                               | POST   | Create a new process.                                                                       |
| `/forms/processes/<id>/`                          | GET    | Retrieve details of a specific process by ID.                                               |
| `/forms/processes/<id>/`                          | PUT    | Update a specific process by ID.                                                            |
| `/forms/processes/<id>/`                          | DELETE | Delete a specific process by ID.                                                            |
| `/forms/forms/`                                   | GET    | Retrieve a list of all forms.                                                               |
| `/forms/forms/`                                   | POST   | Create a new form.                                                                          |
| `/forms/forms/<id>/`                              | GET    | Retrieve details of a specific form by ID.                                                  |
| `/forms/forms/<id>/`                              | PUT    | Update a specific form by ID.                                                               |
| `/forms/forms/<id>/`                              | DELETE | Delete a specific form by ID.                                                               |
| `/report/reports/`                                | GET    | Retrieve a list of all reports.                                                             |
| `/report/reports/`                                | POST   | Create a new report.                                                                        |
| `/report/reports/<id>/`                           | GET    | Retrieve details of a specific report by ID.                                                |
| `/report/reports/<id>/`                           | PUT    | Update a specific report by ID.                                                             |
| `/report/reports/<id>/`                           | DELETE | Delete a specific report by ID.                                                             |
| `/report/process_reports/`                        | GET    | Retrieve a list of all process reports.                                                     |
| `/report/process_reports/`                        | POST   | Create a new process report.                                                                |
| `/report/process_reports/<id>/`                   | GET    | Retrieve details of a specific process report by ID.                                        |
| `/report/process_reports/<id>/`                   | PUT    | Update a specific process report by ID.                                                     |
| `/report/process_reports/<id>/`                   | DELETE | Delete a specific process report by ID.                                                     |
| `/report/forms/<related_object_id>/`              | GET    | Retrieve a report for a specific form by form ID.                                           |
| `/report/process/<related_object_id>/`            | GET    | Retrieve a report for a specific process by form ID.                                        |

---
