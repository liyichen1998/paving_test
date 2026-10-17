# Legacy Audit

This file separates recovered executable evidence from
remembered/reported results.

## Recovered files

### `golden_chiral_triangle_background.py`

Early visualization of the golden directed split on a triangular grid.
It draws the cevians but is not itself the clean child-polygon API.

### `dfs_single_shape_alternating_scaffold.py`

Contains the recovered simultaneous-intersection `children(...)`
implementation:

\[
X=AD`\cap `{=tex}BE,`\quad `{=tex}Y=BE`\cap `{=tex}CF,`\quad `{=tex}Z=CF`\cap `{=tex}AD.
\]

This is the main recovered source used to lock the clean geometry
kernel.

The same script also explores a fixed alternating-handed scaffold. That
scaffold is historical only; its preassigned periodic spin field was
later rejected as a modeling assumption.

### `golden_hex_base_definition.py`

Compact record of the same-handed hex-base construction

\[ B_k={k:L,k:O,k:C}`\cup`{=tex}{(k-1):R}. \]

Preserved as provenance; not yet migrated into the clean API.

### `test_eight_base_periodic_tiling.py`

Historical discrete toroidal exact-cover search. The current test suite
executes it and confirms the old `2 2 FOUND` witness.

### `golden_4spin_preserve_flip_diagnostic.txt`

Diagnostic output from the preserve/flip abstraction. It documents an
explored abstraction, not proof that those states survive as final
geometric boundary states.

## Historical result not recovered as executable source

The earlier `golden_2plus4_local_search` reportedly found a small local
ambiguity witness, with remembered microscopic IDs `(1,3,14,15)`. Its
source was not found among the accessible recovered files used for this
package.

Therefore it is **unverified in this checkpoint** and must be
independently reproduced.

## Known false positive

A coarse search over whole parent-triangle carriers once found apparent
state multiplicity. The differing spins were completely buried inside
the composite. This was bookkeeping entropy, not boundary-visible
programmability.

This failure motivates the final-boundary rule.

## Provenance policy

Treat `legacy/` as read-only historical material. New implementations
belong under `golden4/`. Verified historical behavior should be wrapped
by tests rather than silently rewriting legacy files.
