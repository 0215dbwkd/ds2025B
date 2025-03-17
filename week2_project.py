import random

answer = random.randint(1, 100)
win = False

for guesses in range(3, 0, -1):

    while True:
        guess = input(f"{guesses}번의 기회가 남았습니다. 숫자 입력 : ")

        try:
            guess = int(guess)
            break
        except:
            print("숫자를 입력해주세요")

    print(guess)

    if answer == guess:
        print("정답입니다!")
        print("")
        win = True
        break
    elif answer > guess:
        print("입력하신 값은 정답보다 작은 수 입니다. LOW")
    else:
        print("입력하신 값은 정답보다 큰 수 입니다 HIGH.")

if win:
    print("당신이 이겼습니다!")
else:
    print(f"당신이 졌습니다. 정답은 {answer}입니다.")
