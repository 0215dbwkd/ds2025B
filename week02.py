# 실행 할 때는 alt + shift + F10
# 재실행은 ctrl + F5

n = int(input("정수 입력 : "))
result = 0
# for i in range(1, n+1):
#    result = result + i
result = n * (n + 1) // 2 # O(1)
print(result)

# O(n)