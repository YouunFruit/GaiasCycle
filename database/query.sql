--Who works on which farm (showing User and Farm details):
SELECT Users.Name, Users.Role, Farm.Location, Farm.Type
FROM Users
         JOIN Devices ON Users.UserID = Devices.UserID
         JOIN Farm ON Devices.FarmID = Farm.FarmID;

--Which devices belong to which user (showing User and Device details):
SELECT Users.Name, Devices.Type AS DeviceType, Devices.Status
FROM Users
         JOIN Devices ON Users.UserID = Devices.UserID;

--How many people are working in Farm 1:
SELECT COUNT(DISTINCT Users.UserID) AS WorkersInFarm1
FROM Users
         JOIN Devices ON Users.UserID = Devices.UserID
WHERE Devices.FarmID = 1;

--List all devices installed on Farm 2 (showing Device and Farm details):
SELECT Devices.DeviceID, Devices.Type, Devices.Status, Farm.Location
FROM Devices
         JOIN Farm ON Devices.FarmID = Farm.FarmID
WHERE Devices.FarmID = 2;

--Show inactive devices and their associated farms and users:
SELECT Devices.DeviceID, Devices.Type, Users.Name AS AssignedUser, Farm.Location AS FarmLocation
FROM Devices
         LEFT JOIN Users ON Devices.UserID = Users.UserID
         LEFT JOIN Farm ON Devices.FarmID = Farm.FarmID
WHERE Devices.Status = 'Inactive';

--Count the number of users by role (e.g., Farmers, Technicians, Admins):
SELECT Role, COUNT(*) AS NumberOfUsers
FROM Users
GROUP BY Role;
