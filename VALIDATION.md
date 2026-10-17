# Validation Report

**Checkpoint:** Golden-4 Tiling Lab v0.2

## Regression suite

``` text
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/generated/interface/models.py", line 32317, in hydrate_crdt_from_proto
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/rpc/remote.py", line 749, in __call__
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
test_central_is_equilateral (test_geometry.Golden4GeometryTests.test_central_is_equilateral) ... ok
test_children_cover_parent_area (test_geometry.Golden4GeometryTests.test_children_cover_parent_area) ... ok
test_four_equal_areas (test_geometry.Golden4GeometryTests.test_four_equal_areas) ... ok
test_golden_parameter (test_geometry.Golden4GeometryTests.test_golden_parameter) ... ok
test_handedness_is_mirror_metric (test_geometry.Golden4GeometryTests.test_handedness_is_mirror_metric) ... ok
test_scalene_lengths (test_geometry.Golden4GeometryTests.test_scalene_lengths) ... ok
test_three_scalenes_congruent (test_geometry.Golden4GeometryTests.test_three_scalenes_congruent) ... ok
test_eight_base_periodic_witness_reproduces (test_legacy_periodic.LegacyPeriodicWitness.test_eight_base_periodic_witness_reproduces) ... ok

----------------------------------------------------------------------
Ran 8 tests in 5.198s

OK
```

Return code: `0`.

## Syntax compilation

`python -m compileall -q golden4 tests legacy`

Return code: `0`.

``` text
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/generated/interface/models.py", line 32317, in hydrate_crdt_from_proto
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/rpc/remote.py", line 749, in __call__
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
```

## Manual consistency audit

-   Clean geometry is isolated under `golden4/`.
-   Historical material is isolated under `legacy/`.
-   The fixed alternating-handed board is explicitly historical/rejected
    as a modeling assumption.
-   The unrecovered `golden_2plus4_local_search` result is explicitly
    unverified.
-   All docs use the current weaker target: construct at least one
    explicit nonperiodic tiling before asking for universal
    aperiodicity.
-   Buried internal spin multiplicity is explicitly excluded from useful
    programmability.
-   Future negative searches must state their finite envelope.
-   No aperiodicity theorem or monotile claim is asserted by this
    checkpoint.

## SHA-256 manifest

``` text
e6ff3ed86116fcccd98f4e541896a220aae7b6b68db8cfb465c358c24385f079  .gitignore
ef818bec07460982eb7218e45e1ba0a55fe776b4b89d38ca9e03980ec2f82287  README.md
244f3919112e1979d4241025132fbec7946677396dc56da3e2b8f2a95baf6b40  VALIDATION.txt
f9896cf9c499e3d38e15e1c1f92aa40604bd7a78d11eff7c8cfee05e77134931  docs/EXPERIMENT_PROTOCOL.md
18950a5dd787c6d879e63e268e6bbfb79d8e1320733b8a5ba0dfb8ea3f18afc5  docs/GEOMETRY_SPEC.md
54011852c16876e508d3235396aac8f119719c0c3a35077ee2761e153b2300cc  docs/LEGACY_AUDIT.md
ebaa955236e45ad3fc1480b7dbdd6fa4bc42dd67279dd9a5a7f9b4aef8596a7b  docs/RESEARCH_PLAN.md
06e73e10da297512a739dbe3bed9b0ad8978ec85789945e670e325dde23b42d8  golden4/__init__.py
2d42d6dc7a3c5b67ace20684f584a2de9b53fb449ac637649a3e282ce67da3bc  golden4/geometry.py
3f587080375de302ee90c6bfeddf8981b7a97b184fcafd5bff07d6dacd903075  legacy/dfs_single_shape_alternating_scaffold.py
4827753831460e7cba1b7170d0dd945316d937497e5ab9aaa2b6efee59de6f46  legacy/golden_4spin_preserve_flip_diagnostic.txt
bcdadf02a11755849f93b443b2cbccf9867db7504dee113701561134dd2c7988  legacy/golden_chiral_triangle_background.py
85651fea2f925b8c0376137cf199d0a324f3cf04eaccd1b4137eda42b31e90a1  legacy/golden_hex_base_definition.py
7d2b42d27dd66bbd1037b87cccf25cb984c68bfffc2953ebe9c541ffaed0d9eb  legacy/test_eight_base_periodic_tiling.py
732685927588f0e82d943a7b3ba90edafd2de37ad09549359d8312d3d4c01d9d  pyproject.toml
b7d54cd14fce267460e325953f629dcad8d5e98bf5513971279ebca4b8823198  requirements.txt
57c9d9eab29615e3200e7d6fd9aaee4f153bc7e5f37b82c4897e0aa84222e361  tests/test_geometry.py
acb266db19710f88d5de574633ced065bef36f5da4ad2608af8e5a93a3d9f3cf  tests/test_legacy_periodic.py
```
