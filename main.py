from re import A
import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 아래에 코드를 기록하세요.
# 코드 실행은 터미널에서 shell을 실행시켜서 해주세요. 
# $ python manage.py shell_plus 

# 4
d = Director.objects.get(name = '봉준호')
print(f'id : {d.id}')
print(f'name : {d.name}')
print(f'debut : {d.debut}')
print(f'country : {d.country}')

#5
g = Genre.objects.get(title = '드라마')
print(f'id : {g.id}')
print(f'title : {g.title}')

#6
director_ = Director.objects.get(name='봉준호')
genre_ = Genre.objects.get(title='드라마')

movie = Movie()

movie.director = director_
movie.genre = genre_
movie.title = '기생충'
movie.opening_date = '2019-05-30'
movie.running_time = 132
movie.screening = False

movie.save()

#7
movies = [
    ("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
    ("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
    ("김한민", "사극", "한산", "2022-07-27", 129, True),
    ("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
    ("이정재", "첩보", "헌트", "2022-08-10", 125, True),
    ("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
    ("한재림", "재난", "비상선언", "2022-08-03", 140, True),
    ("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True),
]

for movie in movies:
    director_ = Director.objects.get(name = movie[0])
    genre_ = Genre.objects.get(title = movie[1])
    title_ = movie[2]
    opening_date_ = movie[3]
    running_time_ = movie[4]
    screening_ = movie[5]
    Movie.objects.create(director = director_, genre = genre_, title = title_, opening_date = opening_date_, running_time = running_time_, screening = screening_)

#8
movies = Movie.objects.all()
for m in movies:
    print(m.director, m.genre, m.title, m.opening_date, m.running_time, m.screening)

#9
movies = Movie.objects.all()
for m in movies:
    print(m.director.name, m.genre, m.title, m.opening_date, m.running_time, m.screening)

#10
movies = Movie.objects.all()
for m in movies:
    print(m.director.name, m.genre.title, m.title, m.opening_date, m.running_time, m.screening)

#11
movies = Movie.objects.order_by('-opening_date')
for m in movies:
    print(m.director.name, m.genre.title, m.title, m.opening_date, m.running_time, m.screening)

#12
m = Movie.objects.order_by('opening_date')[0]
print(m.director.name, m.genre.title, m.title, m.opening_date, m.running_time, m.screening)

#13
movies = Movie.objects.filter(screening = True).order_by('opening_date')
for m in movies:
    print(m.director.name, m.genre.title, m.title, m.opening_date, m.running_time, m.screening)

#14
movies = Movie.objects.filter(director = Director.objects.get(name = '봉준호').id).order_by('opening_date')
for m in movies:
    print(m.director.name, m.genre.title, m.title, m.opening_date, m.running_time, m.screening)

#15
movies = Movie.objects.filter(director = Director.objects.get(name = '봉준호').id).order_by('running_time')
m = movies[1]
print(m.director.name, m.genre.title, m.title, m.opening_date, m.running_time, m.screening)

#16
movies = Movie.objects.filter(running_time__gt = 119).order_by('running_time')
for m in movies:
    print(m.director.name, m.genre.title, m.title, m.opening_date, m.running_time, m.screening)

#17
movies = Movie.objects.filter(running_time__gte = 119).order_by('running_time')
for m in movies:
    print(m.director.name, m.genre.title, m.title, m.opening_date, m.running_time, m.screening)

#18
import datetime
start_date = datetime.date(2022, 2, 2)
end_date = datetime.datetime.now()
movies = Movie.objects.filter(opening_date__range = (start_date, end_date)).order_by('opening_date')

for m in movies:
    print(m.director.name, m.genre.title, m.title, m.opening_date, m.running_time, m.screening)

#19
movies = Movie.objects.filter(director = 1, genre = 2).order_by('opening_date')
for m in movies:
    print(m.director.name, m.genre.title, m.title, m.opening_date, m.running_time, m.screening)

#20
movies = Movie.objects.exclude(director = 1).order_by('opening_date')
for m in movies:
    print(m.director.name, m.genre.title, m.title, m.opening_date, m.running_time, m.screening)