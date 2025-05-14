# Snowflake Database Setup Documentation

## Table of Contents
1. [Database and Schema Creation](#database-and-schema-creation)
2. [Table Definitions](#table-definitions)
   - [DimLoyaltyInfo](#dimloyaltyinfo)
   - [DimCustomer](#dimcustomer)
   - [DimProductData](#dimproductdata)
   - [DimDate](#dimdate)
   - [DimStoreData](#dimstoredata)
   - [FactOrders](#factorders)
3. [Data Loading Configuration](#data-loading-configuration)
   - [File Format Setup](#file-format-setup)
   - [Stage Creation](#stage-creation)
   - [File Upload Commands (PUT)](#file-upload-commands-put)
4. [Data Loading Execution](#data-loading-execution)
   - [Loading Dimension Tables](#loading-dimension-tables)
   - [Loading Fact Table](#loading-fact-table)
5. [User Management](#user-management)

## Database and Schema Creation

```sql
-- Create database
CREATE DATABASE "testdb";

-- Create schema
CREATE SCHEMA "testschema";
```

## Table Definitions

### DimLoyaltyInfo

```sql
CREATE OR REPLACE TABLE DimLoyaltyInfo (
    LoyaltyInfoID INT PRIMARY KEY,
    ProgramName VARCHAR(100),
    ProgramTier VARCHAR(500),
    PointsSecured INT
);
```

### DimCustomer

```sql
CREATE OR REPLACE TABLE DimCustomer (
    CustomerID INT PRIMARY KEY AUTOINCREMENT START 1 INCREMENT 1,
    FirstName VARCHAR(1550),
    LastName VARCHAR(1550),
    Gender VARCHAR(1550),
    DOB DATE,
    Email VARCHAR(1500),
    Address VARCHAR(1555),
    City VARCHAR(1550),
    State VARCHAR(1550),
    ZipCode VARCHAR(1510),
    LoyaltyInfoID INT
);
```

### DimProductData

```sql
CREATE OR REPLACE TABLE DimProductData (
    ProductID INT PRIMARY KEY AUTOINCREMENT START 1 INCREMENT 1,
    ProductName VARCHAR(1500),
    Category VARCHAR(550),
    BrandName VARCHAR(550),
    UnitPrice DECIMAL(10, 2)
);
```

### DimDate

```sql
CREATE OR REPLACE TABLE DimDate (
    DateID INT PRIMARY KEY,
    Date DATE,
    DayofWeek VARCHAR(100),
    Month INT,
    Year INT,
    Quarter INT,
    IsWeekend BOOLEAN
);
```

### DimStoreData

```sql
CREATE OR REPLACE TABLE DimStoreData (
    StoreID INT PRIMARY KEY AUTOINCREMENT START 1 INCREMENT 1,
    StoreName VARCHAR(1500),
    StoreType VARCHAR(550),
    StoreOpeningDate DATE,
    Address VARCHAR(2555),
    City VARCHAR(550),
    State VARCHAR(550),
    Country VARCHAR(550),
    Region VARCHAR(550),
    ManagerName VARCHAR(1500)
);
```

### FactOrders

```sql
CREATE OR REPLACE TABLE FactOrders (
    OrderID INT PRIMARY KEY AUTOINCREMENT START 1 INCREMENT 1,
    DateID INT,
    ProductID INT,
    StoreID INT,
    CustomerID INT,
    QuantityOrdered INT,
    OrderAmount DECIMAL(10, 2),
    DiscountAmount DECIMAL(10, 2),
    ShippingCost DECIMAL(10, 2),
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (DateID) REFERENCES DimDate(DateID),
    FOREIGN KEY (CustomerID) REFERENCES DimCustomer(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES DimProductData(ProductID),
    FOREIGN KEY (StoreID) REFERENCES DimStoreData(StoreID)
);
```

## Data Loading Configuration

### File Format Setup

```sql
CREATE OR REPLACE FILE FORMAT CSV_SOURCE_FILE_FORMAT
    TYPE = 'CSV'
    SKIP_HEADER = 1
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    DATE_FORMAT = 'YYYY-MM-DD';
```

### Stage Creation

```sql
CREATE OR REPLACE STAGE TESTSTAGE;
```

### File Upload Commands (PUT)

These commands need to be executed from the SnowSQL CLI, not in a worksheet:

```sql
-- PUT file://D:/dwbi/DimLoyaltyInfo.csv @TESTSTAGE/DimLoyaltyInfo/ AUTO_COMPRESS=FALSE;
-- PUT file://D:/dwbi/DimCustomerData.csv @TESTSTAGE/DimCustomerData/ AUTO_COMPRESS=FALSE;
-- PUT file://D:/dwbi/DimProductData.csv @TESTSTAGE/DimProductData/ AUTO_COMPRESS=FALSE;
-- PUT file://D:/dwbi/DimDate.csv @TESTSTAGE/DimDate/ AUTO_COMPRESS=FALSE;
-- PUT file://D:/dwbi/DimStoreData.csv @TESTSTAGE/DimStoreData/ AUTO_COMPRESS=FALSE;
-- PUT file://D:/dwbi/factorders.csv @TESTSTAGE/factorders/ AUTO_COMPRESS=FALSE;
-- PUT file://D:/dwbi/landing/*.csv @TESTSTAGE/landing/ AUTO_COMPRESS=FALSE;
```

## Data Loading Execution

### Loading Dimension Tables

```sql
COPY INTO DimLoyaltyInfo
FROM @TESTSTAGE/DimLoyaltyInfo/DimLoyaltyInfo.csv
FILE_FORMAT = (FORMAT_NAME = 'CSV_SOURCE_FILE_FORMAT');

COPY INTO DimCustomer (FirstName, LastName, Gender, DOB, Email, Address, City, State, ZipCode, LoyaltyInfoID)
FROM @TESTSTAGE/DimCustomerData/DimCustomerData.csv
FILE_FORMAT = (FORMAT_NAME = 'CSV_SOURCE_FILE_FORMAT');

COPY INTO DimProductData (ProductName, Category, BrandName, UnitPrice)
FROM @TESTSTAGE/DimProductData/DimProductData.csv
FILE_FORMAT = (FORMAT_NAME = 'CSV_SOURCE_FILE_FORMAT');

COPY INTO DimDate (DateID, Date, DayofWeek, Month, Year, Quarter, IsWeekend)
FROM @TESTSTAGE/DimDate/DimDate.csv
FILE_FORMAT = (FORMAT_NAME = 'CSV_SOURCE_FILE_FORMAT');

COPY INTO DimStoreData (StoreName, StoreType, StoreOpeningDate, Address, City, State, Country, Region, ManagerName)
FROM @TESTSTAGE/DimStoreData/DimStoreData.csv
FILE_FORMAT = (FORMAT_NAME = 'CSV_SOURCE_FILE_FORMAT');
```

### Loading Fact Table

```sql
COPY INTO FactOrders (DateID, ProductID, StoreID, CustomerID, QuantityOrdered, OrderAmount, DiscountAmount, ShippingCost, TotalAmount)
FROM @TESTSTAGE/factorders/factorders.csv
FILE_FORMAT = (FORMAT_NAME = 'CSV_SOURCE_FILE_FORMAT');

COPY INTO FactOrders (DateID, ProductID, StoreID, CustomerID, QuantityOrdered, OrderAmount, DiscountAmount, ShippingCost, TotalAmount)
FROM @TESTSTAGE/landing/
FILE_FORMAT = (FORMAT_NAME = 'CSV_SOURCE_FILE_FORMAT');
```

## User Management

```sql
CREATE OR REPLACE USER testpbiuser
  PASSWORD = 'testpbiuser',
  LOGIN_NAME = 'pbiuser',
  DEFAULT_ROLE = 'ACCOUNTADMIN',
  DEFAULT_WAREHOUSE = 'COMPUTE_WH',
  MUST_CHANGE_PASSWORD = TRUE;

-- Grant accountadmin access
GRANT ROLE accountadmin TO USER testpbiuser;
```