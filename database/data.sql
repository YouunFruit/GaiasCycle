INSERT INTO Users (name, username, password, role, ContactDetails)
VALUES
    ('Marie', 'marie_user', 'password123', 'Farmer', 'marie@example.com'),
    ('Iker', 'iker_user', 'password123', 'Technician', 'iker@example.com'),
    ('Martin', 'martin_user', 'password123', 'Admin', 'martin@example.com'),
    ('Sam', 'sam_user', 'password123', 'Farmer', 'sam@example.com'),
    ('Balita', 'balita_user', 'password123', 'Technician', 'balita@example.com'),
    ('Rishi', 'rishi_user', 'password123', 'Farmer', 'rishi@example.com');


INSERT INTO Farm (location, size, type)
VALUES
    ('Urban Farm - Potsdam', 50.0, 'Urban Farm'),
    ('Crop Farm - Berlin', 200.0, 'Crop Farm');


INSERT INTO Devices (type, status, InstallationDate, FarmId, UserId)
VALUES
    ('Soil Moisture Sensor', 'Active', '2024-10-01', 1, 2),
    ('Temperature Sensor', 'Active', '2024-10-05', 2, 5),
    ('CO2 Sensor', 'Inactive', '2024-09-15', 1, 4),
    ('Water pH Sensor', 'Active', '2024-10-10', 2, 2);


