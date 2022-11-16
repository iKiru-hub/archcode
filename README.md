# archode

this code is meant to help the visualization of the code structure.

the final product should be something like, when prompted with the
query "One.method_1":


class.One.method_1()

--------- class.Two.method_1()

--------- class.Two.method_2()

------------------ class.Three.method_1()

------------------ class.Three.method_2()

------------------ class.Three.method_3()

class.One.method_2()

class.One.method_3()

--------- class.Two.method_1()


the requirement is the writing a file in which the code is structure as a python dict, 
such that the principal function in archcode.py can build three
