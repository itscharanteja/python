class cla1:
    def __init__(self,id,name):
        print("New object is being created..!")
        self.id = id
        self.name = name
        self.follower = 0
        self.following = 0
        



    def follow(self,user):
        user.follower += 1
        user.following += 1
        
user1 =  cla1(501,'charan')
user2 = cla1(502,'groot')
user2.follow(user1)
user2.follow(user1)

# a.user = "Charan"
# a.id = "502"
# print(a.id,'\n',a.name)
# print(a.follower)
# b = cla1()
print(user1.follower)
print(user1.following)
print(user2.follower)
print(user2.following)

# b.user = "groot"
# b.id = "503"

# print(b.id)