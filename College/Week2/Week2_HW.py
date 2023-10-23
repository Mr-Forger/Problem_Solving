#회문 검사
#입력한 문자열이 회문이면 Yes와 처음부터 중간까지의 문자 출력
#아니면 No와 원래의 문자열에 순서를 뒤집은 문자열을 연결하여 만든 회문 출력

text = input("문자를 입력하세요: ")

def palindrome(text):
    for i in range(len(text)//2):
        if text[i] != text[-i - 1]:
            return False
    return True


if palindrome(text):
    print("Yes")
else:
    print(f"No {text}{text[::-1]}")



