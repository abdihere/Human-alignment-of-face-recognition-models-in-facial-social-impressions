# Contingencies, existing data and deviations

The study uses existing data only, so what was seen before registration matters as much as what was planned. This page states what happens if something goes wrong during the analysis, everything computed or seen before registration, how the plan changed along the way, and the known limits of the design. The guiding rule is that, apart from the development checks on one model described below, **no trait prediction, leakage value or other outcome for the 16 models has been computed before registration.**

## If something goes wrong

These rules are fixed in advance so that no analytic choice is made after seeing an outcome.

**Before the real run.**

- If a built-in test fails on real data (*Sensitivity and validation*), the run stops. The code is fixed, the synthetic run is repeated, the fix is recorded as a deviation, and the real run starts again from the beginning. No outcome is read from the failed run.
- If a model's embedding file fails its checksum or shape check, that model is left out of every analysis and the report says so. H1 is run if at least 12 models in at least 9 families remain; otherwise it is reported descriptively.
- If the transformation code had failed its validation, the main H1b test would still have run with the released matrices for the 14 core models, and the analyses that need retraining would have been reported as not tested. (The validation passed.)

**During the run.**

| Situation | Rule |
|---|---|
| A chosen ridge penalty lies at the edge of the grid | kept; the share of edge penalties is reported per model |
| A trait's out-of-fold accuracy ρᵢ is zero or negative | kept in L(m); the trait and model are flagged |
| The five repeated partitions give different L(m) | their mean is used; the standard deviation over repeats is reported |
| The wild bootstrap p-value falls between 0.020 and 0.030 | the test is rerun with 99,999 draws, and that p-value decides |
| The transformation does not raise alignment on unseen trials for some models | those models stay in H1b and their number is reported; if this happens for most models, H1b is reported as not tested |
| A race × gender cell has fewer than 50 faces (Q3) or a CFD cell fewer than 20 | described only, not pooled |

**Reporting.** All 16 models appear in every table, whatever their results. H1 is reported with all three conditions, even if the first fails. Exploratory results are labelled as such and are not used to reinterpret H1. Any analysis not described in this registration is labelled *unregistered*.

## What was seen before registration

| What | Where | Relation to the outcomes |
|---|---|---|
| Human ratings: trait scores, reliabilities, trait correlations and structure, demographics, memorability | notebook 01 | human data only; they define the outcome's baseline |
| Similarity trials and Hojjati et al.'s released splits | notebook 01 | input to alignment and to the transformation |
| Alignment and recognition accuracy of all models, and the copy check | notebooks 01 and 02 | predictors; they decided the model set |
| Power simulations with the real predictors | notebook 02b | predictors only |
| Alignment of Dlib and SFace under the released and retrained transformations | notebook 03 | similarity data only |
| Synthetic runs of the full analysis | notebook 03 | simulated embeddings and ratings |

**Development checks on one model.** While the estimator and the pipeline were being developed (October–November 2026), they were run on one model, Dlib, as code checks: excess leakage L(m) = +0.0420 uncorrected and −0.0684 corrected, per-trait out-of-fold accuracies, and a one-fold transformation pilot (alignment on held-out trials 0.404 retrained, 0.418 with the released matrix, 0.358 raw). An earlier, faulty estimator gave Dlib an L(m) of 0.37; that number is void. These values came from code that has since been rewritten and are not used. No other model's trait predictions or leakage values were computed. Seeing one model's value gives little information about a relation across 16 models, but it is disclosed so that readers can judge for themselves.

## How the model set was decided

The two non-recognition models in the release (an active appearance model and StyleGAN2) are excluded (*Models*). Four openly available networks were extracted as candidates for extension. Two passed the copy check and were added. Two failed it because they share weights with models already in the set:

| Candidate | Shares weights with | Median row-wise cosine |
|---|---|---|
| ResNet-100 trained on Glint360K (InsightFace `antelopev2`) | ArcFace-100 | 0.894 |
| Inception-ResNet-v1 trained on VGGFace2 | FaceNet512 | 0.877 |

Their alignment and recognition accuracy were computed and seen before the decision, but the decision used only the copy-check statistics. Earlier candidate lists also included other networks, some of which were extracted for pipeline tests; no outcome was computed for any of them.

## Deviations from earlier plans

| Date | Change | Reason |
|---|---|---|
| Oct 2026 | Recognition accuracy measured as d′ instead of AUC | AUC is at or near 1.0 for five models |
| Oct 2026 | Excess leakage corrected for trait accuracy and rating reliability | without these terms, weaker models look less leaky and noisy ratings bias the baseline |
| 20 Nov 2026 | First condition of H1 changed from a family-bootstrap interval to a wild cluster bootstrap-t test | the interval was too conservative to detect plausible effects |
| 23 Nov 2026 | Shared-weights rule added to the copy check | RSA alone could not flag a model compared with its own re-extraction |
| 23 Nov 2026 | Model set fixed at 16 models in 12 families | copy check, and a power gain of about 8 points |
| 24 Nov 2026 | Hojjati et al.'s Zenodo version 2 used instead of version 1 | version 2 adds the transformation code, trained matrices and training triplets; every file used before is byte-identical |
| 24 Nov 2026 | H1b uses the released matrices for the 14 core models instead of retraining them | they were trained on triplets with no hold-out face; retraining is used only where no released matrix exists |

## Known limits

- **One observation per model.** With 16 models in 12 families, H1 has limited power (*Sensitivity and validation*), and model-level properties correlated with alignment cannot be ruled out. H1 is therefore not interpreted causally.
- **Extension preprocessing.** The two extension models were extracted with their own preprocessing, not the deepface pipeline used for the core models. For 25 stimulus images no face was detected and the whole image was used.
- **Transformation penalties for the extensions.** The extension models have no published penalty terms and use those of the core model with the same architecture.
- **Hardware.** TensorFlow ran on the CPU and PyTorch on the GPU with cuDNN disabled. Neither changes results beyond floating-point rounding; the re-extraction check matched the release.
- **The data.** The faces are mostly White US adults, the ratings come from US online workers, demographic labels are perceived rather than self-reported, and the hold-out set differs from the main set in age and race (*Faces and human ratings*). Conclusions are limited accordingly.
