CREATE TABLE Customers(
    c_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    customer_address VARCHAR(100) NOT NULL
);

CREATE TABLE Publishers(
    p_id INT PRIMARY KEY,
    publisher_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE Books(
    isbn VARCHAR(100) PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    price DECIMAL, NOT NULL,
    publication_date DATE, not null,
    page_count INT not NULL,
    publisher_id INT REFERENCES Publishers(p_id)
);


