import random
import requests

API_KEY = 'be5759d6e37a60eab1ade0621290c1ac'

# Function to fetch movies based on genre from TMDB API


def fetch_movies_by_genre(api_key, genre_id, min_rating=7.0):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}&vote_average.gte={min_rating}&language=en-US&page=1'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()['results']
        return data
    else:
        print(
            f"Failed to retrieve movies. Status Code: {response.status_code}")
        return []


# Genre IDs for TMDB (Common Genres)
genre_mapping = {
    'action': 28,
    'comedy': 35,
    'drama': 18,
    'horror': 27,
    'romance': 10749,
    'sci-fi': 878,
    'thriller': 53
}


def recommend_random_movie(api_key, genre):
    if genre not in genre_mapping:
        return "Sorry, I don't have recommendations for that genre."

    genre_id = genre_mapping[genre]
    movies = fetch_movies_by_genre(api_key, genre_id)
    if not movies:
        return "No movies available for recommendation."

    movie = random.choice(movies)
    title = movie['title']
    rating = movie['vote_average']
    overview = movie['overview']

    return f"\nTitle: {title}\nRating: {rating}\nOverview: {overview}\n"


def main():
    print("Available genres: Action, Comedy, Drama, Horror, Romance, Sci-Fi, Thriller")
    while True:
        user_input = input(
            "Type a genre to get a movie recommendation or 'exit' to quit: ").lower()
        if user_input == 'exit':
            print("Goodbye!")
            break
        else:
            result = recommend_random_movie(API_KEY, user_input)
            print(result)


if __name__ == "__main__":
    main()
