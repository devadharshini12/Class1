from datetime import date
class student:

    def __init__(self,name,gender,mark1,mark2,rank):
        self.name=name
        self.gender=gender
        self.mark1=mark1
        self.mark2=mark2
        self.rank=rank

    def address(self):
        addr=f"Name : {self.name}\nGender : {self.gender}\nmark1 : {self.mark1}\nmark2 : {self.mark2}\nrank : {self.rank}"
        return addr


stu1=student("Dharshini","Female",92,87,5)

print(stu1.address())