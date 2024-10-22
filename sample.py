from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Predefined list of movies
class Movie(BaseModel):
    id: int
    title: str
    year: int
    director: str

# Sample data
movies_db = [
    Movie(id=1, title="RRR", year=2022, director="SS Rajamouli"),
    Movie(id=2, title="Avatar The Way Of Water", year=2023, director="James Cameron"),
    Movie(id=3, title="Pushpa", year=2021, director="Sukumar"),
    Movie(id=4, title="Kalki 2890AD", year=2024, director="Nag Ashwin"),
    Movie(id=5, title="Jailer", year=2023, director="Nelson"),
]

# Get all movies
@app.get("/movies", response_model=List[Movie])
def get_movies():
    return movies_db

# Get a movie by ID
@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int):
    for movie in movies_db:
        if movie.id == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

# Create a new movie
@app.post("/movies", response_model=Movie)
def create_movie(movie: Movie):
    movies_db.append(movie)
    return movie

# Update a movie
@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, updated_movie: Movie):
    for index, movie in enumerate(movies_db):
        if movie.id == movie_id:
            movies_db[index] = updated_movie
            return updated_movie
    raise HTTPException(status_code=404, detail="Movie not found")

# Delete a movie
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    for index, movie in enumerate(movies_db):
        if movie.id == movie_id:
            movies_db.pop(index)
            return {"detail": "Movie deleted"}
    raise HTTPException(status_code=404, detail="Movie not found")
