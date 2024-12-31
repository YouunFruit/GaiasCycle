# API Endpoints

## User Endpoints

### `POST /api/user`
- **Description**: Create a new user
- **Request Body**: `UserCreate` object
    - **Example**:
      ```json
      {
        "contact": "user@example.com",
        "name": "John Doe",
        "username": "johndoe",
        "password": "securepassword123"
      }
      ```
- **Response**: `UserRead` object
    - **Example**:
      ```json
      {
        "id": 1,
        "contact": "user@example.com",
        "name": "John Doe",
        "username": "johndoe"
      }
      ```

### `GET /api/user/{user_id}`
- **Description**: Get user by ID
- **Path Parameter**: `user_id` (integer)
- **Response**: `UserRead` object
    - **Example**:
      ```json
      {
        "id": 1,
        "contact": "user@example.com",
        "name": "John Doe",
        "username": "johndoe"
      }
      ```

### `GET /api/user/username/{username}`
- **Description**: Get user by username
- **Path Parameter**: `username` (string)
- **Response**: `UserRead` object
    - **Example**:
      ```json
      {
        "id": 1,
        "contact": "user@example.com",
        "name": "John Doe",
        "username": "johndoe"
      }
      ```

---

## Farm Endpoints

### `POST /api/farm`
- **Description**: Create a new farm
- **Request Body**: `FarmCreate` object
    - **Example**:
      ```json
      {
        "lat": 34.0522,
        "lon": -118.2437,
        "size": 150.5
      }
      ```
- **Response**: `FarmRead` object
    - **Example**:
      ```json
      {
        "id": 1,
        "lat": 34.0522,
        "lon": -118.2437,
        "size": 150.5
      }
      ```

### `GET /api/farm`
- **Description**: Get all farms
- **Response**: List of `FarmRead` objects
    - **Example**:
      ```json
      [
        {
          "id": 1,
          "lat": 34.0522,
          "lon": -118.2437,
          "size": 150.5
        },
        {
          "id": 2,
          "lat": 36.7783,
          "lon": -119.4179,
          "size": 200.0
        }
      ]
      ```

### `GET /api/farm/{farm_id}`
- **Description**: Get farm by ID
- **Path Parameter**: `farm_id` (integer)
- **Response**: `FarmRead` object
    - **Example**:
      ```json
      {
        "id": 1,
        "lat": 34.0522,
        "lon": -118.2437,
        "size": 150.5
      }
      ```

---

## Tower Endpoints

### `POST /api/tower`
- **Description**: Create a new tower
- **Request Body**: `TowerCreate` object
    - **Example**:
      ```json
      {
        "farm_id": 1,
        "slot_amount": 10
      }
      ```
- **Response**: `TowerRead` object
    - **Example**:
      ```json
      {
        "id": 1,
        "farm_id": 1,
        "slot_amount": 10
      }
      ```

### `GET /api/tower`
- **Description**: Get all towers
- **Response**: List of `TowerRead` objects
    - **Example**:
      ```json
      [
        {
          "id": 1,
          "farm_id": 1,
          "slot_amount": 10
        },
        {
          "id": 2,
          "farm_id": 1,
          "slot_amount": 8
        }
      ]
      ```

### `GET /api/tower/{tower_id}`
- **Description**: Get tower by ID
- **Path Parameter**: `tower_id` (integer)
- **Response**: `TowerRead` object
    - **Example**:
      ```json
      {
        "id": 1,
        "farm_id": 1,
        "slot_amount": 10
      }
      ```

---

## Device Endpoints

### `POST /api/device`
- **Description**: Create a new device
- **Request Body**: `DeviceCreate` object
    - **Example**:
      ```json
      {
        "tower_id": 1,
        "farm_id": 1,
        "slot_id": 1,
        "device_type": "FARM",
        "status": "ONLINE",
        "value": 50,
        "unit": "kWh",
        "installation_date": "2023-01-15"
      }
      ```
- **Response**: `DeviceRead` object
    - **Example**:
      ```json
      {
        "id": 1,
        "tower_id": 1,
        "farm_id": 1,
        "slot_id": 1,
        "device_type": "FARM",
        "status": "ONLINE",
        "value": 50,
        "unit": "kWh",
        "installation_date": "2023-01-15"
      }
      ```

### `GET /api/device`
- **Description**: Get all devices
- **Response**: List of `DeviceRead` objects
    - **Example**:
      ```json
      [
        {
          "id": 1,
          "tower_id": 1,
          "farm_id": 1,
          "slot_id": 1,
          "device_type": "FARM",
          "status": "ONLINE",
          "value": 50,
          "unit": "kWh",
          "installation_date": "2023-01-15"
        }
      ]
      ```

### `GET /api/device/{device_id}`
- **Description**: Get device by ID
- **Path Parameter**: `device_id` (integer)
- **Response**: `DeviceRead` object
    - **Example**:
      ```json
      {
        "id": 1,
        "tower_id": 1,
        "farm_id": 1,
        "slot_id": 1,
        "device_type": "FARM",
        "status": "ONLINE",
        "value": 50,
        "unit": "kWh",
        "installation_date": "2023-01-15"
      }
      ```

---

## Slot Endpoints

### `POST /api/slot`
- **Description**: Create a new slot
- **Request Body**: `SlotCreate` object
    - **Example**:
      ```json
      {
        "tower_id": 1,
        "crop": "Corn",
        "date_filled": "2023-02-01",
        "expected_harvest": "2023-05-01"
      }
      ```
- **Response**: `SlotRead` object
    - **Example**:
      ```json
      {
        "id": 1,
        "tower_id": 1,
        "crop": "Corn",
        "date_filled": "2023-02-01",
        "expected_harvest": "2023-05-01"
      }
      ```

### `GET /api/slot`
- **Description**: Get all slots
- **Response**: List of `SlotRead` objects
    - **Example**:
      ```json
      [
        {
          "id": 1,
          "tower_id": 1,
          "crop": "Corn",
          "date_filled": "2023-02-01",
          "expected_harvest": "2023-05-01"
        }
      ]
      ```

### `GET /api/slot/{slot_id}`
- **Description**: Get slot by ID
- **Path Parameter**: `slot_id` (integer)
- **Response**: `SlotRead` object
    - **Example**:
      ```json
      {
        "id": 1,
        "tower_id": 1,
        "crop": "Corn",
        "date_filled": "2023-02-01",
        "expected_harvest": "2023-05-01"
      }
      ```
