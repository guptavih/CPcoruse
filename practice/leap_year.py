def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    else:
        return False
print(is_leap_year(2000))  # Expected output: True
print(is_leap_year(1900))  # Expected output: False
print(is_leap_year(2024))  # Expected output: True