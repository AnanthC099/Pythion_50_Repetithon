'''
We are implementing a positional vector in Three Dimensional Euclidean Space 
'''

class Vector3D: 
    def __init__(self, x:float, y:float, z:float): 
        acceptable_types = [int, float]
        if type(x) not in acceptable_types or type(y) not in acceptable_types or type(z) not in acceptable_types:
            raise TypeError('Bad type: for initialization data')
        self.x, self.y, self.z = x, y, z 

    def add(self, other): 
        if type(self) is not Vector3D or type(other) is not Vector3D: 
            raise TypeError('Bad type')
        x_sum = self.x + other.x 
        y_sum = self.y + other.y 
        z_sum = self.z + other.z 
        v_sum = Vector3D(x_sum, y_sum, z_sum)
        return v_sum 

    def subtract(self, other): 
        if type(self) is not Vector3D or type(other) is not Vector3D: 
            raise TypeError('Bad type')
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def mod(self): 
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5 

    def normalize(self): 
        N = self.mod() 
        if N == 0.0: 
            raise ValueError('Zero vector cannot be normalized')
        return Vector3D(self.x/N, self.y/N, self.z/N)

    def dot(self, other): 
        if type(self) is not Vector3D or type(other) is not Vector3D: 
            raise TypeError('Bad type')
        return (self.x * other.x + self.y * other.y + self.z * other.z)

    def show(self): 
        print(f'({self.x})i+({self.y})j+({self.z})k')

    def cross(self, other):
        x_cross = self.y * other.z - self.z * other.y
        y_cross = self.z * other.x - self.x * other.z
        z_cross = self.x * other.y - self.y * other.x
        return Vector3D(x_cross, y_cross, z_cross)

#-----------------------CLIENT SIDE CODE-----------------------------------

V1 = Vector3D(1.0, 2.0, 3.0)
V2 = Vector3D(4.0, 5.0, 6.0)

print('--- Vector V1 ---')
V1.show()

print('\n--- Vector V2 ---')
V2.show()

# Addition
V_add = V1.add(V2)
print('\n--- V1 + V2 ---')
V_add.show()

# Subtraction
V_sub = V1.subtract(V2)
print('\n--- V1 - V2 ---')
V_sub.show()

# Magnitude
print(f'\n|V1| = {V1.mod()}')
print(f'|V2| = {V2.mod()}')

# Normalization
V1_norm = V1.normalize()
print('\n--- V1 normalized ---')
V1_norm.show()
print(f'|V1_norm| = {V1_norm.mod()}')

# Dot product
d = V1.dot(V2)
print(f'\nV1 . V2 = {d}')

# Cross product
V_cross = V1.cross(V2)
print('\n--- V1 x V2 ---')
V_cross.show()

# Verify cross product is perpendicular to both V1 and V2
print(f'\n(V1 x V2) . V1 = {V_cross.dot(V1)}')
print(f'(V1 x V2) . V2 = {V_cross.dot(V2)}')

#-----------------------BOUNDARY CASES-------------------------------------

# Unit vectors
i = Vector3D(1.0, 0.0, 0.0)
j = Vector3D(0.0, 1.0, 0.0)
k = Vector3D(0.0, 0.0, 1.0)

print('\n--- Unit vector cross products ---')
i_cross_j = i.cross(j)
print('i x j = ', end='')
i_cross_j.show()

j_cross_k = j.cross(k)
print('j x k = ', end='')
j_cross_k.show()

k_cross_i = k.cross(i)
print('k x i = ', end='')
k_cross_i.show()

# Zero vector normalization - should raise ValueError
try:
    V_zero = Vector3D(0.0, 0.0, 0.0)
    V_zero.normalize()
    print('\nERROR: Zero vector normalize should have raised ValueError')
except ValueError as e:
    print(f'\nZero vector normalize correctly rejected: {e}')

# Bad type - should raise TypeError
try:
    V_bad = Vector3D("a", 2.0, 3.0)
    print('ERROR: Bad type should have raised TypeError')
except TypeError as e:
    print(f'Bad type correctly rejected: {e}')