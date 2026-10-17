# Geometry Specification

This file defines the geometry future code must reproduce.

## Parent and parameter

Use an equilateral triangle (ABC), normalized counterclockwise. For unit
side:

\[ A=(0,0),`\quad `{=tex}B=(1,0),`\quad`{=tex}
C=`\left`{=tex}(`\frac12`{=tex},`\frac{\sqrt3}{2}`{=tex}`\right`{=tex}).
\]

The golden directed fraction is

\[ t=`\frac{5+\sqrt5}{10}`{=tex}`\approx0.7236067977499789`{=tex}. \]

The opposite handed state uses (1-t).

## Simultaneous-cevian definition

For the (+) state:

\[ D=(1-t)B+tC,`\quad`{=tex} E=(1-t)C+tA,`\quad`{=tex} F=(1-t)A+tB. \]

Let

\[
X=AD`\cap `{=tex}BE,`\quad `{=tex}Y=BE`\cap `{=tex}CF,`\quad `{=tex}Z=CF`\cap `{=tex}AD.
\]

The children are exactly

\[ S\_{AB}=(A,B,X),`\quad`{=tex} S\_{BC}=(B,C,Y),`\quad`{=tex}
S\_{CA}=(C,A,Z),`\quad`{=tex} E=(X,Y,Z). \]

This is a **simultaneous intersection definition**. Do not implement it
as sequential cuts whose later lines are truncated by earlier-created
cells.

## Required invariants

For parent area (A_0),

\[ A(S\_{AB})=A(S\_{BC})=A(S\_{CA})=A(E)=A_0/4. \]

The three (S) children are congruent. For unit parent side:

\[
`\left`{=tex}{`\frac{\sqrt5-1}{4}`{=tex},`\frac{1+\sqrt5}{4}`{=tex},1`\right`{=tex}}
`\approx`{=tex}{0.3090169944,0.8090169944,1}. \]

The central child is equilateral with side (1/2). The (-) state is
mirror-related and has identical metric child data.

## Final-boundary rule

A macroscopic candidate is the polygon union of microscopic children.
Internal edges are erased. State/dependency claims must be made from the
resulting boundary and legal neighboring placements, not labels that
disappear inside the union.

## Numerical policy

The checkpoint kernel uses floating point and is sufficient for its
current regression tests. Exhaustive geometry should eventually use
algebraic coordinates in
(`\mathbb `{=tex}Q(`\sqrt3`{=tex},`\sqrt5`{=tex})), exact combinatorial
scaffold coordinates plus verified predicates, or a carefully tested
robust tolerance policy.

Congruence, chirality, contact, overlap, and gap detection are
research-critical and need dedicated tests.
