import os

r = os.system("ls")
print("---")
f = os.popen("ls", "w")
# 바로 파일을 생성할 수가 없다. 파일명 지정이 없기 때문에
# w는 의미가 있는가?
# if (f.writable):
#   print(f.write())
