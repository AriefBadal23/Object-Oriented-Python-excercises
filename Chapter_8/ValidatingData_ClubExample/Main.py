# Club example main program

from Club import *

# Create a club at most 5 members

oProgrammingClub = Club('Programming', 5)

oProgrammingClub.add_member('Joe Schmoe')
oProgrammingClub.add_member('Cindy Lou hoo')
oProgrammingClub.add_member('Dino Richmond')
oProgrammingClub.add_member('Susie Sweetness')
oProgrammingClub.add_member('Fred Farkle')

# You can still change the maximum value of the max_members instance variable
# Which is not best practice
# oProgrammingClub.max_members=300

oProgrammingClub.report()

# Attempt to add additional member
oProgrammingClub.add_member('Iwanna Join') 
