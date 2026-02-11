# Class Statement General Format
# Count 1
# Server side code: Definition of class 
class class_name:
    def __init__(self, other_initialization_parameters):
        self.attr_name_1 = attr_value_1
        self.attr_name_2 = attr_value_2
        .
        .
        .
        self.attr_name_N = attr_value_N

    def method_1(self, other_formal_parameters_if_any):
        definition of method 1

    def method_2(self, other_formal_parameters_if_any):
        definition of method 2

    .
    .
    .
    def method_K(self, other_formal_parameters_if_any):
        definition of method K

# Client Side Code -> Code which creates object from class and invokes class methods on it 
object_1_name = class_name(initialization_data)
object_1_name.method_1(input_data)
.
.
.
object_1_name.method_K(input_data)
#----------------------------------------------------------
# count 2
# Server Side Code -> Class definition
class class_name:
    def __init__(self, other_initialization_data_if_any):
        self.attr_1_name = attr_value_1
        self.attr_2_name = attr_value_2
        .
        .
        .
        self.attr_K_name = attr_value_K

    def method_1(self, other_formal_parameters_if_any):
        definition of method 1

    def method_2(self, other_formal_parameters_if_any):
        definition of method 2

    .
    .
    .
    def method_K(self, other_formal_parameters_if_any):
        definition of method K

object_name = class_name(initialization_data)
object_name.method_1(input_data)

.
.
object_name.method_K(input_data)
#------------------------------------------------------------
# Count 3
class class_name:
    def __init__(self, other_initialization_data_if_any):
        self.attr_1_name = attr_value_1
        self.attr_2_name = attr_value_2
        .
        .
        .
        self.attr_N_name = attr_value_N

    def method_1(self, other_input_data_if_any):
        definition of method_1

    .
    .
    .

    def method_K(self, other_input_data_if_any):
        definition of method K


object_name = class_name(initialization_data)
object_name.method_1(input_data)

.
.
.
object_name.method_K(input_data)

# Count 4
class class_name:
    def __init__(self, other_initialization_parameters_if_any):
        self.attr_1_name = attr_value_1
        self.attr_2_name = attr_value_2
        .
        .
        .
        self.attr_N_name = attr_value_N


    def method_1(self, other_input_parameters_if_any):
        definition of method 1

    .
    .
    .

    def method_K(self, other_input_parameters_if_any):
        definition of method K


object_name = class_name(initialization_data)
object_name.method_1(input_data)

.
.
object_name.method_K(input_data)

# count 5

class class_name:
    def __init__(self, other_initialzation_data_if_any):
        self.attr_1_name = attr_value_1
        self.attr_2_name = attr_value_2
        .
        .
        .
        self.attr_N_name = attr_value_N

    def method_1(self, other_input_parameters_if_any):
        definition of method 1

    .
    .
    .

    def method_K(self, other_input_parameters_if_any):
        definition of method K


object_name = class_name(initialization_data)
object_name.method_1(input_data)
.
.
.
object_name.method_K(input_data)




