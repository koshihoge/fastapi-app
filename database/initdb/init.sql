CREATE TABLE users (
    username varchar PRIMARY KEY,
    full_name varchar not null,
    email varchar,
    hashed_password varchar,
    invalid bool,
    created_at timestamp,
    updated_at timestamp
);

CREATE TABLE employees (
    name varchar,
    email varchar,
    company_id int,
    created_at timestamp,
    updated_at timestamp
);

CREATE TABLE companies (
    name varchar,
    url varchar,
    created_at timestamp,
    updated_at timestamp
);

COPY employees FROM '/workspace/database/employees.csv' DELIMITER ',' CSV HEADER;
COPY companies FROM '/workspace/database/companies.csv' DELIMITER ',' CSV HEADER;
COPY users FROM '/workspace/database/users.csv' DELIMITER ',' CSV HEADER;

ALTER TABLE employees ADD id serial PRIMARY KEY;
ALTER TABLE companies ADD id serial PRIMARY KEY;
