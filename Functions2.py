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


def isMovieBetterThan55(movie):
      return movie["imdb"] > 5.5

print(isMovieBetterThan55(movies[7]))
print("")

def moviesBetterThan55(movies):
      for i in movies:
            if i["imdb"] > 5.5:
                  print(f"{i}")

moviesBetterThan55(movies)
print("")

def findCategory(movies, str):
      for i in movies:
            if i["category"] == str:
                  print(f"{i}")

findCategory(movies, "Thriller")
print("")

def findAverage(movies):
      avg = 0
      for i in movies:
        avg += i["imdb"]
      return(avg / len(movies))

print(findAverage(movies))
print("")

def findCategoryAvg(movies, str):
      avg = 0
      count = 0
      for i in movies:
            if i["category"] == str:
                  avg += i["imdb"]
                  count += 1
      return(avg / count)

print(findCategoryAvg(movies, "Romance"))
print("")
