"""
Complexity Analysis:
-------------------
Time Complexity:
We need to search through all sub groups and users of all groups.

n = Total number of groups + Total number of users in all groups
TC: O(n)
SC: O(1)


Return True if user is in the group, False otherwise.

Args:
    user(str): user name/id
    group(class:Group): group to check user membership against

n = Total number of groups + Total number of users in all groups
TC: O(n)
SC: O(1)
"""


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

parent.add_group(child)
child.add_group(sub_child)

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)


def is_user_in_group(user, group):
    if user in group.get_users():
        return True

    for group in group.get_groups():
        return is_user_in_group(user, group)

    return False


print(is_user_in_group(sub_child_user, sub_child))  # True
print(is_user_in_group(sub_child_user, child))  # True
print(is_user_in_group(sub_child_user, parent))  # True
print(is_user_in_group("unknown user", sub_child))  # False
print(is_user_in_group("", sub_child))  # False
