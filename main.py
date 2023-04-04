import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame


# --- PART 1: READING DATA ---
# 1.1
def read_ratings_data(f):
    mRatings = {}
    rFile = open(f)
    for line in rFile:
        line.strip('\n')
        name, rating, uID = line.split('|')
        name = name.strip('\n')
        # print("name: ", name)
        # print("rating: ", rating)
        if name in mRatings:
            mRatings[name].append(float(rating))
        else:
            mRatings[name] = [float(rating)]
    return mRatings


# 1.2
def read_movie_genre(f):
    mGenre = {}
    rFile = open(f)
    for line in rFile:
        line.strip('\n')
        genre, uID, name = line.split('|')
        genre = genre.strip('\n')
        name = name.strip('\n')
        # print("name: ", name)
        # print("rating: ", genre)
        mGenre[name] = genre
    return mGenre

# # --- PART 2: PROCESSING DATA ---
# 2.1


def create_genre_dict(d):
    gDict = {}
    for i in d.keys():
        if d[i] in gDict:
            gDict[d[i]].append(i)
        else:
            gDict[d[i]] = [i]
    return gDict
# 2.2


def calculate_average_rating(d):
    aRatings = {}
    for i in d.keys():
        aRatings[i] = round((sum(d[i])/len(d[i])), 2)
    return aRatings

# # --- PART 3: RECOMMENDATION ---
# 3.1


def get_popular_movies(d, n=10):
    pDict = {}
    temp = sorted(d)
    i = 0
    while n >= 0:
        # print("i: ", i)
        if i >= len(temp):
            break
        pDict[i] = temp[i]
        # print(pDict)
        i = i + 1
        n = n - 1
    # print("returning")
    return pDict

# 3.2


def filter_movies(d, thres_rating=3):
    fMovies = {}
    for i in d.keys():
        if d[i] >= thres_rating:
            fMovies[i] = d[i]
    return fMovies

# 3.3


def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    pgDict = {}
    temp = genre_to_movies[genre]
    temp2 = {}
    for i in temp:
        temp2[i] = movie_to_average_rating[i]
    # print("temp: ", temp)
    # print("temp2: ", temp2)
    i = 0
    while n >= 0:
        # print("i: ", i)
        if i >= len(temp):
            break
        pgDict[i] = temp[i]
        # print(pDict)
        i = i + 1
        n = n - 1
    return pgDict

# 3.4


def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    temp = genre_to_movies[genre]
    temp2 = {}
    for i in temp:
        temp2[i] = movie_to_average_rating[i]
    # print("temp2: ", temp2)
    total = 0
    for i in temp2:
        total = total+temp2[i]
    gRating = round((total/len(temp2)), 2)
    return gRating

# 3.5


def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    gpDict = {}
    temp = {}
    for i in genre_to_movies.keys():
        temp[i] = get_genre_rating(i, genre_to_movies, movie_to_average_rating)
    # print("temp: ", temp)
    genres = []
    for k in temp.keys():
        genres.append(k)
    # print("genres: ", genres)
    i = 0
    while n >= 0:
        # print("i: ", i)
        if i >= len(temp):
            break
        gpDict[genres[i]] = temp[genres[i]]
        # print(pDict)
        i = i + 1
        n = n - 1
    return gpDict


# # --- PART 4: USER FOCUSED ---
# 4.1
def read_user_ratings(f):
    uRatings = {}
    rFile = open(f)
    for line in rFile:
        line.strip('\n')
        name, rating, uID = line.split('|')
        name = name.strip('\n')
        rating = float(rating.strip("\n"))
        uID = int(uID.strip("\n"))
        # print("name: ", name)
        # print("rating: ", rating)
        # print("uID: ", uID)
        if uID in uRatings:
            uRatings[uID].append((name, rating))
        else:
            uRatings[uID] = [(name, rating)]

    return uRatings

# 4.2


def get_user_genre(user_id, user_to_movies, movie_to_genre):
    temp = user_to_movies[user_id]
    genres = {}
    averages = {}
    # print("temp: ", temp)
    for i in temp:
        if movie_to_genre[i[0]] in genres:
            genres[movie_to_genre[i[0]]].append(i[1])
        else:
            genres[movie_to_genre[i[0]]] = [i[1]]
    # print("genres: ", genres)

    for i in genres.keys():
        averages[i] = round((sum(genres[i])/len(genres[i])), 2)
    # print("averages: ", averages)
    uGenre = max(averages, key=averages.get)
    return uGenre

# 4.3


def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    uRec = {}
    uMovies = user_to_movies[user_id]
    notSeen = {}
    for i in movie_to_average_rating.keys():
        for k in uMovies:
            if i == k[0]:
                print("i: ", i)
                notSeen[i] = movie_to_genre[i]
    print("uMovies: ", uMovies)
    print("notSeen: ", notSeen)
    print("len(notSeen): ", len(notSeen))
    return uRec


if __name__ == "__main__":
    ratings = read_ratings_data("movieRatingSample.txt")
    # print("ratings:\n", ratings)
    # print("len(ratings): ", len(ratings))

    genres = read_movie_genre("genreMovieSample.txt")
    print("genres:", genres)
    # print("len(genres): ", len(genres))

    gDict = create_genre_dict(genres)
    # print("gDict: ", gDict)
    # print("len(gDict): ", len(gDict))

    aveRatings = calculate_average_rating(ratings)
    print("aveRatings: ", aveRatings)
    # print("len(aveRatings): ", len(aveRatings))

    popDict = get_popular_movies(aveRatings)
    # print("popDict: ", popDict)
    # print("len(popDict): ", len(popDict))

    fMovies = filter_movies(aveRatings)
    # print("fMovies: ", fMovies)
    # print("len(fMovies): ", len(fMovies))

    pgDict = get_popular_in_genre("Comedy", gDict, aveRatings)
    # print("pgDict: ", pgDict)
    # print("len(pgDict): ", len(pgDict))

    gRating = get_genre_rating("Comedy", gDict, aveRatings)
    # print("gRating: ", gRating)

    gpDict = genre_popularity(gDict, aveRatings)
    # print("gpDict: ", gpDict)
    # print("len(gpDict): ", len(gpDict))

    uRatings = read_user_ratings("movieRatingSample.txt")
    print("uRatings: ", uRatings)
    # print("len(uRatings): ", len(uRatings))

    uGenre = get_user_genre(6, uRatings, genres)
    # print("uGenre: ", uGenre)

    uRec = recommend_movies(6, uRatings, genres, aveRatings)
    print("uRec:", uRec)
    print("len(uRec): ", len(uRec))
