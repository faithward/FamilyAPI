
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        # make sure it doesn't add duplicates
        print("Hello")
        for people in self._members:
            if (member["first_name"] == people["first_name"]):
                return 'Family member already exists'
        member["id"] = self._generateId
        self._members.append(member)
        return 'New family member has been added', 200

    def delete_member(self, id):
        # fill this method and update the return
        for people in self._members:
            if (people["id"] == id):
                self._members.remove(people)
        return self._members

    def get_member(self, id):
        # fill this method and update the return
        for people in self._members:
            if (people["id"] == id):
                return people
        return 'No such family member registered', 404


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
