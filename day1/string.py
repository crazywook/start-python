# 위치 찾기
a = 'I am Iron Man'
print('find r: ', a.find('r'))
print('index r: ', a.index('r'))
print('find', a.find('w'))
# this will invoke error
# print('index', a.index('w'))
# 문자열 삽입
a = ','
# 객체와 파라메터가 바껴야 할 것 같은 기분이지만
print(a.join('avengers'))
