import random

answer = random.randint(1, 100)
count = 0

while True:
    count += 1
    while True:
        guess = input(f"숫자 입력 : ")

        try:
            guess = int(guess)
            break
        except:
            print("숫자를 입력해주세요")
            print("")

    print(guess)

    if answer == guess:
        print(f"정답입니다! 당신은 총 {count}번 만에 맞췄습니다.")
        print("")
        break
    elif answer > guess:
        print("입력하신 값은 정답보다 작은 수 입니다. LOW")
    else:
        print("입력하신 값은 정답보다 큰 수 입니다 HIGH.")


