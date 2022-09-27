class Sample():
    n_objects = 0 # this is a class variable
    def __init__(self, name):
        self.name = name
        Sample.n_objects = Sample.n_objects + 1

    def get_object_count(self):
        print('There are', Sample.n_objects, 'Sample objects')
        
    def __del__(self):
        Sample.n_objects = Sample.n_objects - 1


# Instantiate 4 objects
oSample1 = Sample('A')
oSample2 = Sample('B')
oSample3 = Sample('C')
oSample4 = Sample('D')


# Delete 1 object
del oSample3

# See how many we have
oSample1.get_object_count()
