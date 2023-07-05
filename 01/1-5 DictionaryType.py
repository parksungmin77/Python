'''
# 딕셔너리(사전) Key와 Value를 한쌍으로 갖으며 Key를 통해 Value값을 얻을수있다. Key는 변경 불가
# {Key1:Value1, Key2:Value2, .......}
# dic = {"name" : "Jame", "birth" : "0214 "}

# 딕셔너리 쌍 추가 삭제 하기

1. 딕셔너리 쌍 추가 하기
a = {1 : 'a'}
a[2] = 'b'
# {2 : 'b'} 추가

2. 딕셔너리 요소 삭제 하기
a = {1 : 'a'}
del a[1]
# Key가 1인 Key:value 쌍 삭제
-----------------------------------------------------------------
# 딕셔너리에서 Key를 사용해 Value 얻기

money = {'지폐' : 1000, '동전' : 500}
money['지폐']

# 주의! Key는 고유의 값으로 한번 설정해두면 나머지것이 모두 무시된다

a = {1 : 'c', 1 : 'd' }
# {1 : 'd'}값이 무시됨
----------------------------------------------------------------------
# 딕셔너리 관련 함수

1. Key 리스트 만들기(keys)
a = {'name' : 'park', 'phone': '00312416754', 'birth':'1204'}
a.keys()
# 딕셔너리 a의 키만을모아 dict_keys 객체를 돌려준다.

# dict_keys 를  리스트로 변환
list(a.keys())

2. Value 리스트 만들기(values)
a.values()
# 딕셔너리 a의 Value만을 모아 dict_values 객체를 돌려준다.

3. Key,Value 쌍 얻기(items)
a.items()

4. Key:Value 쌍 모두 지우기(clear)
a.clear()
# 딕셔너리 a 에 모든 요소를 삭제하니 주의! {} 로 표기된다.

5. Key로 Value 얻기(get)
a = {'name' : 'park', 'phone' : '01653021', 'birth' : '0712'}
a.get('phone')
a.get('name')
# 만일 존재하지 않는 Key를 부를경우 None, 오류가 발생 된다.
# 그러나 존재하지 않아도 미리 정해둔 디폴드 값을 쓰면 편리하다.
a.get('foo','bar')
a.get('far','snow')
# 위 딕셔너리에는 'foo','far'가 없어서 대신 디폴트 값인 'bar', 'snow'를 돌려준다.

6. 해당 Key가 딕셔너리 안에 있는지 찾기(in)
a = {'name' : 'park', 'phone' : '01653021', 'birth' : '0712'}
'name' in a
'index' in a
# 없으면 False, 있으면 True 로 출력된다.
'''