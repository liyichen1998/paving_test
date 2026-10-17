"""Golden four-way triangle subdivision.

This is the approved simultaneous-dependency construction recovered from the
earlier research code: three cyclic cevians are drawn simultaneously; their
pairwise intersections define four child triangles.  For the golden parameter,
the children have equal area: three congruent scalene triangles plus one
equilateral triangle.
"""
import math
import numpy as np

PHI=(1+math.sqrt(5))/2
RATIO=(5+math.sqrt(5))/(5-math.sqrt(5))  # phi^2
T=RATIO/(1+RATIO)

def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def line_intersection(p,p2,q,q2):
    p=np.asarray(p,float); p2=np.asarray(p2,float)
    q=np.asarray(q,float); q2=np.asarray(q2,float)
    r=p2-p; s=q2-q
    return p + cross(q-p,s)/cross(r,s)*r

def polygon_area(poly):
    p=np.asarray(poly,float)
    x=p[:,0]; y=p[:,1]
    return abs(float(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1))))/2

def signed_area3(A,B,C):
    return cross(np.asarray(B)-A,np.asarray(C)-A)/2

def regular_triangle(side=1.0):
    return (np.array([0.,0.]),np.array([side,0.]),
            np.array([side/2,math.sqrt(3)*side/2]))

def split_triangle(A,B,C,hand=+1):
    """Return [S_AB, S_BC, S_CA, E] for hand +1 or -1.

    Input orientation is normalized CCW.  hand=-1 uses 1-T and is the
    reflected subdivision state.
    """
    A=np.asarray(A,float); B=np.asarray(B,float); C=np.asarray(C,float)
    if cross(B-A,C-A)<0: B,C=C,B
    frac=T if hand==1 else 1-T
    D=(1-frac)*B+frac*C
    E=(1-frac)*C+frac*A
    F=(1-frac)*A+frac*B
    X=line_intersection(A,D,B,E)
    Y=line_intersection(B,E,C,F)
    Z=line_intersection(C,F,A,D)
    return [
        np.array([A,B,X]),
        np.array([B,C,Y]),
        np.array([C,A,Z]),
        np.array([X,Y,Z]),
    ]

def side_lengths(tri):
    tri=np.asarray(tri,float)
    return sorted(float(np.linalg.norm(tri[(i+1)%3]-tri[i])) for i in range(3))
