# Backend Components

---

# Backend Documentation

## Backend Architecture and Responsibilities

### Overview
The backend is designed to:
- Handle API requests from the frontend and external systems.
- Manage business logic for user, farm, tower, device, and slot functionalities.
- Interact with the database to perform CRUD operations.
- Provide secure and scalable services.
- Integrate with third-party tools like Redis for caching and Docker for containerization.

### Architecture
- **Layered Architecture**:
    - **Presentation Layer**: Exposes RESTful APIs.
    - **Service Layer**: Contains business logic and validation.
    - **Data Access Layer**: Handles interactions with the database.
- **Technologies**:
    - Python (FastAPI framework)
    - MySQL database
    - Docker for containerization
    - Redis for caching frequently accessed data

### Key Responsibilities
1. **User Management**:
    - Registration and authentication.
    - Fetch user data by ID or username.
2. **Farm and Tower Management**:
    - CRUD operations for farms and towers.
3. **Device Monitoring**:
    - Storing and retrieving device information.
    - Managing device status (online/offline).
4. **Slot Tracking**:
    - Monitoring crop and harvest details.

---

## Frameworks and Libraries Used

### Core Backend Framework
- **FastAPI**:
    - Provides asynchronous API handling.
    - Built-in data validation with Pydantic.

### Database
- **SQLAlchemy** (with AsyncSession):
    - ORM for database operations.
    - Support for MySQL.

### Caching
- **Redis**:
    - Used for caching frequently accessed data.

### Containerization
- **Docker**:
    - Provides containerized environment for the application and MySQL database.

### Additional Libraries
- **Pydantic**:
    - Schema definitions and data validation.
- **Enum**:
    - Defines constants like device status and type.
- **Datetime**:
    - Handles date and time operations.

---

## APIs Exposed by the Backend

### User APIs
- `POST /api/user`:
    - Create a new user.
    - **Request Body**: `UserCreate` object
    - **Response**: `UserRead` object
- `GET /api/user/{user_id}`:
    - Fetch user by ID.
    - **Path Parameter**: `user_id` (integer)
    - **Response**: `UserRead` object
- `GET /api/user/username/{username}`:
    - Fetch user by username.
    - **Path Parameter**: `username` (string)
    - **Response**: `UserRead` object

### Farm APIs
- `POST /api/farm`:
    - Create a new farm.
    - **Request Body**: `FarmCreate` object
    - **Response**: `FarmRead` object
- `GET /api/farm`:
    - Fetch all farms.
    - **Response**: List of `FarmRead` objects
- `GET /api/farm/{farm_id}`:
    - Fetch farm by ID.
    - **Path Parameter**: `farm_id` (integer)
    - **Response**: `FarmRead` object

### Tower APIs
- `POST /api/tower`:
    - Create a new tower.
    - **Request Body**: `TowerCreate` object
    - **Response**: `TowerRead` object
- `GET /api/tower`:
    - Fetch all towers.
    - **Response**: List of `TowerRead` objects
- `GET /api/tower/{tower_id}`:
    - Fetch tower by ID.
    - **Path Parameter**: `tower_id` (integer)
    - **Response**: `TowerRead` object

### Device APIs
- `POST /api/device`:
    - Create a new device.
    - **Request Body**: `DeviceCreate` object
    - **Response**: `DeviceRead` object
- `GET /api/device`:
    - Fetch all devices.
    - **Response**: List of `DeviceRead` objects
- `GET /api/device/{device_id}`:
    - Fetch device by ID.
    - **Path Parameter**: `device_id` (integer)
    - **Response**: `DeviceRead` object

### Slot APIs
- `POST /api/slot`:
    - Create a new slot.
    - **Request Body**: `SlotCreate` object
    - **Response**: `SlotRead` object
- `GET /api/slot`:
    - Fetch all slots.
    - **Response**: List of `SlotRead` objects
- `GET /api/slot/{slot_id}`:
    - Fetch slot by ID.
    - **Path Parameter**: `slot_id` (integer)
    - **Response**: `SlotRead` object

