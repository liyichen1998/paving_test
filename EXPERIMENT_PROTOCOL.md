# Experiment Protocol

## Before every search

1.  Run the full regression suite.
2.  Record the exact code revision and configuration.
3.  Confirm the simultaneous-cevian geometry.
4.  Confirm no fixed alternating +/- board has slipped into the model.
5.  Confirm candidate state is measured from final geometry, not buried
    labels.
6.  If any baseline regression fails, do not interpret downstream search
    output.

## Positive witness requirements

Save the candidate canonical ID, microscopic realization, serialized
polygon boundary, rigid transforms, adjacency/contact graph, reflection
policy, sliding/discreteness classification, numbered diagnostic
rendering, and a machine-checkable validation script.

## Negative search requirements

State the finite envelope: maximum microscopic size, substrate
radius/window, handed states, allowed motions, topology restrictions,
growth depth/radius, numerical tolerance, timeout and node limit.

"No witness found" never means "impossible."

## Symmetry discipline

Raw search-tree size is not branching complexity. Patches related by
allowed global rigid motion must be canonicalized before branching
counts are interpreted.

Reflection used to test achirality must remain distinct from reflection
allowed as a placement operation.

## Buried-state test

When multiple microscopic realizations give the same macroscopic
polygon, erase internal edges and compare legal external continuations.
If the realizations cannot be distinguished externally in the tested
neighborhood, do not count them as useful states.

## Sliding test

If a neighbor can move continuously while remaining legal, classify that
freedom as continuous/sliding. The present interest is finite/discrete
local choice.

## Regression-witness policy

Historical witnesses move into formal tests only after their geometry
and semantics are reconstructed and independently checked. The reported
`(1,3,14,15)` witness is not yet a regression test because its source
search file was not recovered.
