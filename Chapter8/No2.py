#문자열을 입력 받아 for 문을 이용하여 개별 문자로 출력해보자. 그리고 for 문을 이용하여 입력 받은 문자열의 역순으로 개별 문자를 출력해보자.

string=input("문자열 : ")
print("개별 문자 출력 : ",end="")
for i in string:
    print(i,end="")
print()

print("역순 개별 문자 출력 : ", end="")
for i in range(len(string) - 1, -1, -1):
    print(string[i], end="")
print()