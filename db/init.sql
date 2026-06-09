CREATE DATABASE IF NOT EXISTS productos_db;

USE productos_db;

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2)
);

INSERT INTO productos (nombre, precio) VALUES
('Laptop', 2500),
('Mouse', 50);
