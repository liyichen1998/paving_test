import math
import numpy as np
import matplotlib.pyplot as plt

phi = (1 + math.sqrt(5)) / 2
ratio = (5 + math.sqrt(5)) / (5 - math.sqrt(5))   # = phi^2
t = ratio / (1 + ratio)                            # ~= 0.7236068

def signed_area(tri):
    (x1,y1),(x2,y2),(x3,y3) = tri
    return 0.5*((x2-x1)*(y3-y1)-(y2-y1)*(x3-x1))

def ccw(tri):
    tri = [np.asarray(p, dtype=float) for p in tri]
    if signed_area(tri) < 0:
        tri[1], tri[2] = tri[2], tri[1]
    return tri

def directed_point(P, Q, frac):
    return (1-frac)*P + frac*Q

def draw_chiral_one_layer(ax, tri, frac=t, lw_outer=0.75, lw_inner=0.5):
    A, B, C = ccw(tri)
    D = directed_point(B, C, frac)
    E = directed_point(C, A, frac)
    F = directed_point(A, B, frac)

    poly = np.vstack([A,B,C,A])
    ax.plot(poly[:,0], poly[:,1], linewidth=lw_outer)

    for P,Q in [(A,D),(B,E),(C,F)]:
        ax.plot([P[0],Q[0]], [P[1],Q[1]], linewidth=lw_inner)

def triangular_grid_triangles(cols, rows, side=1.0):
    h = math.sqrt(3)/2 * side
    tris = []
    for j in range(rows):
        xoff = 0.5*(j % 2)
        xoff2 = 0.5*((j+1) % 2)
        y, y2 = j*h, (j+1)*h

        row0 = [np.array([(i+xoff)*side, y]) for i in range(cols+1)]
        row1 = [np.array([(i+xoff2)*side, y2]) for i in range(cols+1)]

        if j % 2 == 0:
            for i in range(cols):
                tris.append([row0[i], row0[i+1], row1[i]])
                if i < cols-1:
                    tris.append([row0[i+1], row1[i+1], row1[i]])
        else:
            for i in range(cols):
                tris.append([row0[i], row0[i+1], row1[i+1]])
                if i < cols-1:
                    tris.append([row0[i], row1[i+1], row1[i]])
    return tris

fig, ax = plt.subplots(figsize=(14,9))
for tri in triangular_grid_triangles(12, 8, 1.0):
    draw_chiral_one_layer(ax, tri, frac=t)  # swap t -> 1-t to reverse chirality

ax.set_aspect("equal")
ax.axis("off")
plt.show()
