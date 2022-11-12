
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
        #self.id = self._generateId()

        # example list of members
        self._members = [{
            "first_name": "John",
            "age" : 33,
            "lucky_numbers" : [7, 13, 22],
            "id" : self._generateId()
        },
        {
            "first_name": "Jane",
            "age" : 35,
            "lucky_numbers" : [10, 14, 3],
            "id" : self._generateId()
        },
        {
            "first_name": "Jimmy",
            "age" : 5,
            "lucky_numbers" : [1],
            "id" : self._generateId()
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        # make sure it doesn't add duplicates
        for people in self._members:
            if (member["first_name"] == people["first_name"]):
                return 'Family member already exists'
        self._members.append(member)
        print("New family member has been added")
        return ''

    def delete_member(self, id):
        # fill this method and update the return
        for people in self._members:
            if (people["id"] == id):
                self._members.remove(people)
                print("Family member has been deleted")
                return ''
        return 'No such family member registered'

    def get_member(self, id):
        # fill this method and update the return
        for people in self._members:
            if (people["id"] == id):
                return people
        return 'No such family member registered'


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
