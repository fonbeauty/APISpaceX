movies = [
    [1994, 'The Shawshank Redemption', 9.0],
    [1999, 'Fight Club', 8.8],
    [1994, 'Pulp Fiction', 8.9],
    [1972, 'The Godfather', 9.1],
    [2008, 'The Dark Knight', 9.0],
    [1998, 'Godzilla', 6.8],
    [1989, 'Batman', 7.5]
]

# result = sorted(movies)
result = sorted(movies, key=lambda movie: (movie[2], movie[1]))
for i in result:
    print(i)
