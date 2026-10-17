# Golden-4 Tiling Lab

**Status:** research checkpoint / computational laboratory\
**Version:** 0.2\
**Scope:** golden four-way subdivision of an equilateral triangle and
computational searches built on top of it.

This repository is intended to be the **source of truth** for the
project. It preserves recovered historical code, locks the geometry
already checked, records rejected approaches, and defines a reproducible
route for future searches. It does **not** claim an aperiodic monotile
has been found.

## Core construction

For an equilateral parent triangle (ABC), define

\[ `\varphi`{=tex}=`\frac{1+\sqrt5}{2}`{=tex},`\qquad`{=tex}
t=`\frac{5+\sqrt5}{10}`{=tex}`\approx0.7236067977499789`{=tex}. \]

Choose (D`\in `{=tex}BC,E`\in `{=tex}CA,F`\in `{=tex}AB) at directed
fraction (t). Draw the three cevians **simultaneously**:

\[ AD,`\qquad `{=tex}BE,`\qquad `{=tex}CF. \]

With

\[
X=AD`\cap `{=tex}BE,`\quad `{=tex}Y=BE`\cap `{=tex}CF,`\quad `{=tex}Z=CF`\cap `{=tex}AD,
\]

the four children are

\[
(A,B,X),`\quad`{=tex}(B,C,Y),`\quad`{=tex}(C,A,Z),`\quad`{=tex}(X,Y,Z).
\]

At the golden value, all four have equal area. The first three are
congruent scalene triangles and the center is equilateral:

\[ `\boxed{\Delta\to3S+E}`{=tex}. \]

For a unit parent, the scalene side lengths are

\[
`\frac{\sqrt5-1}{4}`{=tex},`\quad`{=tex}`\frac{1+\sqrt5}{4}`{=tex},`\quad1`{=tex},
\]

and the central equilateral side is (1/2). The reflected handed state is
obtained with (1-t).

## Current research question

Can finite unions of Golden-4 microscopic triangles produce a single
macroscopic shape with **genuine discrete, boundary-visible contextual
freedom** that survives patch growth?

The target is not hidden +/- labels. If two microscopic states become
indistinguishable after internal edges are erased and cannot change any
legal external continuation, they do not count as useful
programmability.

The most interesting local signature is

\[
`\boxed{\text{pairwise ambiguity}+\text{third-neighbor resolution}}`{=tex}.
\]

A pair may allow several legal continuations, while a third or fourth
neighbor removes some choices. This is a static geometric CSP-style
dependency.

The current relaxed goal is

\[
`\exists`{=tex}`\mathcal `{=tex}T`\in`{=tex}`\mathrm{Tilings}`{=tex}(T)`\text{ nonperiodic}`{=tex},
\]

not yet

\[
`\forall`{=tex}`\mathcal `{=tex}T`\in`{=tex}`\mathrm{Tilings}`{=tex}(T), `\mathcal `{=tex}T`\text{ nonperiodic}`{=tex}.
\]

So a periodic witness is important metadata, but no longer automatically
kills a candidate.

## Modeling decisions

1.  The triangular lattice is a geometric scaffold/ruler, not a
    precolored state machine.
2.  Parent triangles may carry locally chosen handedness (+) or (-).
3.  **Do not preassign a periodic alternating +/- board.**
4.  Candidate tiles are actual polygon unions of microscopic children.
5.  Internal subdivision edges disappear from the final candidate
    boundary.
6.  Buried spin multiplicity is not programmability.
7.  Search grows patches center-out; placement order is not intrinsic
    time.
8.  Symmetry-equivalent patches must be quotiented before branching is
    interpreted.
9.  A known regression failure invalidates downstream search output
    until fixed.
10. Negative finite search results are not impossibility theorems.

## Repository layout

``` text
golden4_research_package/
├── README.md
├── VALIDATION.md
├── pyproject.toml
├── requirements.txt
├── golden4/
│   ├── __init__.py
│   └── geometry.py
├── tests/
│   ├── test_geometry.py
│   └── test_legacy_periodic.py
├── docs/
│   ├── GEOMETRY_SPEC.md
│   ├── RESEARCH_PLAN.md
│   ├── EXPERIMENT_PROTOCOL.md
│   └── LEGACY_AUDIT.md
└── legacy/
    ├── golden_chiral_triangle_background.py
    ├── dfs_single_shape_alternating_scaffold.py
    ├── golden_hex_base_definition.py
    ├── test_eight_base_periodic_tiling.py
    └── golden_4spin_preserve_flip_diagnostic.txt
```

`golden4/` is clean code. `legacy/` is provenance and includes
approaches later rejected.

## Verified checkpoint

The regression suite checks the golden parameter, four equal areas,
three congruent scalene children, the central equilateral child,
expected side lengths, total area, mirrored +/- metric equivalence, and
reproduction of the historical old eight-base `2 x 2 FOUND` periodic
witness.

Run:

``` bash
python -m unittest discover -s tests -v
```

See `VALIDATION.md`.

## Historical status

The fixed alternating-handed scaffold was useful for developing search
machinery, but it is not an accepted model because it hard-codes a
periodic spin pattern.

A coarse earlier search also produced a false positive: apparent state
multiplicity came entirely from buried parent spins. Future searches
must operate on the actual final polygon boundary.

A later experiment reportedly found a local ambiguity witness involving
microscopic IDs `(1,3,14,15)`. Its original `golden_2plus4_local_search`
source was **not recovered** in the accessible files used for this
checkpoint. Treat it as a lead to reproduce, not a verified result.

## Next serious milestone

Build a robust pipeline

\[
`\text{geometry}`{=tex}`\to`{=tex}`\text{canonical polygon}`{=tex}`\to`{=tex}`\text{candidate unions}`{=tex}
`\to`{=tex}`\text{placements}`{=tex}`\to`{=tex}`\text{patch growth}`{=tex}`\to`{=tex}`\text{dependency statistics}`{=tex}.
\]

The first important success is not "find aperiodicity." It is to
independently rediscover a genuine boundary-visible local ambiguity
witness from the approved geometry.

Every future computational claim should have committed code, explicit
configuration, seed information when relevant, a machine-readable
witness, a diagnostic rendering, and a statement of the finite search
envelope.
