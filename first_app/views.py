from django.shortcuts import render
import random
# Create your views here.

def index(request):
    username = '이순신'

    result = {
        'username': username,
    }
    return render(request, 'index.html', result)

def lunch(request):
    menus = ['라면', '김밥','떡볶이']

    pick = random.choice(menus)

    result = {
        'pick':pick
    }

    return render(request, 'lunch.html',result)

def lotto(request):
    lotto = []
    rnd_num = random.randint(1, 46)

    for _ in range(6):
        rnd_num = random.randint(1, 46)
        lotto.append(rnd_num)

    result = {
        'lotto' : lotto
    }
    return render(request, 'lotto.html', result)
 
