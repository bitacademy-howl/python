# Q4
# 파일명은 quiz02_4.py로 합니다.
# 다음과 같이 문자열이 설정되어 있습니다.

# 문자열에서 ',', '.', '\n'을 제거하고 모두 대문자로 변경합니다.
# 변경된 소스를 기반으로 단어의 빈도수를 체크해 봅시다.
# (실행 결과 예시)
# WE: 1
# ENCOURAGE: 1
# EVERYONE: 1
# TO: 3
# CONTRIBUTE: 1
# PYTHON: 2
# IF: 1
# ...

s = """We encourage everyone to contribute to Python. 
If you still have questions after reviewing the material
in this guide, then the Python Mentors 
group is available to help guide new contributors through the process."""

print(s)
s.strip()

