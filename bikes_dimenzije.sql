DROP DATABASE bikes_dimenzije;
CREATE DATABASE bikes_dimenzije;
USE bikes_dimenzije;

CREATE TABLE dim_product (
	product_SK INT NOT NULL,
    id INT,
    version INT,
    product_name VARCHAR(200),
    category VARCHAR(45),
    sub_category VARCHAR(45),
    date_from DATETIME,
    date_to DATETIME,
    PRIMARY KEY (product_SK)
    );
    
CREATE TABLE dim_location (
	location_SK INT NOT NULL,
    id INT,
    version INT,
    state VARCHAR(45),
    country VARCHAR(45),
    date_from DATETIME,
    date_to DATETIME,
    PRIMARY KEY (location_SK)
    );
    
CREATE TABLE dim_product_cost (
	product_cost_SK INT NOT NULL,
    id INT,
    version INT,
    unit_cost INT,
    cost INT,
    profit INT,
    date_from DATETIME,
    date_to DATETIME,
    PRIMARY KEY (production_cost_SK)
    );
   
CREATE TABLE dim_customer (
	customer_SK INT NOT NULL,
    id INT,
    version INT,
    age INT,
    age_group VARCHAR(45),
    gender VARCHAR (45),
	date_from DATETIME,
    date_to DATETIME,
    PRIMARY KEY (customer_SK)
    );
 
CREATE TABLE dim_time_of_order (
	time_of_order_SK INT NOT NULL,
    order_date DATETIME,
    PRIMARY KEY (time_of_order_SK)
    );
    
CREATE TABLE dim_order (
	order_SK INT NOT NULL AUTO_INCREMENT,
    id INT,
    order_quantity INT,
    unit_price INT,
    revenue INT,
    time_of_order_SK INT,
    production_cost_SK INT,
    customer_SK INT,
    location_SK INT,
    product_SK INT,
    PRIMARY KEY (order_SK),
    FOREIGN KEY (time_of_order_SK) REFERENCES dim_time_of_order(time_of_order_SK) ON DELETE NO ACTION ON UPDATE CASCADE,
    FOREIGN KEY (production_cost_SK) REFERENCES dim_production_cost(production_cost_SK) ON DELETE NO ACTION ON UPDATE CASCADE,
    FOREIGN KEY (customer_SK) REFERENCES dim_customer(customer_SK) ON DELETE NO ACTION ON UPDATE CASCADE,
	FOREIGN KEY (location_SK) REFERENCES dim_location(location_SK) ON DELETE NO ACTION ON UPDATE CASCADE,
    FOREIGN KEY (product_SK) REFERENCES dim_product(produc_SK) ON DELETE NO ACTION ON UPDATE CASCADE,
  
    
    
    
    );

    select * from dim_customer;
    
    select * from bikes_dimenzije.dim_location;
    
    select * from dim_production_cost;
    
    select * from dim_product;

	select * from dim_time_of_order;

    select * from dim_order;
   


   


