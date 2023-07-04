'''
# 문자열 
문자,단어로 구성된 문자들의 집합
-------------------------------------------------
# 문자열을 만드는법은 4개로 구성

1. 큰따옴표로(")양쪽 둘러 싸기
"I need Python"

2. 작은따옴표(')양쪽 둘러 싸기
'Python World'

3. 큰따옴표 3개를 연속(""")로 양쪽 둘러싸기
"""Life is too short, You need Python"""

4. 작은 큰따옴표 3개를 연속'''()
'''Life is too short, You need Python'''
'''
-------------------------------------------------
# 문자열에 작은따옴표나 큰따옴표를 포함이 필요할때

1.문자열에 작은 따옴표 (') 포함시키기
"Python's Very Easy"
# 1번은 위와같이 왼쪽과 오른쪽에 " " 포함 하면 된다.

2.문자열에 큰 따옴표 (") 포함시키기
'"Python is Amazing" he says.'
# 2번은 위와같이 1번과같이 표현하면 된다.

3. 백슬래시(\)를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함시키기
'Python\' is diverse'
# 3번은 백슬래시뒤에 ',"는 문자열을 둘러싸는 기호의 의미가 아니게되어 문자 그자체가 된다.
'''
'''
------------------------------------------------
# 여러줄인 문자열을 변수에 대입하고 싶을때

1. 줄을 바꾸는 이스케이프 코드 '\n' 사용
a = "Life is Short\n You need python"
print(a)

2. 연속된 작은 따옴표 3개 또는 큰따옴표 3개 사용하기
------------------------------------------------
# 문자열 연산

1. 문자열 더해서 연산하기
a = "I need"
b = "Python!"
print(a + b)

2. 문자열 곱하기
a = "I Love Python"
print(a * 5)
-----------------------------------------------
# 문자열 길이 구하기(len)

a = "Earth Class"
len(a)
------------------------------------------------
#문자열 인덱싱 과 슬라이싱
인덱싱은 가르킨다는 의미, 슬라이싱은 무엇을 잘라낸다는 의미
-----------------------------------------------
# 인덱싱
a = "I love you. And you?"
a[1] = 
a[-4] = y

# 슬라이싱
a = "I love you. And you?"
a[2:6] = 'love'
a[2:] = "love you. And You?"
a[-6:-11] = 'A .uoy'
a[:] = "I love you. And You?"
a[2:6:2] = "lv"
---------------------------------------------------
# 문자열 포매팅
문자열 안에 어떤값을 삽입 하는 방법

1. 숫자 바로 대입
"I Eat %d Candys" % 5

2. 문자열 바로 대입
"I Eat %s Candys" % Five

3.숫자 값을 나타내는 변수로 대입
num = 5
"I Eat %d Candys" % num

4. 2개 이상의 값 넣기
num = five
day = "30"
"I studied for %s days. As a result, I gained %d kg." % (day,num)
---------------------------------------------------------------
# 포매팅 활용

1. 정렬과 공백
"%15s" % "hello"
# 전체길이가 15개인 문자열 공간에서 hello가 오른쪽으로 정렬 
"%-15s" % "hello"
# 전체길이가 15개인 문자열 공간에서 hello가 왼쪽으로 정렬

2. 소수점 표현하기
"%0.2f % 1.2352346347
# 소수점을 2자리까지만 표시

"%14.2f % 1.2352346347
# 소수점을 2자리까지만 표시하고 전체길이가 14개인 문자열 공간에서 오른쪽으로 정렬

"%-14.2f % 1.2352346347
# 소수점을 2자리까지만 표시하고 전체길이가 14개인 문자열 공간에서 왼쪽으로 정렬
----------------------------------------------------------------
# format 함수를 사용한 포매팅

1. 숫자 바로 대입하기
"I eat {0} Banana".format(3)

2. 문자열 바로 대입하기
"I eat {0} Banana".format("five")

3. 숫자 값을 가진 변수로 대입하기
num = 5
"I eat {0} Banana".format(num)

4. 2개 이상의 값 넣기
num = 10
day = "Five"
"I ate {0} bananas in {1} days.".fomrat(num,day)

5. 이름으로 넣기
"I ate {num} bananas in {day} days."format(num = 10, day = 5)

6. 인덱스와 이름 혼용해서 넣기
" I ate {num} bananas in {1} days.format(num = 10, 5)

7. 오른쪽 정렬
"{0:>15}".format("Hello")

8. 왼쪽 정렬
"{0:<15}".format("Hello")

9. 가운데 정렬
"{0:^15}".format("Hello")

10. 공백 채우기"
"{0:★^15}".format("Hello")

11. 소수점 표현하기
s = 3.4656789
"{0:0.2f}".format(s)
s = 3.4656789
"{0:12.2f}".format(s)

12. 문자 표현하기
"{{Love}}".format()
--------------------------------------------
# f 문자열 포매팅 (버전 3.6부터 가능하며 문자열앞에 f 접두사 붙이면 기능 사용 가능)

name = "Park Sung Min"
age = 24
f'나의 이름은{name}입니다. 나이는 {age}입니다.'

age = 24
f'나는 내년이면 {age+1}살이 됩니다.

d = {'name:'박성민', 'age':24}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

f'{"hello":<15}

f'{"hello":^15}

f'{"hello":>15}

f'{"hello":☆15}

f'{"hello":★15}

s = 3.4656789
f'{0:0.2f}'

s = 3.4656789
f'{s:0.2f}'

s = 3.4656789
f'{s:10.2f}'

f'{{love}}'
-------------------------------------------------------
# 문자열 관련 함수(count,find,index,join,upper,lower,lstrip,strip,rstrip,replace,split)

# count
s = "Lotte
s.count(t)

# find
a = "sanck is the dealicious"
a.find(s)
# 만약 찾는 문자나 문자열 존재하지않으면 -1

# index
a = "sanck is the dealicious"
a.index(s)
# 만약 찾는 문자나 문자열 존재하지않으면 오류를 띄운다.

# join
",".join("asdf")

# upper
a = "hello"
a.upper()

# lower
a = "HELLO"
a.lower()

# lstrip
a = "     hello"
a.lstrip()

# rstirp
a = "hello      "
a.rstrip()

# strip
a = "          hello        "

# replace
a = "Life is too short"
a.replace("Life", "Time")

# split
a = "Time is too short"
a.split()
# 공백을 기준으로 문자열을 나눔
a.split(:)
# : 기준으로 문자열을 나눔
'''