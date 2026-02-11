"""
Simplified version of abc_implementation.py

ORIGINAL (Advanced): Custom metaclass 'interface' that manually tracks
abstract methods, liabilities, and prevents instantiation.

SIMPLIFIED: Uses Python's built-in abc module which does all of this
automatically with much less code.
"""

from abc import ABC, abstractmethod


# --- Base class B1 with abstract methods f1 and f2 ---
class B1(ABC):
    @abstractmethod
    def f1(self):
        pass

    @abstractmethod
    def f2(self):
        pass


# --- Base class B2 with abstract methods f3 and f4 ---
class B2(ABC):
    @abstractmethod
    def f3(self):
        pass

    @abstractmethod
    def f4(self):
        pass


# --- D implements only f1 and f2 (still abstract because f3, f4 missing) ---
class D(B1, B2):
    def f1(self):
        pass

    def f2(self):
        pass


# --- D1 implements all four methods (fully concrete, can be instantiated) ---
class D1(B1, B2):
    def f1(self):
        pass

    def f2(self):
        pass

    def f3(self):
        pass

    def f4(self):
        pass


# --- Testing ---
# Try to create B1 (abstract - should fail)
try:
    b1 = B1()
except TypeError as e:
    print(f"Cannot create B1: {e}")

# Try to create B2 (abstract - should fail)
try:
    b2 = B2()
except TypeError as e:
    print(f"Cannot create B2: {e}")

# Try to create D (still abstract - f3, f4 not implemented)
try:
    d = D()
except TypeError as e:
    print(f"Cannot create D: {e}")

# Create D1 (concrete - all methods implemented)
try:
    d1 = D1()
    print(f"D1 created successfully! type(d1): {type(d1)}")
except TypeError as e:
    print(f"Cannot create D1: {e}")
