a = range(10)

result = [num * 3 for num in a]

print(result)

# a.map(n => n * 3)
# 이게 더 가독성이 좋은데
# 맵 함수가 있으리라 생각

result = [num * 3 for num in a if num % 2 == 0]
print(result)
# a.filter(n => n % 2).map(n => n * 3)
# n => 도 생략 가능할텐데

# 한줄로 짜는 비둘기 코드가 바로 이것인가
result = [x*y for x in range(2, 10) for y in range(1, 10)]
print(result)
