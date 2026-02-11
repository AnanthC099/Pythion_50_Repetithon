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