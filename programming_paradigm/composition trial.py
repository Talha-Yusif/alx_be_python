class Member:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Library:
    def __init__(self):
        self.members=[]
    def add_member(self,member):
        self.members.append(member)
    def list_all_members(self):
        for member in self.members:
            print(f"name={member.name} has id of{member.id}")

member1=Member("prince",45678)
member2=Member("cream",90890)
member3=Member("kofi",11111)

shelf=Library()
shelf.add_member(member1)
shelf.add_member(member2)
shelf.add_member(member3)

shelf.list_all_members()
print(shelf.list_all_members())

