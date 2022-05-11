# Club class

class Club():
    def __init__(self, clubname, max_members):
        self.clubname = clubname
        self.max_members = max_members
        self.member_list = []

    
    def add_member(self, name):
        # Make sure that there is enough room left
        if len(self.member_list) < self.max_members:
            self.member_list.append(name)
            print('Ok.', name, 'has been added to the', self.clubname, 'club')

        else:
            print('Sorry but we cannot add', name, 'to the', self.clubname, 'club.')
            print('This club already has the maximum of', self.max_members, 'members.')

    def report(self):
        print()
        print('Here are the', len(self.member_list), 'members of the', self.clubname, 'club:')
        for name in self.member_list:
            print(' ' + name)
        print()