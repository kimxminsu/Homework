string=input("문자열 : ")
print("개별 문자 출력 : ",end="")
for i in string:
    print(i,end="")
print()

print("역순 개별 문자 출력 : ", end="")
for i in range(len(string) - 1, -1, -1):
    print(string[i], end="")
print()