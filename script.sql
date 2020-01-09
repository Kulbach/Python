DROP DATABASE cinema;

CREATE DATABASE cinema;

DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS directors;
DROP TABLE IF EXISTS movie_director;
DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS actor_movie;

CREATE TABLE movies(
	movie_id serial PRIMARY KEY,
	title VARCHAR(100) NOT NULL,
	description TEXT,
	movie_cost INTEGER,
	genre_id INTEGER NOT NULL
);

 CREATE TABLE directors(
	director_id serial PRIMARY KEY,
	name VARCHAR(70) NOT NULL,
	bio TEXT,
	age INTEGER NOT NULL
);

CREATE TABLE movie_director(
	movie_id INTEGER NOT NULL,
	director_id INTEGER NOT NULL,
	PRIMARY KEY (movie_id, director_id)
);

CREATE TABLE genres(
	genre_id serial PRIMARY KEY,
	genre VARCHAR(50)
);

CREATE TABLE actors(
	actor_id serial PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	gender VARCHAR(45) NOT NULL,
	age VARCHAR(45) NOT NULL,
	bio TEXT
);

CREATE TABLE actor_movie(
	movie_id INTEGER NOT NULL,
	actor_id INTEGER NOT NULL,
	PRIMARY KEY (movie_id, actor_id)
);


ALTER TABLE movies
ADD CONSTRAINT fk_genre_id FOREIGN KEY (genre_id) REFERENCES genres (genre_id)
