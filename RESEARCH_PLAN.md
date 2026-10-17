# Research Plan

## Objective

Determine whether the Golden-4 subdivision supports nontrivial geometric
programmability and, if so, whether that can construct an explicit
nonperiodic tiling by one macroscopic shape.

The present target is existence of a nonperiodic tiling, not universal
aperiodicity.

## Phase 0 --- checkpoint integrity

Recover historical code, isolate approved geometry, establish regression
tests, and record rejected assumptions.

**Exit:** baseline tests pass from a clean checkout.

## Phase 1 --- robust geometry kernel

Implement robust polygon union, canonicalization under
translation/rotation, reflection comparison, chirality, overlap/gap
detection, and legal-contact predicates.

**Exit:** rigid-motion invariance and deliberately invalid contacts are
covered by tests.

## Phase 2 --- free-spin substrate

Generate finite neighborhoods without preassigning a periodic +/-
coloring. Each parent may have

\[ `\sigma`{=tex}\_i`\in`{=tex}{+,-}. \]

Explicitly test whether neighboring subdivisions form a conforming
microscopic cell complex; do not assume arbitrary spin assignments do.

**Exit:** valid local spin neighborhoods can be enumerated and rendered.

## Phase 3 --- macroscopic candidates

Enumerate connected microscopic unions. Compute the actual final
polygon, canonicalize it, record multiple realizations of the same
shape, classify chirality, and reject buried-state pseudo-freedom.

**Exit:** deterministic candidate database with canonical IDs.

## Phase 4 --- placement engine

Enumerate legal congruent placements around a seed. Distinguish isolated
discrete contacts from continuous sliding families.

**Exit:** complete local placement catalog for small candidates.

## Phase 5 --- dependency search

Measure inequivalent one-, two-, and three-neighbor states, e.g.

\[ B_1(T),`\quad `{=tex}B_2(T),`\quad `{=tex}B_3(T), \]

and count cases where pairwise ambiguity is resolved by a third/fourth
neighbor.

**Exit:** independently reproduce at least one genuine boundary-visible
ambiguity witness. The historical `(1,3,14,15)` result is a target, not
ground truth.

## Phase 6 --- center-out patch growth

Grow inequivalent legal patches to increasing radius, quotienting global
rigid symmetries. Track surviving classes, branching, dead branches,
finite orientation cycles, translation vectors, and contextual states.

**Exit:** persistent discrete branching survives enough layers to
justify symbolic analysis.

## Phase 7 --- periodicity adversary

Search toroidal domains, small translation vectors, small fundamental
domains, and repeated orientation/state cycles.

Periodic witnesses are recorded rather than automatically rejected under
the current objective.

## Phase 8 --- nonperiodic encoding

Only after genuine geometric states exist, test whether they can
implement a known nonperiodic substitution or symbolic process without
adding labels by hand.

A successful result needs one macroscopic prototile, an explicit
algorithm producing arbitrarily large legal patches/a plane tiling, and
a proof or certificate that the generated tiling is nonperiodic.

## Phase 9 --- optional stronger problem

Only later revisit whether **every** legal tiling by the shape must be
nonperiodic. That is a substantially harder monotile question.
