### Bresenham Circle Algorithm Pseudo Code
```
drawCircle(centre_x, centre_y, radius):
    offset_y = 0
    offset_x = radius
    crit = 1 - radius
    while offset_y ≤ offset_x:
        setPixel(centre_x + offset_x, centre_y + offset_y)   -- octant 1
        setPixel(centre_x + offset_y, centre_y + offset_x)   -- octant 2
        setPixel(centre_x - offset_x, centre_y + offset_y)   -- octant 4
        setPixel(centre_x - offset_y, centre_y + offset_x)   -- octant 3
        setPixel(centre_x - offset_x, centre_y - offset_y)   -- octant 5
        setPixel(centre_x - offset_y, centre_y - offset_x)   -- octant 6
        setPixel(centre_x + offset_x, centre_y - offset_y)   -- octant 8
        setPixel(centre_x + offset_y, centre_y - offset_x)   -- octant 7
        offset_y = offset_y + 1
        if crit ≤ 0:
            crit = crit + 2 * offset_y + 1
        else:
            offset_x = offset_x - 1
            crit = crit + 2 * (offset_y - offset_x) + 1
```

### Reuleux Overlaps
```
c_x = centre_x;
c_y = centre_y;
c_x1 = c_x + diameter/2;
c_y1 = c_y + diameter * $sqrt(3)/6;
c_x2 = c_x - diameter/2;
c_y2 = c_y + diameter * $sqrt(3)/6;
c_x3 = c_x;
c_y3 = c_y - diameter * $sqrt(3)/3;
```

`centre_x`: x-coordinate of the triangle

`centre_y`: y-coordinate of the triangle

`(c_x1, c_y1)`: bottom-right intersection coordiante
`(c_x2, c_y2)`: bottom-left intersection coordinate
`(c_x3, c_y3)`: top intersection coordinate

`diameter`: side length of the inscribed triangle, which is equivalent to the radius of the three circles

