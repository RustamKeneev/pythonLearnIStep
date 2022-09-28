import first
print("Top level in second.py")
first.function_one()

if __name__ == '__main__':
    print("second.py is being run directly")
else:
    print("second.py has been imported")

"""
__name__  позволяет вам выяснить  был ли запущен модуль с непосредственно или он был бы импортирован
"""

