import math
from collections import defaultdict
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.ops import unary_union
from shapely import affinity

phi=(1+math.sqrt(5))/2
ratio=(5+math.sqrt(5))/(5-math.sqrt(5))
t=ratio/(1+ratio)

def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def inter(p,p2,q,q2):
    p=np.asarray(p,float); p2=np.asarray(p2,float); q=np.asarray(q,float); q2=np.asarray(q2,float)
    r=p2-p; s=q2-q
    return p+cross(q-p,s)/cross(r,s)*r

def children(A,B,C,frac):
    A=np.asarray(A,float); B=np.asarray(B,float); C=np.asarray(C,float)
    if cross(B-A,C-A)<0: B,C=C,B
    D=(1-frac)*B+frac*C; E=(1-frac)*C+frac*A; F=(1-frac)*A+frac*B
    X=inter(A,D,B,E); Y=inter(B,E,C,F); Z=inter(C,F,A,D)
    return [Polygon([A,B,X]),Polygon([B,C,Y]),Polygon([C,A,Z]),Polygon([X,Y,Z])]

# one alternating-handed hexagon, IDs 1..24
O=np.array([0.,0.])
V=[np.array([math.cos(math.radians(60*k)),math.sin(math.radians(60*k))]) for k in range(6)]
local={}; gid=1
for k in range(6):
    frac=t if k%2==0 else 1-t
    for p in children(O,V[k],V[(k+1)%6],frac):
        local[gid]=p; gid+=1

seed_ids=[11,13,15,16]
seed=unary_union([local[i] for i in seed_ids])

# build periodic hex scaffold
E1=np.array([1.5,math.sqrt(3)/2]); E2=np.array([0.,math.sqrt(3)])
R=4
cells=[]
for q in range(-R,R+1):
    for r in range(-R,R+1):
        sh=q*E1+r*E2
        for lid,p in local.items():
            g=affinity.translate(p,xoff=sh[0],yoff=sh[1])
            cells.append({'key':(q,r,lid),'poly':g,'cent':(g.centroid.x,g.centroid.y)})

# robust mapping by rounded geometry signature

def sig(poly):
    coords=[]
    for x,y in poly.exterior.coords[:-1]: coords.append((round(x,8),round(y,8)))
    return tuple(sorted(coords))
cell_by_sig={sig(c['poly']):i for i,c in enumerate(cells)}

# create all congruent copies from local dihedral placements and scaffold translations
placements=[]; seen=set()
for refl in [False,True]:
    s=seed if not refl else affinity.scale(seed,xfact=-1,yfact=1,origin=(0,0))
    for deg in range(0,360,60):
        sr=affinity.rotate(s,deg,origin=(0,0))
        # derive its 4 component atoms using same transform on seed atoms
        atoms=[]
        for lid in seed_ids:
            a=local[lid]
            if refl: a=affinity.scale(a,xfact=-1,yfact=1,origin=(0,0))
            a=affinity.rotate(a,deg,origin=(0,0))
            atoms.append(a)
        for q in range(-R,R+1):
            for r in range(-R,R+1):
                sh=q*E1+r*E2
                ids=[]; ok=True
                for a in atoms:
                    g=affinity.translate(a,xoff=sh[0],yoff=sh[1])
                    ci=cell_by_sig.get(sig(g))
                    if ci is None: ok=False; break
                    ids.append(ci)
                if ok and len(set(ids))==4:
                    key=tuple(sorted(ids))
                    if key not in seen:
                        seen.add(key)
                        placements.append({'cells':key,'refl':refl,'deg':deg})

by_cell=defaultdict(list)
for pi,p in enumerate(placements):
    for ci in p['cells']: by_cell[ci].append(pi)

# central seed
seed_cells=tuple(sorted(i for i,c in enumerate(cells) if c['key'][0]==0 and c['key'][1]==0 and c['key'][2] in seed_ids))
seed_pi=next(i for i,p in enumerate(placements) if p['cells']==seed_cells)

# finite target region, hex radius 2
def hdist(q,r): return max(abs(q),abs(r),abs(q+r))
target={i for i,c in enumerate(cells) if hdist(c['key'][0],c['key'][1])<=2}
occupied=set(placements[seed_pi]['cells']); chosen=[seed_pi]
NODES=0; LIMIT=200000

def solve():
    global NODES
    NODES+=1
    if NODES>LIMIT: return False
    uncovered=[c for c in target if c not in occupied]
    if not uncovered: return True
    best=None; opts_best=None
    for c in uncovered:
        opts=[]
        for pi in by_cell[c]:
            if all(x not in occupied for x in placements[pi]['cells']): opts.append(pi)
        if not opts: return False
        if opts_best is None or len(opts)<len(opts_best):
            best=c; opts_best=opts
            if len(opts)==1: break
    opts_best.sort(key=lambda pi:-sum((x in target and x not in occupied) for x in placements[pi]['cells']))
    for pi in opts_best:
        pc=placements[pi]['cells']
        occupied.update(pc); chosen.append(pi)
        if solve(): return True
        chosen.pop()
        for x in pc: occupied.remove(x)
    return False

success=solve()

# render
fig,ax=plt.subplots(figsize=(12,11))
for i,c in enumerate(cells):
    q,r,_=c['key']
    if hdist(q,r)<=3:
        x,y=c['poly'].exterior.xy
        ax.plot(x,y,color='0.8',lw=.3)

for n,pi in enumerate(chosen,1):
    g=unary_union([cells[i]['poly'] for i in placements[pi]['cells']])
    if g.geom_type=='Polygon':
        x,y=g.exterior.xy
        ax.fill(x,y,alpha=.35)
        ax.plot(x,y,color='black',lw=1.2)
        cc=g.centroid
        ax.text(cc.x,cc.y,str(n),ha='center',va='center',fontsize=7)

ax.set_aspect('equal'); ax.axis('off')
ax.set_title(f"Seed 11+13+15+16 | DFS cover success={success} | copies={len(chosen)} | nodes={NODES}")
out='/mnt/data/dfs_11_13_15_16_result.png'
fig.savefig(out,dpi=240,bbox_inches='tight',pad_inches=.04)
plt.close(fig)

Path('/mnt/data/dfs_11_13_15_16_report.txt').write_text(
    f"success={success}\nplacements={len(placements)}\ncopies={len(chosen)}\nnodes={NODES}\n"
)
print(success, len(placements), len(chosen), NODES)
