
#Import the datetime embedded module and display the namespace of this module (sorted alphabetically) 
# as given below.

import datetime

for name in sorted(datetime.__dict__):
    print(name)
