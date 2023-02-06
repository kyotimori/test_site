from datetime import date

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


post_data = [
    {
        'slug': 'sun-and-a-dog',
        'img': 'dog.jpg',
        'author': 'Nika',
        'date': date(2017, 7, 20),
        'title': 'Catching sun',
        'excerpt': 'After so many cloudy and rainy days, the sun has finally come out. '
                'Got out with Joey away from home, look how happy he is!',
        'content': '''
            Arrived ignorant miles its marry use dear education removing bed. 
            Shed chicken much charmed nor comfort does desire welcomed smallness new melancholy announcing discovered sitting. 
            Tedious every each along simplicity luckily speaking pursuit minuter spoil entreaties described effect juvenile merit tore. 
            May dispatched affection change before how lasting. Incommode carried after engrossed above additions instantly unaffected branch draw evil winding northward. 
        '''
    },
    {
        'slug': 'cozy-evening',
        'img': 'cacao.jpg',
        'author': 'Nika',
        'date': date(2017, 8, 5),
        'title': 'Cozy evening',
        'excerpt': 'After so many cloudy and rainy days, the sun has finally come out. '
                'Got out with Joey away from home, look how happy he is!',
        'content': ''''
            Thing greatly branched done summer interested window described remainder. 
            Imprudence tended sympathize want arise there such do wishing proposal cheered occasional attended. 
            Thing sufficient stronger income behaviour change regret uneasy distant walk five park. 
            Elsewhere windows place shyness musical believe enjoyment six. Discovery partiality equal introduced address each venture tall increasing estimable. 
        '''
    },
    {
        'slug': 'village-forest-field',
        'img': 'village.jpg',
        'author': 'Nika',
        'date': date(2017, 8, 18),
        'title': 'Countryside weekends',
        'excerpt': "I haven't been to the village for a long time. "
                "Finally, I can take a walk in the woods and in the field, make bouquets and pick berries. "
                "I adore raspberries!",
        'content': '''
            Wishes chamber admire took invitation last so part. 
            Marked admiration full greatly collected enquire. 
            Loud hearted shutters appear each overcame me shed society conveying followed. 
            Wished especially commanded barton remainder likewise unpacked table mutual rooms doubt surrounded natural mistake ecstatic. 
            Behaviour talked confined suffering admitted sake minutes than resolving figure likewise required. 
        '''
    }
]


def index(request): 
    intro = 'Hiiiiii this is my blog!'
    sorted_posts = sorted(post_data, key=lambda post: post['date'])
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/start_page.html', {
        'intro': intro,
        'data': latest_posts
    })


def posts(request):
    post_number = 3
    return render(request, 'blog/posts.html', {
        'range': range(post_number),
        'data': post_data
    })


def post_id(request, post_id):
    identified_post = next(post for post in post_data if post['slug'] == post_id)
    return render(request, 'blog/post_page.html', {
        'post': identified_post
    })
