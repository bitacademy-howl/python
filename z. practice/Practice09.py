# 문제9.
# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.
#
# <<실행결과>>
#
# 입력> Java Programming!
# 결과> !gnimmargorP avaJ

# def reverse(s):
#     reversedS = ''
#     for i in range(i, len(s)):
#         reversedS = reversedS + s[(len(s)-i)-1:len(s)-i]
#     return reversedS

def reverse(s):

    reversedS = ''

    for i in range(len(s), 0, -1):
        reversedS = reversedS + s[i-1:i]

    return reversedS



s = input("입력 > ")
print("결과 > " + reverse(s))