#!/usr/bin/env python3
def fractional_part(num,den):
 if den==0:
  frac=0
 elif (num%den)==0:
  frac=0
 else:
  x=(num%den)
  frac=(x/den)
 return frac
print(fractional_part(5, 4))
print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
