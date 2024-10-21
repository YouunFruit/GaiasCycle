SELECT Users.Name, Users.Role, Farm.Location, Farm.Type
FROM Users
         JOIN Devices ON Users.UserID = Devices.UserID
         JOIN Farm ON Devices.FarmID = Farm.FarmID;
