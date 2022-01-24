# 関数

def say_hello():
    print("hello world")


say_hello()

# 引数、戻り値
def sum(x, y):
    return x + y

num1 =  sum(30, 30)
num2 =  sum(3, 3)
print(num1)
print(num2)


import random

def attack(enemy):
    print("勇者は" + enemy + "を攻撃した。")
    hit = random.randint(1,10)
    if hit < 6 :
        print(enemy + "に" + str(hit) + "の攻撃を与えた")
    else:
        print("クリティカルヒット" + str(hit) + "のダメージを与えた")

enemies = ["スライム","モンスター","ドラゴン"]
for enemy in enemies:
    attack(enemy)


def introduce(greeting, *names):
    for name in names:
        print("私は" + name + "です。" + greeting)

introduce("こんにちは","勇者","村人")
