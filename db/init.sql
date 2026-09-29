CREATE DATABASE IF NOT EXISTS appdb;

USE appdb;

CREATE TABLE IF NOT EXISTS application_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    application_name VARCHAR(100),
    version VARCHAR(20)
);

INSERT INTO application_info
(application_name, version)
VALUES
('Three Tier Application', '1.0.0');
