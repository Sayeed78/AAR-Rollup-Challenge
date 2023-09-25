
-- Generates Subscription table
CREATE TABLE Subscription (
    column1 INT PRIMARY KEY,
    column2 INT,
    column3 DATE, 
    column4 DATE,
    --FOREIGN KEY (column2) REFERENCES Accounts(column1)
);

-- Generates subscription_items table
CREATE TABLE Subscription_items (
    column1 INT PRIMARY KEY,
    column2 INT,
    column3 CHAR VARCHAR(50), 
    column4 INT,
    column5 INT,
    column6 INT,
    column7 DATE,
    column8 DATE,
    FOREIGN KEY (column2) REFERENCES Subscription(column1);
);


SET @database = 'F:\Sohail Sayeed\Repos\AAR-Rollup-Challenge\database'

-- Load data from CSV file into the table
LOAD DATA INFILE @database + '\subscriptions.csv'
INTO TABLE Subscription
FIELDS TERMINATED BY ','  -- Specify the delimiter used in your CSV file
LINES TERMINATED BY '\n' -- Specify the line terminator used in your CSV file
IGNORE 1 ROWS;           -- Skip the header row in the CSV

LOAD DATA INFILE 'F:\Sohail Sayeed\Repos\AAR-Rollup-Challenge\database\subscriptions_items.csv'
INTO TABLE Subscription_items
FIELDS TERMINATED BY ','  -- Specify the delimiter used in your CSV file
LINES TERMINATED BY '\n' -- Specify the line terminator used in your CSV file
IGNORE 1 ROWS;           -- Skip the header row in the CSV

SELECT * FROM Subscription_items;
