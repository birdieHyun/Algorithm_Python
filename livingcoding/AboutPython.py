a = 1
print(a)

a = int(1e9)  # 10억
print(a)

a = 0.3 + 0.6
print(round(a, 2))

print(2 ** 3)  # 2의 세제곱

print(2 ** 0.5)  # 2의 제곱근

##############################

# 리스트 자료형

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 인덱스
#    0,1,2,3,4,5,6....
#    -9, -8, -7 .....-1
# '-' 는 거꾸로 간다.


print(a)

n = 10
# a = [0] * n
print(a)

# 인덱싱
print(a[2])

print(a[-1])

# 리스트의 인덱싱과 슬라이싱
# 연속적인 위치를 갖는 원소들을 가져와야 할 때는 슬라이싱을 이용
# 시작인덱스부터 끝 인덱스를 설정 -> 끝 인덱스는 실제 인덱스보다  1크게 설정한다.

print(a[0:3])  # 0 ~ 2 인덱스의 값을 가져온다.

# 리스트 컴프리헨션
# 리스트를 초기화 하는 방법
# 대괄호 안에 조건문과 반복문을 적용하여 리스트 초기화
# 0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 위의 코드를 구현하면
a = []
for i in range(20):
    if i % 2 == 1:
        a.append(i)
print(a)

# 1부터 9까지의 수들을 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 20)]

print(array)

# 리스트 컴프리헨션은 2차원 리스트를 초기화할때 효과적으로 사용될 수 있다.
# 특히 N x M 크기의 2차원 리스트를 한번에 초기화 할 때 매우 유용하다.
# 좋은 예시 : array = [[0] * m for _in range(n)]

# 잘못된 예시 : array = [[0] * m ] * n

# _(언더바)의 경우 for문에서  i 를 쓰지 않는 것과 같은 것
# append, sort, reverse, insert, count, remove 등의 기타 메서드가 있다.

# 리스트 관련 기타 메서드
a = [1, 4, 3]
print("기본 리스트: ", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입", a)

# 오름차순 정렬
a.sort()
print("오름차순  :", a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 : ", a)

# sort 와 sorted 의 차이
# sort 는 리스트 자체를 정렬, sorted 는 리스트를 정렬한 수 반환 즉 sorted는 리스트의 값이 바뀌지 않음

a = [5, 4, 3, 2, 1]
b = [5, 4, 3, 2, 1]
a.sort()
result = sorted(b)

print("sort : ", a)
print("sorted : ", result)
print("b : ", b)

# 리스트에서 특정 값의 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# 파이썬의 경우 removeAll이 없어서 이렇게 작성한다.
# remove 메서드의 경우 하나의 값만  지우기 때문
result = [i for i in a if i not in remove_set]
print(result)

####################
# 문자열 자료형
# 파이썬은 ' 나 "  둘 다 사용할 수 있다.
# " 로 시작하면 "" 안에서 ' 는 그냥 출력 가능하다
# " 안에 " 를 넣고싶은 경우 \" 를 하면 된다.

data = 'hello world'
print(data)

data = "Don't tou know \"python\"?"
data = "Don't tou know 'python'?"

print(data)

#

a = "hello"
b = "world"

print(a + b)

print(a * 3)

# 슬라이싱도 가능하다.
a = "ABCDEF"
print(a[2:4])

################
# 튜플
# 튜플 자료형은 리스트와 유사하지만 한번 선언된 값을 변경할 수 없다, 리스트에 비해 상대적으로 공간효율적이다.
# 리스트는 [] (대괄호)를 사용하지만, 튜플은 () 소괄호 를 사용한다.
a = (1, 2, 3, 4)
print(a)

# a[2] = 7 이러면 에러가 발생한다.

###############
# 사전 자료형
# 키와 값을 쌍으로 데이터로 가지는 자료형
# 변경 불가능한 자료형을 키로 사용할 수 있다.
# 파이썬의 사전 자료형은 해시테이블을 이용하므로, 데이터의 검색 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.

data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 키 데이터만 뽑아서 리스트로 이용할 때는 keys() 함수를 이용
# 값 데이터만을 뽑아서 리스트로 이용할 땐 values() 함수를 이용

###########################
# 집합 자료형
# 중복을 허용하지 않고, 순서가 없다.
data = set([1, 1, 2, 3, 4, 4, 5])
print("중복을 허용하지 않는 셋")
print(data)

# 중괄호를 이용하여 처리할 수도 있다.
data = {1, 2, 3, 3, 4, 5, 5, 5, 5}
print(data)

# 집합이기 때문에 합집합, 교집합, 차집합 연산이 있다.

# 새로운 원소 추가
data = set([1, 2, 3])
data.add(4)
print(data)

# 새로운 원소 여러개 추가
data.update([5, 6])
data.update({7, 8})
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

# 기본 입출력
# 모든 프로그램은 적절한(약속된) 입출력 양식을 가지고 있다.
# 프로그램 동작의 단계는 데이터를 입력받거나 생성하는 것

# 자주 사용되는 표준 입력 방법
# input() 함수는 한 줄의 ㅁ누자열을 입력받는 함수
# Map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용한다.
# 예시) 공백을 기준으로 구분된 데이터를 입력 받을때는 다음과 같이 사용한다.
# list(map(int, input().split()))

# 예시) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용한다.
# a, b, c = map(int, input().split())


# a,b,c,d,e = map(int, input().split())
# data = list(map(int, input().split()))

# print(data)
# print(a, b, c, d, e)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

'''
2차원 배열의 경우 
3 x 4 일 때 
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
이렇게 들어온다면 
'''

# n = int(input())
# m = int(input())
#
# arr =[]
# for i in range(n):
#     arr.append(list(map(int, input().split())))
#
# print(arr)

''' 
빠르게 입력 받기 
사용자로부터 입력을 최대한 빠르게 받아야 하는 경우 가 있을때 
파이썬의 경우 sys라이브러리에 정의되어 있는 sys.stdin.readLine() 메서드를 사용 
단 입력 후 엔터가 줄바꿈 기호로 입력되므로 retrip() 메서드를 함께 사용한다. 

예를 들어 입력 받는 개수가 천만개다. 이러면 readLine()을 쓰는 것이 효율적
그래프 등에서 사용 
'''

import sys

# data = sys.stdin.readLine().rstrip()
print(data)

'''
파이썬에서 기본 출력은 print() 함수를 이용 
각 변수를 콤마, 를 이용하여 띄어쓰기로 구분하여 출력할 수 있다.  
print()는 기본적으로 출력 이후에 줄바꿈을 수행하지만, 원치 않을 경우 end 속성을 이용할 수 있다. 
'''
a = 1
print(a, end=' ')
print(2)
# 이러면 줄바꿈을 하지 않는다.

'''
print 내에서는 같은 자료형만 출력 가능 
print('hello' + 7) -> 에러 발생
'''
print('hello' + str(7))

# 이렇게 캐스팅을 해주면 된다.

'''
조건문 
조건문은 프로그램을 작성할 때 프로그램의 흐름을 제어하는 문법 
조건문을 이용해 조건에 따라 프로그램의 로직을 설정할 수 있다. 
'''

x = 15
if x > 10:
    print(x)

''' 
성적 구간에 따른 학점 출력 
'''

score = 90

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")

'''
파이썬에서는 코드의 블록을 들여쓰기로 지정한다. 
상당수 파이썬 커뮤니티에서는 4개의 공백 4개를 사용하는 것이 사실상이 표준이다. 
'''

'''
비교연산자 자바랑 똑같다. 
'''

a = 7

if a < 10 and a > 0:
    print(a)

if 0 < a < 10:
    print(a)

# 두번째 처럼 해도 되는데, 첫번째 방법 사용하도록 다른 언어와의 헷갈림 때문에

'''
파이썬의 기타 연산자 
여러개의 데이터를 담는 자료형을 위해 in 연산자와 not in 연산자가 제공 
리스트, 튜플, 문자열, 딕셔너리 모두 사용 가능 
x in 리스트 : 리스트 안에 x 가 들어가 있으면 참 
x not in 리스트 : 리스트 안에 x 가 들어가 있지 않으면 참 
'''

'''
조건문이 참일때 아무것도 처리하고 싶지 않으면 pass 키워드를 사용 
'''

a = 2
print(a)
if a == 1:
    pass  # 나중에 작성하고 싶은 경우 사용하는 경우도 있다.
else:
    print(10)

print("끝")

'''
조건문의 간소화 
조건문에서 실행될 코드가 한줄인 경우 줄바꿈 안해도 된다. 
'''

score = 85

result = "합격" if score > 50 else "불합격"

print(result)

# 이렇게 한줄로 작성할 수도 있다.

'''
반복문 
특정한 소스코드를 반복적으로 실행하고자 하 ㄹ때 사용 
while 과 for문 있는데 어떤것을 사용해도 무관하다.  

다만 코딩테스트에서는 for문이 더 간결 

'''

# 1부터 9까지 각 정수의 합 구하기
i = 1
result = 0

while i <= 9:
    result += i
    i += 1

print(result)

'''
for문 

for문의 구조는 다음과 같은데, 특정한 변수를 이용하여 in 뒤에 오는 자료형(리스트, 튜플 등)에 포함되어 있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문 

for 변수 in 리스트: 
    실행할 소스코드
'''

'''
for문에서 수를 차례대로 나열할 때는 range()를 주로 이용한다. 
이때 range(시작 값, 끝 값) 형태로 사용한다. 
인자를 하나만 넣으면 자동으로 0부터 시작 
'''

result = 0
for i in range(3, 9):  # 3부터 8까지 더한다.
    result += i

print(result)

# for 문에는 스텝도 있다.
for i in range(1, 10, 2):
    print(i)

# 1부터 9까지 2칸씩 뛰면서 출력한다.

# 학생들의 합격 여부 판단 예시
score = [90, 85, 77, 64, 97]
for i in range(5):
    if score[i] > 70:
        print(i + 1, "번 학생은 합격입니다")

# 특정 번호 학생은 제외하기
print("특정 번호 학생은 제외하기")

score = [90, 85, 77, 64, 97]
cheating_student_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_student_list:
        continue
    if score[i] > 70:
        print(i + 1, "번 학생은 합격입니다")

'''
함수 
내장 함수 : 파이썬이 기본적으로 제공하는 함수 
사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수 
'''

'''
프로그램에서 똑같은 코드가 반복적으로 사용되어야 할 때가 많다. 
함수를 사용하면 소스코드의 길이를 줄일 수 있다. 

def 함수명(매개변수):
    실행할 소스코드
    return 반환값
'''

'''
더하기 함수 예시 

def add(a, b):
    return a + b
'''


def add(a, b):
    return a + b


print(add(1, 2))

# 리턴값이 없어도 된다.

# 파라미터의 값을 직접 지정해줄 수 있다.
print(add(b=3, a=7))

'''
global 키워드 

global 키워드로 변수를 지정하면 해당 함수에서는 지역 함수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다. 
'''

a = 0


def func():
    global a
    a += 1


print(a)
func()
print(a)

'''
파이썬에서 함수는 여러개의 반환값을 가질 수 있다. 
'''


def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var


a, b, c, d = operator(7, 3)
print(a, b, c, d)

'''
람다 표현식 
특정한 기능을 수행하는 함수를 한줄에 작성할 수 있다.
'''


def add(a, b):
    return a + b


# 일반적인 add 메서드 사용
print(add(3, 7))

# 람다 표현식 사용 정렬에서 많이 사용된다.
print(lambda a, b: a + b(3, 7))

# 실제로 이렇게는 쓰이지 않고 다음과 같이 쓰인다.
array = [('홍길동', 50), ('이순신', 32), ('아무개', 20)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key= lambda x: x[1]))

# 여러개의 리스트에 적용
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a, b: a + b, list1, list2)
print(list(result))





'''
특히 유용한 표준 라이브러리 

내장 함수 : print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브버리 

itertools: 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브버리, 순열과 조합 라이브러리를 제공 

heapq : 힙(Heap) 기능을 제공하는 라이브러리, 우선순위 큐 기능을 구현하기 위해 사용한다. 

bisect : 이진 탐색 (Binary Search) 기능을 제공하는 라이브러리 

collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함한 라이브러리 
'''

# 자주 사용되는 내장 함수

# sum()
result = sum([1,2,3,4,5])
print(result)


# min(), max()
result = min([1,2,3,4,5])
print(result)

result = max([1,2,3,4,5])
print(result)

# eval()
result = eval("(3+5) * 7")
print(result)

###############################

'''
순열과 조합 
모든 경우의 수를 고려해야 할 때 어떤 라이브러리를 효과적으러로 사용할 수 있을까? 

순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것 
    - {'A', 'B', 'C'} 에서 세 대를 선택하여 나열하는 경우 'ABC', 'ACB' .... 

조합 : 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것 
    - {'A', 'B', 'C'} 에서 순서 고려하지 않고 두개를 뽑는 경우 -> 'AB' 'AC' ......
    
'''
# 순열

from itertools import permutations

data = {'A', 'B', 'C'}

result = list(permutations(data, 3))
print(result)


# 중복 순열과 중복 조합

from itertools import product

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

from itertools import  combinations_with_replacement

result = list(combinations_with_replacement(data,2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)

