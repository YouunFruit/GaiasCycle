# Testing Guidelines

## 1. Types of Tests

### Unit Testing
Unit tests focus on testing individual components in isolation. These tests ensure that each part of the application works as expected. For instance, testing backend API endpoints, user authentication logic, or database interactions.

### Integration Testing
Integration tests check the interaction between different components of the system. This includes validating that the backend communicates correctly with the database, and that API calls return the expected results when integrated with other services.

### End-to-End Testing
End-to-end tests simulate real-world user interactions with the entire system. These tests ensure that the complete user journey works smoothly, from the frontend interface to the backend and database.

### Performance Testing
Performance tests validate that the application can handle expected loads and perform efficiently under stress. This involves checking response times and system behavior under heavy traffic.

### Security Testing
Security tests are designed to identify vulnerabilities within the system. They verify that sensitive data is protected, and the application is resistant to common security threats such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).

## 2. Frameworks and Tools

The following frameworks and tools are used for different types of testing:

### Unit Testing Frameworks:
- **pytest**: A robust testing framework for Python, which is easy to use and integrates well with other tools.
- **unittest**: Python's built-in testing module, used for unit testing.

### Integration Testing Frameworks:
- **Postman**: Used to test RESTful APIs. It allows you to send HTTP requests and validate responses, making it ideal for integration testing of backend services.
- **pytest**: Also used for integration testing, especially with custom test suites for backend API interactions.

### End-to-End Testing Frameworks:
- **Selenium**: An automated web testing framework that interacts with browsers to simulate user actions.

### Performance Testing Tools:
- **JMeter**: A tool for load testing and performance benchmarking, useful to simulate heavy traffic and validate system responsiveness.
- **Locust**: A Python-based tool that allows you to define user behavior and test how the system handles concurrent requests.

### Security Testing Tools:
- **OWASP ZAP**: A security testing tool that scans the application for vulnerabilities, including common OWASP threats.
- **Burp Suite**: A powerful tool for identifying and mitigating security issues within web applications.

## 3. Steps to Run Tests Locally

### Setting Up the Environment
1. **Install Dependencies**:
   First, make sure that all necessary dependencies for testing are installed. Run the following command to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up the Local Database (for integration tests)**:
   Since we're using a **local database** for testing, ensure that it's set up properly. We are using MySQL locally. Ensure that your local database is running and accessible for tests.(**MySQL container from Docker**)

   You can also use **test-specific databases** for testing purposes, ensuring that your development database isn't affected by test data.

   Make sure your local database connection is properly configured in your `.env` file or environment variables:
   ```bash
   export DATABASE_URL=your_local_database_url
   export API_KEY=your_api_key
   ```

3. **Environment Variables**:
   Some tests may require specific environment variables. Set them as needed, either in a `.env` file or through your system settings. For example:
   ```bash
   export DATABASE_URL=your_local_database_url
   export API_KEY=your_api_key
   ```

4. **Configure Test Settings**:
   Some tests may require mock services or certain configurations. Ensure that any mock services are set up (e.g., mock databases, APIs) and the appropriate test configuration is applied.

### Running Unit Tests
To run the unit tests, use the following command:
```bash
pytest tests/unit/
```
You can specify additional options such as `--maxfail=1` to stop after the first failure:
```bash
pytest --maxfail=1 tests/unit/
```

### Running Integration Tests
For integration tests:
- **Postman**: Import the collection for integration tests and click "Run" to execute them.
- **pytest**: If running integration tests via `pytest`, use:
  ```bash
  pytest tests/integration/
  ```

### Running End-to-End Tests
For end-to-end testing with **Selenium** or **Cypress**:
- **Selenium**: Ensure that the browser driver (e.g., ChromeDriver) is installed. Then run the tests:
  ```bash
  pytest tests/e2e/
  ```


### Running Performance Tests
To run performance tests with **Locust** or **JMeter**:
- **Locust**: Run Locust for load testing:
  ```bash
  locust -f tests/performance/test_script.py
  ```

- **JMeter**: Import the JMeter test plan and run it from the JMeter interface.

### Running Security Tests
For security tests:
- **OWASP ZAP**: Start OWASP ZAP and configure the target application URL. Run automated security scans.
- **Burp Suite**: Use Burp Suite to scan for vulnerabilities in the application.

---

### Additional Notes:
- **Test Coverage**: Aim to have high test coverage by writing tests for the core components of your application.
- **CI/CD Integration**: Ensure that tests are integrated into your continuous integration (CI) pipeline, so tests run automatically on each commit.

---