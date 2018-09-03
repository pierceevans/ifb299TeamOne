CREATE DATABASE Rentals;
USE Rentals;

CREATE TABLE Customers (
    Customer_ID INT NOT NULL,
    Customer_Name NVARCHAR(25) NOT NULL,
    Customer_Phone NVARCHAR(30) NOT NULL,
    Customer_Address NVARCHAR(35) NOT NULL,
    Customer_Occupation NVARCHAR(20) NOT NULL,
	Customer_Birthday DATE NOT NULL,
    Customer_Gender NCHAR(1) NOT NULL,
    PRIMARY KEY (Customer_ID)
);

CREATE TABLE Makes (
 Car_Make_Key int,
 Car_Make_Name nvarchar(20),
 Car_Model nvarchar(25),
 Car_Series nvarchar(30),
 PRIMARY KEY (Car_Make_Key)
);

CREATE TABLE Vehicles (
 Car_ID int not null,
 Car_Make_Key int references Makes(Car_Make_Key),
 Car_Series_Year int, 
 Car_PriceNew int,
 Car_EngineSize nvarchar(4),
 Car_FuelSystem nvarchar(25),
 Car_TankCapacity nvarchar(6),
 Car_Power nvarchar(5),
 Car_SeatingCapacity int,
 Car_StandardCapacity nvarchar(5),
 Car_BodyType nvarchar(15),
 Car_Drive nchar(3),
 Car_Wheelbase nchar(6),
 PRIMARY KEY (Car_ID)
);

CREATE TABLE Locations (
 Location_ID int, 
 Store_State nvarchar(20),
 Store_City nvarchar(20),
 Store_Address nvarchar(30),
 PRIMARY KEY (Location_ID)
);

CREATE TABLE Stores (
 Store_ID int not null,
 Store_Name nvarchar(30),
 Store_Phone nvarchar(25),
 Location_ID int references Locations(Location_ID),
 PRIMARY KEY (Store_ID)
);

CREATE TABLE Times (
 Time_ID int not null,
 Year int not null,
 Month int not null,
 Day int not null,
 PRIMARY KEY (Time_ID)
);

CREATE TABLE Orders (
 Order_ID int not null,
 Customer_ID int not null references Vehicles(Customer_ID),
 Car_ID int not null references Vehicles(Car_ID),
 Pickup_Store_ID int not null references Stores(Store_ID),
Return_Store_ID int not null references Stores(Store_ID),
 Order_Create_Date_ID int not null references Times(Time_ID),
 Pickup_Date_ID int not null references Times(Time_ID),
Return_Date_ID int not null references Times(Time_ID),
 PRIMARY KEY (Order_ID)
);
