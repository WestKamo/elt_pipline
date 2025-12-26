CREATE TABLE users (id SERIAL PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), email VARCHAR(100), date_of_birth DATE);
INSERT INTO users (first_name, last_name, email, date_of_birth) VALUES ('John', 'Doe', 'john.doe@example.com', '1990-01-01'), ('Jane', 'Smith', 'jane.smith@example.com', '1992-05-15');
CREATE TABLE films (film_id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL, release_date DATE, price DECIMAL(5,2), rating VARCHAR(10), user_rating DECIMAL(2,1));
INSERT INTO films (title, release_date, price, rating, user_rating) VALUES ('Inception', '2010-07-16', 12.99, 'PG-13', 4.8);
CREATE TABLE film_category (category_id SERIAL PRIMARY KEY, film_id INTEGER, category_name VARCHAR(50));
CREATE TABLE actors (actor_id SERIAL PRIMARY KEY, actor_name VARCHAR(255));
CREATE TABLE film_actors (film_id INTEGER, actor_id INTEGER, PRIMARY KEY (film_id, actor_id));
