CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Username VARCHAR(50) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Role ENUM('Farmer', 'Technician', 'Admin') NOT NULL,
    ContactDetails VARCHAR(255)
);


CREATE TABLE Farm (
    FarmID INT AUTO_INCREMENT PRIMARY KEY,
    Location VARCHAR(255) NOT NULL,
    Size FLOAT,
    Type ENUM('Crop Farm', 'Livestock Farm', 'Urban Farm') NOT NULL
);

CREATE TABLE Devices (
    DeviceID INT AUTO_INCREMENT PRIMARY KEY,
    Type VARCHAR(100) NOT NULL,
    Status ENUM('Active', 'Inactive') NOT NULL,
    InstallationDate DATE,
    FarmID INT,
    UserID INT,
    FOREIGN KEY (FarmID) REFERENCES Farm(FarmID) ON DELETE CASCADE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE SET NULL
);


