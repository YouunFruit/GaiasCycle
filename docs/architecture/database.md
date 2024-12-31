# Database Schema Documentation

## 1. Schema Diagram

### Entities and Their Relationships

#### **Users**
- **Primary Key:** `id`
- **Attributes:**
    - `contact`
    - `name`
    - `username`
    - `password`
- No relationships with other tables.

#### **Farms**
- **Primary Key:** `id`
- **Attributes:**
    - `lat`
    - `lon`
    - `size`
- **Relationships:**
    - **One-to-Many** with `Towers` (via `farm_id`)
    - **One-to-Many** with `Devices` (via `farm_id`)

#### **Towers**
- **Primary Key:** `id`
- **Attributes:**
    - `slot_amount`
    - `farm_id`
- **Relationships:**
    - **Many-to-One** with `Farms` (via `farm_id`)
    - **One-to-Many** with `Slots` (via `tower_id`)
    - **One-to-Many** with `Devices` (via `tower_id`)

#### **Slots**
- **Primary Key:** `id`
- **Attributes:**
    - `tower_id`
    - `crop`
    - `date_filled`
    - `expected_harvest`
- **Relationships:**
    - **Many-to-One** with `Towers` (via `tower_id`)
    - **One-to-Many** with `Devices` (via `slot_id`)

#### **Devices**
- **Primary Key:** `id`
- **Attributes:**
    - `farm_id`
    - `tower_id`
    - `slot_id`
    - `device_type` (Enum: `FARM`, `TOWER`, `SLOT`)
    - `value`
    - `unit`
    - `status` (Enum: `ONLINE`, `OFFLINE`)
    - `installation_date`
- **Relationships:**
    - **Many-to-One** with `Farms` (via `farm_id`)
    - **Many-to-One** with `Towers` (via `tower_id`)
    - **Many-to-One** with `Slots` (via `slot_id`)

### Diagram (Simplified Textual Representation)
```plaintext
Users
    - id (PK)
    - contact
    - name
    - username
    - password

Farms
    - id (PK)
    - lat
    - lon
    - size
    Relationships:
        - Towers (One-to-Many)
        - Devices (One-to-Many)

Towers
    - id (PK)
    - slot_amount
    - farm_id (FK to Farms)
    Relationships:
        - Slots (One-to-Many)
        - Devices (One-to-Many)

Slots
    - id (PK)
    - tower_id (FK to Towers)
    - crop
    - date_filled
    - expected_harvest
    Relationships:
        - Devices (One-to-Many)

Devices
    - id (PK)
    - farm_id (FK to Farms)
    - tower_id (FK to Towers)
    - slot_id (FK to Slots)
    - device_type (Enum: FARM, TOWER, SLOT)
    - value
    - unit
    - status (Enum: ONLINE, OFFLINE)
    - installation_date
```

---

## 2. Explanation of Tables and Relationships

### **Users Table**
- Stores information about users managing or monitoring the system.
- No direct relationships with other tables.

### **Farms Table**
- Represents agricultural farms.
- Each farm can have multiple towers and devices.
- **Key Relationships:**
    - **One-to-Many** with Towers: A farm can have multiple towers.
    - **One-to-Many** with Devices: Devices can be installed directly on a farm.

### **Towers Table**
- Represents structures within farms, capable of holding multiple slots.
- Each tower belongs to a single farm.
- **Key Relationships:**
    - **Many-to-One** with Farms: A tower is linked to one farm.
    - **One-to-Many** with Slots: A tower can have multiple slots.
    - **One-to-Many** with Devices: Devices can be installed on towers.

### **Slots Table**
- Represents subdivisions within towers, which can hold crops.
- Each slot belongs to one tower.
- **Key Relationships:**
    - **Many-to-One** with Towers: A slot belongs to one tower.
    - **One-to-Many** with Devices: Devices can be installed on slots.

### **Devices Table**
- Represents hardware sensors or devices installed on farms, towers, or slots.
- The `device_type` attribute determines whether the device is linked to a farm, tower, or slot.
- **Key Relationships:**
    - **Many-to-One** with Farms: Devices can be installed on farms.
    - **Many-to-One** with Towers: Devices can be installed on towers.
    - **Many-to-One** with Slots: Devices can be installed on slots.

---

## 3. Data Flow

### Insertion
1. **User Creation**: Users register into the system, creating an entry in the `users` table.
2. **Farm Creation**: A new farm is added to the `farms` table with latitude, longitude, and size information.
3. **Tower Creation**: Towers are added to the `towers` table, linking them to the relevant farm using `farm_id`.
4. **Slot Creation**: Slots are added to the `slots` table, linking them to the relevant tower using `tower_id`.
5. **Device Creation**: Devices are added to the `devices` table, specifying their type (`FARM`, `TOWER`, or `SLOT`) and linking them to the appropriate entity.

### Retrieval
1. **Device Data**: Fetch devices installed on a specific farm, tower, or slot by querying the `devices` table with appropriate filters on `farm_id`, `tower_id`, or `slot_id`.
2. **Farm Overview**: Fetch all towers and devices linked to a specific farm.
3. **Tower Overview**: Fetch all slots and devices linked to a specific tower.
4. **Slot Overview**: Fetch all devices linked to a specific slot.

### Updates
1. Devices periodically send updated data (e.g., status or value) using producer threads (like Kafka). These updates are processed and stored in external systems or log streams for analytics.

### Deletion
1. If a farm, tower, or slot is deleted, cascade deletions may occur for linked towers, slots, and devices.
