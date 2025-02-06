movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
'''
#1 Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def above_55(movies,movie_name):
    for movie in movies:
        if movie['name']== movie_name and movie['imdb'] > 5.5:
            return True
        else:
            return False

movie_name = input()
print(above_55(movies,movie_name)) 

#2 Write a function that returns a sublist of movies with an IMDB score above 5.5.
def sublist_ifabove55(movies):
    lists = []
    for list in movies:
        if list['imdb']>5.5:
            lists.append(list)
    return lists
print(sublist_ifabove55(movies))

#3 Write a function that takes a category name and returns just those movies under that category.
def categories(movies,movie_category):
    lists = []
    for list in movies:
        if list['category']>movie_category:
            lists.append(list['name'])
    return lists
cate = input()
print(categories(movies,cate))

#4 Write a function that takes a list of movies and computes the average IMDB score.
def avg_imdb(movies):
    score = sum(movie['imdb'] for movie in movies)
    count = 0
    for i in movies:
        count+=1
    return round((score/count),2)
print(avg_imdb(movies))

#5 Write a function that takes a category and computes the average IMDB score.
def avg_imdb_category(movies,movie_category):
    score = 0
    count = 0
    for i in movies:
        if i['category']== movie_category:
            count+=1
            score += i['imdb']
    return round(score/count,2)

movie_category = input()
print(avg_imdb_category(movies,movie_category))
'''