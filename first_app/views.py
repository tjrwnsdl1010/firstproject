from django.shortcuts import render
import random
import requests

from faker import Faker
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
    numbers = range(1, 46)
    lucky_num = random.sample(numbers, 6)

    URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1071'

    res = requests.get(URL)

    data = res.json()

    drwtNo1 = data['drwtNo1']
    drwtNo2 = data['drwtNo2']
    drwtNo3 = data['drwtNo3']
    drwtNo4 = data['drwtNo4']
    drwtNo5 = data['drwtNo5']
    drwtNo6 = data['drwtNo6']

    lotto_number = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6]

    num = len(set(lotto_number) & set(lucky_num))


    result = {
        'lucky_num': lucky_num,
        'lotto_number': lotto_number,
        'num': num, 
    }

    return render(request, 'lotto.html', result)

def cube(request, num):
    result = {
        'num' : num,
        'cube':num**3,
    }
    return render(request,'cube.html',result)

def posts(request):
    fake = Faker()
    
    post_dict = {}

    for i in range(5):
        post_dict[fake.text(max_nb_chars=10)] = fake.text()

    result = {'post_dict':post_dict}
    return render(request,'posts.html',result)

def hello(request,name):
    result = {
        'name':name
    }

def menus(request):
    meal = ["김밥","라면","떡볶이","비빔밥","스테이크","우동","스시"]
    dish = {}
    

    
        
    result = {
        'pick' : pick
    }
    return render(request,'menus.html',result)