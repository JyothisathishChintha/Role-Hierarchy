class Tree:

    # Constructor get data in 'Tree' class.
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    # Add_SubRole() func adds subroles for given Role.
    def Add_SubRole(self,Subrole,role):
        if self.data is None:
            return
        if self.data == role:
            if self.left:
                self.right = Tree(Subrole)
            else:
                self.left = Tree(Subrole)
        if self.left:
            self.left.Add_SubRole(Subrole,role)
        if self.right:
            self.right.Add_SubRole(Subrole,role)

    # Display_Roles() func print Tree in Breadth First Search(BFS) Traversal.
    # Dislay  every SubRoles in Tree.
    def Display_Roles(self,que=[]):
        if self.data is None:
            return
        if self.left: 
            que.append(self.left.data)
        if self.right:
            que.append(self.right.data)
        if len(que)!=0 :
            if que[0] is not None:
                print(que.pop(0),end= ' ')
            else:
                que.pop(0)
        if self.left: self.left.Display_Roles(que)
        if self.right: self.right.Display_Roles(que)

    # Delete Role in Tree.
    def Delete(self):
        if self.data is None:
            return
        elif self.left is None and self.right is None:
            self.data = None
            return
        elif self.left:
            self.data = self.left.data
            self.left.Delete()
        elif self.right:
            self.data = self.right.data
            self.right.Delete()
        else:
            self.data = self.left.data
            self.left.Delete()
        return

    # After transfered Delete() func calls to delete role.
    def Delete_Role(self,role,transfer_role):
        if self.data == role:
            if self.left is None and self.right is None:
                self.data = None
                return 
            elif self.right is None:
                if transfer_role == self.left.data:
                    self.data = self.left.data
                    self.left = None
                    return 
            elif self.left is None:
                if transfer_role == self.right.data:
                    self.data = self.right.data
                    self.right = None
                    return
            else:
                if self.left.data == transfer_role:
                    self.data, self.left.data = self.left.data, self.data
                    self.left.Delete()
                if self.right.data == transfer_role:
                    self.data, self.right.data = self.right.data, self.data
                    self.right.Delete()
        if self.left: self.left.Delete_Role(role,transfer_role)
        if self.right: self.right.Delete_Role(role,transfer_role)

    # Add_User() func add Users in Tree.
    def Add_User(self,name,role):
        if self.data is None:
            return
        if self.data == role:
            self.data = name+"-"+role
        if self.left: self.left.Add_User(name,role)
        if self.right: self.right.Add_User(name,role)

    # Display_User() func print only Users in Tree.
    def Display_User(self):
        if self.data is None:
            return
        if self.data:
            temp = self.data.split('-')
        if len(temp) == 2:
            print(temp[0]+' - '+temp[-1])
        if self.left: self.left.Display_User()
        if self.right: self.right.Display_User()

    # Sub_Users() func print every SUb_User in Tree.
    def Sub_Users(self):
        if self.data is None:
            return
        if self.data:
            data = self.data.split('-')[0]
            print(data,end=' ')
        if self.left: self.left.Sub_Users()
        if self.right: self.right.Sub_Users()

    # Display_Users_SubUsers() func display user.
    # Also calls Sub_Users() func to  print Sub_Users for particular user.
    def Display_Users_SubUsers(self):
        if self.data:
            temp = self.data.split('-')
            print(temp[0]+' - ',end=' ')
            if self.left: self.left.Sub_Users()
            if self.right: self.right.Sub_Users()
        print('\n')
        if self.left: self.left.Display_Users_SubUsers()
        if self.right: self.right.Display_Users_SubUsers()

    # Delete _User() func delete User in Tree.
    def Delete_User(self,user_name):
        data_name = self.data.split('-')[0]
        if data_name == user_name:
           self.data = data_name[-1]
           return
        if self.left: self.left.Delete_User(user_name)
        if self.right: self.right.Delete_User(user_name)

    # Number_of_users_from_top() func returns level of Tree for given rolename.
    def Number_of_users_from_top(self,name,cnt=0):
        if self is None:
            return 0
        data = self.data.split('-')
        if data[0] == name:
            return cnt
        if self.left: 
            left = self.left.Number_of_users_from_top(name,cnt+1) 
            if left:
                return left
        if self.right: 
            right = self.right.Number_of_users_from_top(name,cnt+1)
            if right:
                return right


# Common_Boss() func return common boss of both users.
# Also known as Least common Ancestor (LCA).
def Common_Boss(root,user_name1,user_name2):
    if root is None:
        return None
    if root.data == user_name1 or root.data == user_name2:
        return root
    left = Common_Boss(root.left,user_name1,user_name2)
    right = Common_Boss(root.right,user_name1,user_name2)
    if right and left:
        return root


# Height() func returns Total Height of Tree.
def Height(root):
    if root is None:
        return -1
    return max(Height(root.left),Height(root.right))+1


# Add_SubRole() func calls Add_SubRole() func in 'Tree' class.
# To add subrole under a Role
def Add_SubRole(bt):
    Sub_role = input("Enter sub role name: ")
    Root_role = input("Enter reporitng role name: ")
    bt.Add_SubRole(Sub_role,Root_role)


# Delete_Role() func calls Delete_Role() in 'Tree' class.
# TO delete subrole.
def Delete_Role(bt):
    delete_node = input("Enter the role to be deleted: ")
    transfer_node = input("Enter the role to be transferred: ")
    bt.Delete_Role(delete_node,transfer_node)


# Add_User() func calls Add_User() func in 'Tree' class.
# To add User 
def Add_User(bt):
    username = input("Enter User Name: ")
    role = input("Enter Role: ")
    if username == '' or role == '':
        print("username and role is must to adduser in desired role\n")
        Add_User
    else:
        bt.Add_User(username,role)


# These are Some Operations...
def User_Operations(bt):
    print("Operations:\n\t1. Add Sub Role.\n\t2. Display.\
        \n\t3 Delete Role.\n\t4. Add User.\
        \n\t5. Display Users.\n\t6. Display Users and Sub Users.\
        \n\t7. Delete User.\n\t8. Number of users from top.\
        \n\t9. Height of role hierarachy.\t\n\t10. Common boss of users.")
    sub_inp = int(input())
    if sub_inp == 1:
        Add_SubRole(bt)
        User_Operations(bt)
    elif sub_inp == 2:
        print(bt.data,end= ' ')
        bt.Display_Roles()
        print('\n')
    elif sub_inp == 3:
        Delete_Role(bt)
        User_Operations(bt)
    elif sub_inp == 4:
        Add_User(bt)
        User_Operations(bt)
    elif sub_inp == 5:
        bt.Display_User()
    elif sub_inp == 6:
        bt.Display_Users_SubUsers()
    elif sub_inp == 7:
        username = input("Enter user to be deleted: ")
        bt.Delete_User(username)
        User_Operations(bt)
    elif  sub_inp == 8:
        rolename = input("Enter role name: ")
        res = bt.Number_of_users_from_top(rolename)
        print(f"Number of users from top: {res}")
    elif sub_inp == 9:
         print(f"Height - {Height(bt)}")
    elif sub_inp == 10:
        name1 = input("Enter user 1: ")
        name2 = input("Enter user 2: ")
        res = Common_Boss(bt,name1,name2)
        if  res is not None:
            print(f"Top most common boss: {res.data}")
        else:
            print(f"{res}\n")
            User_Operations(bt)
    else:
        print('invalid option\n')
        User_Operations(bt)


# Role_Hierarchy() func is main func to create Role Hierarchy.
def Role_Hierarchy():
    User_inp = input("Enter root role name: ")
    if User_inp == '' or User_inp.isspace():
        print("Root role name cannot be Null ")
        Role_Hierarchy()
    else:
        bt = Tree(User_inp)
        User_Operations(bt)


# Built-in main() func.
if __name__ == '__main__':
    Role_Hierarchy()


'''
    There are some Limitations and Bugs are there.
    Some of them are...
        = There are atmost 2 child nodes are possible because
            we are using Binary tree DS.
        - We can't add more than 1 user for desired roles.
'''

