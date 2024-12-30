# Building Blocks

The GaiaCycle project is structured around key components and reusable functionalities to ensure maintainability and scalability. This section outlines the building blocks of the application.

## 1. Core Components
### Database
- The database serves as the backbone of GaiaCycle, storing user data, plant growth records, and feedback submissions.
- **Technology**: PostgreSQL is used for its robustness and compatibility with Django.
- **Schema**:
  - Users table: Stores user profile information.
  - Plants table: Records details about plant species, growth rates, and associated metrics.
  - Feedback table: Stores feedback and contact form submissions.

### Frontend
- Developed using **HTML**, **CSS**, and **Bootstrap** for responsive design.
- Key features include:
  - Navigation bar for accessing pages such as Home, Maps, and Contact Us.
  - Interactive forms for data input and feedback submission.
  - Tutorial page designed for user guidance.

### Backend
- Built with **Django**, providing a strong framework for routing, database interaction, and form handling.
- Handles user requests, manages business logic, and ensures secure communication between the frontend and the database.

## 2. Reusable Components
- **Reusable Functions**:
  - `send_email_notification`: Sends confirmation emails to users after form submissions.
  - `calculate_growth_rate`: Computes plant growth based on input environmental data.
- **UI Components**:
  - Modular form templates for input validation (e.g., feedback form).
  - Bootstrap-based reusable buttons (e.g., Back to Top button).
- **CSS and JavaScript**:
  - Shared stylesheets for consistent branding across pages.
  - Common JavaScript utilities for client-side validation.

## 3. Dependencies
### External Libraries and Tools
- **Bootstrap**: For responsive design and UI components.
- **FontAwesome**: For icons and visual enhancements.
- **Django**: As the web framework for backend development.
- **PostgreSQL**: Database management system.
- **Favicon**: Integrated for a professional touch across all pages.
- **Testing Tools**: Pytest for unit testing backend logic.

### Integration
- External APIs for advanced features (e.g., Google Maps API for the Maps page).
- CDN-hosted resources for Bootstrap and FontAwesome.

## 4. Testing and Quality
### Testing Guidelines
- Write unit tests for critical backend functions, such as:
  - Database interactions.
  - Form validation logic.
  - Email notification system.
- Use Django’s built-in testing framework for comprehensive coverage.

### Quality Assurance
- Peer reviews for all new modules or major updates.
- Regular code audits to ensure adherence to coding standards.
- Continuous integration tools (e.g., GitHub Actions) to run automated tests on every pull request.

### Example Test Case
```python
def test_calculate_growth_rate():
    soil_moisture = 50
    light_exposure = 8
    expected_rate = (soil_moisture * 0.4) + (light_exposure * 0.6)
    assert calculate_growth_rate(soil_moisture, light_exposure) == expected_rate

