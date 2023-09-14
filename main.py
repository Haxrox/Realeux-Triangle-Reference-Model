import matplotlib.pyplot as plt
import math
from decimal import *

screen = [[0 for y in range(120)] for x in range(160)]

def setPixel(x, y, comp):
  if (x >= 0 and x < 160 and y >= 0 and y < 120 and comp(x, y)):
    screen[x][y] = 1
    plt.axis([0, 160, 0, 120]) 
    plt.plot(x, y, 'ro')
    # print(f'screen[{x}][{y}] = 1')

def drawCircle(centre_x, centre_y, radius, comp):
    print(f'drawCircle({centre_x}, {centre_y}, {radius})')
    offset_y = 0
    offset_x = radius
    crit = 1 - radius
    while offset_y <= offset_x:
        setPixel(centre_x + offset_x, centre_y + offset_y, comp) #  -- octant 1
        setPixel(centre_x + offset_y, centre_y + offset_x, comp)  # -- octant 2
        setPixel(centre_x - offset_x, centre_y + offset_y, comp)   #-- octant 4
        setPixel(centre_x - offset_y, centre_y + offset_x, comp)   #-- octant 3
        setPixel(centre_x - offset_x, centre_y - offset_y, comp)   #-- octant 5
        setPixel(centre_x - offset_y, centre_y - offset_x, comp)   #-- octant 6
        setPixel(centre_x + offset_x, centre_y - offset_y, comp)   #-- octant 8
        setPixel(centre_x + offset_y, centre_y - offset_x, comp)   #-- octant 7
        offset_y = offset_y + 1
        if crit <= 0:
            crit = crit + 2 * offset_y + 1
        else:
            offset_x = offset_x - 1
            crit = crit + 2 * (offset_y - offset_x) + 1

        # print(offset_x, offset_y, crit)

def reuleaux(centre_x, centre_y, diameter):
  print(f'reuleaux({centre_x}, {centre_y}, {diameter})')
  c_x = centre_x
  c_y = centre_y
  c_x1 = c_x + diameter/2
  c_y1 = c_y + diameter * math.sqrt(3)/6 # 0.28515625
  c_x2 = c_x - diameter/2
  c_y2 = c_y + diameter * math.sqrt(3)/6 # 0.28515625
  c_x3 = c_x
  c_y3 = c_y - diameter * math.sqrt(3)/6 # 0.57421875

  # Round for precision
  c_x1 = round(c_x1)
  c_x2 = round(c_x2)
  c_x3 = round(c_x3)

  c_y1 = round(c_y1)
  c_y2 = round(c_y2)
  c_y3 = round(c_y3)
  
  print(f'[REULEAUX] Circle 1 - ({c_x1}, {c_y1})')
  drawCircle(c_x1, c_y1, diameter, lambda x, y : (x <= c_x3 and x >= c_x2 and y >= c_y3 and y <= c_y2))
  print(f'[REULEAUX] Circle 2 - ({c_x2}, {c_y2})')
  drawCircle(c_x2, c_y2, diameter, lambda x, y : (x >= c_x3 and x <= c_x1 and y <= c_y1 and y >= c_y3))
  print(f'[REULEAUX] Circle 3 - ({c_x3}, {c_y3})')
  drawCircle(c_x3, c_y3, diameter, lambda x, y : (x <= c_x1 and x >= c_x2 and y >= c_y1 and y >= c_y2))
  
  
# drawCircle(80, 60, 40)
reuleaux(80, 60, 80)
# reuleaux(80, 60, 40)
plt.show()
