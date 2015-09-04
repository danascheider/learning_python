import random

w, x, y, z = random.randint(0,1000), random.randint(0,1000), random.randint(0,1000), random.randint(0,1000)

if x < w:
  orig_x, orig_w = x, w
  x, w = orig_w, orig_x

if y < w:
  orig_y, orig_w = y, w
  y, w = orig_w, orig_y

if z < w: 
  orig_z, orig_w = z, w 
  z, w = orig_w, orig_z

if y < x:
  orig_y, orig_x = y, x
  y, x = orig_x, orig_y

if z < x:
  orig_z, orig_x = z, x
  z, x = orig_x, orig_z

if z < y:
  orig_z, orig_y = z, y
  y, z = orig_z, orig_y

print w, x, y, z