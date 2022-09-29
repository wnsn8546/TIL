from django.shortcuts import render
import random

# Create your views here.
def index(request):
    test_color = "red"
    context = {
        "test_color": test_color,
    }
    return render(request, "index.html", context)


def ping(request):
    return render(request, "ping.html")


def pong(request):
    ball = request.GET.get("ball")
    context = {
        "name": ball,
    }
    return render(request, "pong.html", context)


def is_odd_even(request, number):
    if number % 2 > 0:
        result = "홀수"
    elif number == 0:
        result = "0"
    else:
        result = "짝수"

    context = {
        "number": number,
        "result": result,
    }
    return render(request, "is_odd_even.html", context)


def calculate(request, num1, num2):

    context = {
        "num1": num1,
        "num2": num2,
        "result1": num1 + num2,
        "result2": num1 - num2,
        "result3": num1 * num2,
        "result4": num1 // num2,
    }
    return render(request, "calculate.html", context)


def pre_life(request):
    return render(request, "pre_life.html")


def pre_life_result(request):
    name = request.GET.get("name")
    pre_life_list = [
        "쥐",
        "소",
        "호랑이",
        "토끼",
        "용",
        "뱀",
        "말",
        "양",
        "원숭이",
        "닭",
        "개",
        "돼지",
    ]
    result = random.choice(pre_life_list)
    result_link = {
        "쥐": "https://cdn-icons-png.flaticon.com/512/1067/1067827.png",
        "소": "https://cdn-icons-png.flaticon.com/512/3319/3319363.png",
        "호랑이": "https://cdn-icons-png.flaticon.com/512/375/375073.png",
        "토끼": "https://cdn-icons-png.flaticon.com/512/1807/1807972.png",
        "용": "https://cdn-icons-png.flaticon.com/512/2119/2119228.png",
        "뱀": "https://cdn-icons-png.flaticon.com/512/1067/1067840.png",
        "말": "https://cdn-icons-png.flaticon.com/512/3819/3819870.png",
        "양": "https://cdn-icons-png.flaticon.com/512/2711/2711858.png",
        "원숭이": "https://cdn-icons-png.flaticon.com/512/616/616433.png",
        "닭": "https://cdn-icons-png.flaticon.com/512/1864/1864470.png",
        "개": "https://cdn-icons-png.flaticon.com/512/2171/2171990.png",
        "돼지": "https://cdn-icons-png.flaticon.com/512/1841/1841026.png",
    }
    context = {
        "name": name,
        "result": result,
        "result_link": result_link[result],
    }
    return render(request, "pre_life_result.html", context)


def lipsum_kor(request):
    return render(request, "lipsum_kor.html")


def lipsum_kor_result(request):
    words = ["사과", "바나나", "포도", "멜론", "참외", "딸기", "귤", "체리", "복숭아", "배"]
    paragraph_num = int(request.GET.get("paragraph_num"))
    word_num = int(request.GET.get("word_num"))
    result = ""

    for i in range(word_num):
        j = i % 10
        result += words[j] + " "

    final_result = []
    for i in range(paragraph_num):
        final_result.append(result)

    context = {
        "final_result": final_result,
    }
    return render(request, "lipsum_kor_result.html", context)
