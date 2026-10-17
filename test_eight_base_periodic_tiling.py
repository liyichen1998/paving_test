from collections import defaultdict

stone = [
    (-1,1,3),(-1,1,2),(-1,1,1),(-1,1,0),
    (0,1,3),(0,1,2),(-1,2,5),(-1,2,0)
]
q0,r0,_=stone[0]
stone=[(q-q0,r-r0,k) for q,r,k in stone]

def rot60_cell(c):
    q,r,k=c
    return (-r,q+r,(k+1)%6)

def rotate_shape(shape,n):
    s=list(shape)
    for _ in range(n%6):
        s=[rot60_cell(c) for c in s]
    return s

rots=[rotate_shape(stone,n) for n in range(6)]

def placements(W,H):
    out=[]; seen=set()
    for rid,s in enumerate(rots):
        for dq in range(W):
            for dr in range(H):
                p=tuple(sorted(((q+dq)%W,(r+dr)%H,k) for q,r,k in s))
                if len(set(p))<8 or p in seen:
                    continue
                seen.add(p)
                out.append((p,rid,dq,dr))
    return out

def solve(W,H):
    U={(q,r,k) for q in range(W) for r in range(H) for k in range(6)}
    if len(U)%8: return None

    P=placements(W,H)
    by=defaultdict(list)
    for i,(cells,*_) in enumerate(P):
        for c in cells: by[c].append(i)

    uncovered=set(U)
    used=[]

    def dfs():
        if not uncovered: return True

        best=None; opts=None
        for c in uncovered:
            o=[i for i in by[c] if all(x in uncovered for x in P[i][0])]
            if not o: return False
            if opts is None or len(o)<len(opts):
                best,opts=c,o
                if len(opts)==1: break

        for i in opts:
            cells=P[i][0]
            for x in cells: uncovered.remove(x)
            used.append(i)
            if dfs(): return True
            used.pop()
            for x in cells: uncovered.add(x)
        return False

    if dfs():
        return [P[i] for i in used]
    return None

for W in range(1,9):
    for H in range(1,9):
        if (6*W*H)%8: continue
        ans=solve(W,H)
        print(W,H,"FOUND" if ans else "not found")
        if ans:
            print(ans)
            raise SystemExit
