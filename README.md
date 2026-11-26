# Human alignment of face recognition models in facial social impressions

Master's thesis project. Code, derived data and preregistration materials.

**Preregistration:** [OSF project](https://osf.io/n5hdm)

## The question

Social perception research often measures face impressions (trustworthiness, kindness, attractiveness, …) by mapping the embeddings of a face-recognition network onto human ratings. The network is usually chosen for its recognition accuracy. Hojjati et al. (2026) showed that recognition accuracy and agreement with human face perception (_alignment_) are distinct properties: beyond a certain level of performance, they trade off.

This project asks whether alignment, rather than accuracy, determines how _specific_ such trait measures are. The outcome is **excess leakage**: how much a model's prediction of one trait also tracks other traits, beyond the entanglement already present in people's own ratings.

|         | Question                                                                                                                                        | Status       |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **H1**  | Across 16 models, is higher alignment associated with lower excess leakage, controlling for recognition accuracy and trait-prediction accuracy? | confirmatory |
| **H1b** | Does Hojjati et al.'s alignment transformation lower excess leakage on 544 faces it was not trained on?                                         | secondary    |
| **Q2**  | Does the structure of predicted impressions become richer as alignment rises?                                                                   | exploratory  |
| **Q3**  | Are predictions more demographically uneven than people's ratings, and does this change with alignment?                                         | exploratory  |
| **Q4**  | Does alignment matter differently for memorability than for social traits?                                                                      | exploratory  |

The full rationale, design and decision rules are in the preregistration pages, also kept in [`notes/osf/`](notes/osf/).

## Data and models

- **Faces and ratings:** the 2,222 rated faces of the 10k US Adult Faces Database (Bainbridge, Isola & Oliva, 2013).
- **Similarity judgments and embeddings:** Hojjati et al. (2026), [Zenodo, version 2](https://doi.org/10.5281/zenodo.21867002).
- **External check and recognition test:** Chicago Face Database 3.0.1 (Ma, Correll & Wittenbrink, 2015).
- **Models:** 16 face-recognition models in 12 families. Fourteen come from the Hojjati et al. release; two (ResNet-50 WebFace600K, Inception-ResNet-v1 CASIA-WebFace) were extracted for this project.

No source data, images or model weights are redistributed here. The repository contains checksum lists ([`datasets/MANIFEST.sha256`](datasets/MANIFEST.sha256), [`models/MANIFEST.sha256`](models/MANIFEST.sha256)) so that anyone who obtains the files from their owners can verify they are identical.

## Repository layout

| Path                                  | Contents                                                                                                             |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `notebooks/01_data_and_release.ipynb` | data checks, face sets, ratings and reliability, demographics, alignment and recognition accuracy of the core models |
| `notebooks/02_extension_models.ipynb` | extraction of the two extension models, pipeline check, copy check                                                   |
| `notebooks/02b_h1_power.ipynb`        | power of the H1 test with the real model-level predictors                                                            |
| `notebooks/03_analysis.ipynb`         | the full analysis; synthetic mode before registration, real mode after                                               |
| `results/data/`                       | outputs of notebook 01                                                                                               |
| `results/models/m2/`                  | outputs of notebooks 02 and 02b                                                                                      |
| `results/analysis/synthetic/`         | synthetic run of notebook 03                                                                                         |
| `results/analysis/real/`              | real run of notebook 03 (after registration)                                                                         |
| `notes/osf/`                          | preregistration pages and their figures                                                                              |
| `environment/`                        | exact package versions                                                                                               |
| `datasets/`, `models/`                | checksum lists only                                                                                                  |

## Reproducing

1. Obtain the three datasets from their owners and place them as listed in `datasets/MANIFEST.sha256`; verify with
    ```
    sha256sum -c datasets/MANIFEST.sha256
    ```
2. For notebook 02 only, download the model weights and verify them against `models/MANIFEST.sha256`.
3. Create a Python 3.11 environment:
    ```
    pip install -r environment/requirements-models.lock.txt
    ```
4. Run the notebooks in order. Notebook 03 runs in synthetic mode by default; real mode is locked until the registration link is filled in.

## References

Bainbridge, W. A., Isola, P., & Oliva, A. (2013). The intrinsic memorability of face photographs. _Journal of Experimental Psychology: General, 142_(4), 1323–1334. https://doi.org/10.1037/a0033872

Hojjati, S., Keshvari Ghadikolai, D., Shakeripour, A., Bahmani, Z., Shibata, K., Lau, H., & Moharramipour, A. (2026). _Trade-off between performance and human-like perception in face recognition models_ [Preprint]. PsyArXiv. https://doi.org/10.31234/osf.io/bz3f9_v4

Ma, D. S., Correll, J., & Wittenbrink, B. (2015). The Chicago face database: A free stimulus set of faces and norming data. _Behavior Research Methods, 47_(4), 1122–1135. https://doi.org/10.3758/s13428-014-0532-5
