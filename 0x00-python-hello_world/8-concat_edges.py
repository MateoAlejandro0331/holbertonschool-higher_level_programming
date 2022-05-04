#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:39+16] + str[55:55+12] + str[107:107+5] + str[:6]
print(str)
