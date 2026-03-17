-- --------------------------------------------------------
-- Create Table for Warehouse and Retail Sales
-- --------------------------------------------------------

CREATE TABLE warehouse_sales (
    supplier TEXT,
    item_type TEXT,
    year INTEGER,
    month INTEGER,
    retail_sales REAL,
    retail_transfers REAL,
    warehouse_sales REAL,
    date DATE
);

-- Optional: Insert example data 
-- INSERT INTO warehouse_sales (supplier, item_type, year, month, retail_sales, retail_transfers, warehouse_sales, date)
-- VALUES ('Supplier A', 'Item X', 2023, 1, 1200.50, 300.00, 1500.50, '2023-01-01');