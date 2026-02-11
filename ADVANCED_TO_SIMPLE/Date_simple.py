"""
Simplified version of SESSION-030/Date.py

ORIGINAL: Uses type(x) != int 6 times (constructor + 3 setters),
verbose separate getter/setter methods.
SIMPLIFIED: Uses isinstance(), helper for validation, __repr__.
"""


class Date:
    def __init__(self, day: int, month: int, year: int):
        self._validate_int(day, "day")
        self._validate_int(month, "month")
        self._validate_int(year, "year")
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def _validate_int(value, name):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be int, got {type(value).__name__}")

    def get_day(self) -> int:
        return self.day

    def get_month(self) -> int:
        return self.month

    def get_year(self) -> int:
        return self.year

    def set_day(self, new_day: int) -> None:
        self._validate_int(new_day, "day")
        self.day = new_day

    def set_month(self, new_month: int) -> None:
        self._validate_int(new_month, "month")
        self.month = new_month

    def set_year(self, new_year: int) -> None:
        self._validate_int(new_year, "year")
        self.year = new_year

    def __repr__(self):
        return f"{self.day}/{self.month}/{self.year}"


if __name__ == "__main__":
    D = Date(1, 10, 2025)
    print(D)
    D.set_day(5)
    print(D)
    D.set_month(11)
    print(D)
    D.set_year(2026)
    print(D)
