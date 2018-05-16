#0~100 사이의 점수를 입력 받아 입력한 점수가 0~100인 경우 점수에 대한 A, B, C, D, F 등급을 출력하고, 범위에 해당하지 않은 경우 "입력 가능한 점수 범위는 0~100입니다."를 출력해보자. 점수에 대한 등급 판정은 if-elif-else 문을 이용하여 점수가 90~100일 때 "A"이고, 80~89일 때 "B", 70~79일 때 "C", 60~69일 때 "D", 0~50일 때 "F"로 판정한다.

score=int(input("점수:"))
if 90<=score<=100:
    print(score," : ","A")
elif 80<=score<=89:
    print(score," : ","B")
elif 70<=score<=79:
    print(score," : ","C")
elif 60<=score<=69:
    print(score," : ","D")
elif 0<=score<=59:
    print(score," : ","F")
else:
    print("입력 가능한 정수 범위는 0~100입니다.")