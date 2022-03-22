#! /usr/bin/env python3

import validations as vld

print(vld.validate_user("blue.kale", 3)) # True
print(vld.validate_user(".blue.kale", 3)) # Currently True, should be >print(validate_user("red_quinoa", 4)) # True
print(vld.validate_user("_red_quinoa", 4)) # Currently True, should be>
print(vld.validate_user("Russ Francis", 7)) #  True
print(vld.validate_user("9_hundred_miles",5)) # False

