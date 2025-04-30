# list 자료형
# [, ]
# 변경 및 중복 가능
# 인덱스 접근 가능
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = sum(numbers)
print(total)

# tuple 자료형
# ( , )
# 변경 불가능
# 중복 가능
# 인덱스 접근 가능
data = (10, 20, 30, 40)
print(data[0], data[3])


# dictionary 자료형
# {'이름': 키, }
# 변경 가능
# 중복 불가능
person = {'Taylor': 20, 'Olivia': 24, 'Bruno': 40}
name = 'Olivia'
# f-string 이용
print(f"{name}'s age is {person[name]}")
print(f'{name}의 나이는 {person[name]}살 입니다.')

# set 자료형
# {, }
# 집합 -> 순서가 없고 중복된 값을 허용하지 않음
lst = [1, 2, 3, 4, 4, 5, 5, 6]
unique_numbers = set(lst)
print(unique_numbers)

### set을 다시 list로 만들려면 list()함수 이용
unique_numbers = list(unique_numbers)
print(unique_numbers)

### 괄호 없이 출력하려면 print(*변수)
print(*unique_numbers)
### 구분자도 변경 가능
print(*unique_numbers, sep=', ')

####################################

# enumerate
# 리스트 각 항목을 튜플(인덱스, 값)로 반환
fruits = ['apple', 'banana', 'cherry']
for index, _ in enumerate(fruits):
    print(f'Index = {index}')

for index, value in enumerate(fruits):
    print(f'Index {index} = {value}')

for _, value in enumerate(fruits):
    print(f'Value = {value}')

# lambda 함수


