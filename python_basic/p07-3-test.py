#학생 번호와 이름이 리스트로 주어졌을 때 학생 번호를 입력하면 학생 번호에 해당하는 이름을 순차 탐색으로 찾아 돌려주는 함수

#def search_dict(d, no):

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]
d = dict(zip(stu_no, stu_name))
print(d)
print(d[39])
print(d["John"])
