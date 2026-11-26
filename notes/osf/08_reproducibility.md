# Reproducibility

Everything in this registration can be recomputed from the original data with the code in the [project repository](https://github.com/abdihere/Human-alignment-of-face-recognition-models-in-facial-social-impressions). This page lists the data sources and how to obtain them, the checksums that identify the exact files used, the model weights and software environment, what is frozen at registration, and how to rerun the analysis.

## Data sources

None of the source data are redistributed in the repository. Each dataset must be obtained from its owner, under that owner's terms.

| Dataset | What the study uses | Access |
|---|---|---|
| Hojjati et al. (2026), [Zenodo, version 2](https://doi.org/10.5281/zenodo.21867002) (10 August 2026) | similarity trials and human rankings; embeddings of 14 models; recognition pairs; released splits; transformation code, training triplets and trained matrices | public, CC BY 4.0 |
| Bainbridge, Isola & Oliva (2013), 10k US Adult Faces Database, 2,222-face annotated subset | per-rater ratings of 20 attributes; perceived race, gender and age; memorability | from the database authors, under their terms of use |
| Chicago Face Database 3.0.1 (Ma, Correll & Wittenbrink, 2015) | 597 stimulus photographs; 1,207 recognition photographs; self-reported race and gender; ratings of attractiveness, trustworthiness and happiness | [chicagofaces.org](https://www.chicagofaces.org), under the CFD licence |

## Checksums

The repository tracks a SHA-256 checksum for every data file used ([`datasets/MANIFEST.sha256`](https://github.com/abdihere/Human-alignment-of-face-recognition-models-in-facial-social-impressions/blob/main/datasets/MANIFEST.sha256)) and for every model weight file ([`models/MANIFEST.sha256`](https://github.com/abdihere/Human-alignment-of-face-recognition-models-in-facial-social-impressions/blob/main/models/MANIFEST.sha256)). Anyone who obtains the data can confirm they have the same files with `sha256sum -c datasets/MANIFEST.sha256`. The key input files are:

| Group | Path | SHA-256 |
|---|---|---|
| zenodo | `datasets/external/hojjati_zenodo/Split_data/All_Similarity_trials.npy` | `bcd3c322550cc55f3c04e8b152bc5d52232c2ae9ae97a40ea5032ba4a4b325c9` |
| zenodo | `datasets/external/hojjati_zenodo/Split_data/All_Similarity_scores.npy` | `f9e5143a16246a389391bbb6fd47f98deee0b48ed0b29fd82cf02555b52ab762` |
| zenodo | `datasets/external/hojjati_zenodo/Split_data/USAFD_Similarity_trials.npy` | `dba968ceb1549fb29387efdcae9b493f8e9075861948ac2163290070b5c51d64` |
| zenodo | `datasets/external/hojjati_zenodo/Split_data/USAFD_Similarity_scores.npy` | `3ce48c2c372ad92166f27baccc826df72188737df09385f82552556749fde59a` |
| zenodo | `datasets/external/hojjati_zenodo/Split_data/CFD_Similarity_trials.npy` | `81da6db707fcdd55cc2ba1c017dbf494eb63c5fc77f60127bc5dee78f09273f2` |
| zenodo | `datasets/external/hojjati_zenodo/Split_data/CFD_Similarity_scores.npy` | `2cc87048a8d0eff214a0a251c5e98cd42c075a8978f744e00d178929301e49f0` |
| zenodo | `datasets/external/hojjati_zenodo/Split_data/train.npy` | | `c1c28f36d3d29c3b551505970321d67ce19755cc9d1043557eb7284ef923d41d` |
| zenodo | `datasets/external/hojjati_zenodo/Split_data/val.npy` | | `fd61d44c388e9a578589ba40ef0d2a59843802f83cd56d387d113cdaca808afa` |
| zenodo | `datasets/external/hojjati_zenodo/Recognition_task_pairs/positive_pairs.npy` | `011d389743fdfc3d8093e5086515731f0145da1b7dd3d7375249e8799def9294` |
| zenodo | `datasets/external/hojjati_zenodo/Recognition_task_pairs/negative_pairs.npy` | `a34c5d7047f0294c5403ed8933a393fc95408918e412088fa7b649520c685763` |
| zenodo | `datasets/external/hojjati_zenodo/Models_alignment.pkl` | `eff13b353dbdd0fdc2a6b5dce8467658b6908c74faa9df5b49ca6a90f1c08c01` |
| zenodo | `datasets/external/hojjati_zenodo/Regularization_terms.pkl` | | `31e0956df3ab8b03c51b23ec581a676a15d92952a9137867dbaad80a3d51efe6` |
| zenodo | `datasets/external/hojjati_zenodo/code/Training.py` | | `5de3f3b3aa93748659fe1f5b9ad3eb9d3d99ae725f7962062896a4cf7b1a5ed1` |
| zenodo | `datasets/external/hojjati_zenodo/code/Transformation_matrix_trainer_model.py` | | `a28d62141550451eb0e176fd94f038030487b2a277f92e12ccdac6ab49cb16d0` |
| zenodo | `datasets/external/hojjati_zenodo/Trained_Ws_PCs/Note.txt` | `fe839b5bd5507f36f6fab256cd311f65bb28d601b5a389cd4db602ea5c81bb37` |
| bainbridge | `datasets/raw/2kattributes/target-filenames.txt` | `7fb61e5b1b6295eb5edc945a4c79928747c62be61d624b7f751c50b2afb121fc` |
| bainbridge | `datasets/raw/2kattributes/demographic & others labels/demographic-others-labels.xlsx` | `f5035bffe70096ab91094ce8a51efedeb6faaa2092a7fa1fd3ea0c704536c014` |
| bainbridge | `datasets/raw/2kattributes/psychology attributes/psychology-attributes.xlsx` | `4d35e66ef4eb8bdcf25eeef98f79fe520f2a85dd416bbb1bd8d0bf41e1e63634` |
| bainbridge | `datasets/raw/2kmemorability/memorability-scores.xlsx` | `61f2cd48c2c05eade2bc2d82f43e904a68b8f0ba333a30a5b4b6645e149022b8` |
| cfd | `datasets/raw/cfd/CFD 3.0.1 Norming Data and Codebook.xlsx` | `2e45a6fa4f27800cf99abeeb66565da8c1317da8bebd8a578b4deca78ebad3ae` |

## Model weights

The 14 core models need no weights: their embeddings come from the Zenodo release. The two extension models were extracted from public weights.

| Model | Weights | Licence | SHA-256 |
|---|---|---|---|
| ResNet-50 WebFace600K | `w600k_r50.onnx`, InsightFace `buffalo_l`, release v0.7 | InsightFace pretrained models: non-commercial research only | `4c06341c33c2ca1f86781dab0e829f88ad5b64be9fba56e56bc9ebdefc619e43` |
| Inception-ResNet-v1 CASIA | model 20180408-102900 (Sandberg), via facenet-pytorch | MIT; CASIA-WebFace has its own research terms | `7a67afdbbc995fce5e10128675e318799a70698c2f433ba75dd7eb9a2f096e7d` |

The face detector (RetinaFace) and the two core models re-extracted for the pipeline check (FaceNet512, GhostFaceNet) are also listed in `models/MANIFEST.sha256`.

## Software environment

Python 3.11.18, with NumPy 1.26.4, pandas 3.0.6, scikit-learn 1.9.1, TensorFlow 2.21.0 (with tf-keras 2.21.0), PyTorch 2.2.2 (CUDA 12.1), onnxruntime 1.32.0, deepface 0.0.105 and retina-face 0.0.19. The exact versions of every package are in [`environment/requirements-models.lock.txt`](https://github.com/abdihere/Human-alignment-of-face-recognition-models-in-facial-social-impressions/blob/main/environment/requirements-models.lock.txt). TensorFlow ran on the CPU and PyTorch on an NVIDIA RTX 4060 Ti with cuDNN disabled.

## The freeze

Before registration, the following are fixed in a tagged commit of the repository, and the registration cites that tag:

- the model list and families (*Models*);
- the data and weight checksum lists;
- the derived human data (`results/data/trait_scores_20.csv`, `reliability.csv`, `face_sets.csv`);
- the model-level predictors (`results/data/models_table.csv`, `results/models/m2/predictors_m2.csv`);
- the checksums of the extension models' embeddings (`results/models/m2/cache_MANIFEST.sha256`), which are not tracked themselves;
- the face-level fold partition (`results/analysis/folds_10x5.csv`);
- the analysis notebook (`notebooks/03_analysis.ipynb`) and the environment lock file;
- the transformation code (Zenodo version 2) and its validation (`results/analysis/transform_validation.csv`).

**Freeze tag:** [to be added] · **Commit:** [to be added] · **Date:** [to be added]

## Repository layout

| Path | Contents |
|---|---|
| `notebooks/01_data_and_release.ipynb` | data checks, face sets, ratings, reliability, demographics, alignment and recognition accuracy of the core models |
| `notebooks/02_extension_models.ipynb` | extraction of the extension models, pipeline check, copy check |
| `notebooks/02b_h1_power.ipynb` | power of H1 with the real predictors |
| `notebooks/03_analysis.ipynb` | the full analysis: synthetic mode before registration, real mode after |
| `results/data/`, `results/models/m2/` | outputs of notebooks 01, 02 and 02b |
| `results/analysis/synthetic/` | the synthetic run of notebook 03 |
| `results/analysis/real/` | the real run, after registration |
| `notes/osf/` | these pages and their figures |
| `datasets/`, `models/` | checksum lists only; the files themselves are not tracked |

## How to reproduce

1. Obtain the three datasets from their owners, place them as listed in `datasets/MANIFEST.sha256`, and check them with `sha256sum -c`.
2. Download the model weights and check them against `models/MANIFEST.sha256` (needed only for notebook 02).
3. Create the environment from the lock file.
4. Run the notebooks in order. Notebook 03 runs on real data only after the registration link has been entered.

## References

Bainbridge, W. A., Isola, P., & Oliva, A. (2013). The intrinsic memorability of face photographs. *Journal of Experimental Psychology: General, 142*(4), 1323–1334. https://doi.org/10.1037/a0033872

Hojjati, S., Keshvari Ghadikolai, D., Shakeripour, A., Bahmani, Z., Shibata, K., Lau, H., & Moharramipour, A. (2026). *Trade-off between performance and human-like perception in face recognition models* [Preprint, version 4]. PsyArXiv. https://doi.org/10.31234/osf.io/bz3f9_v4. Data and code: https://doi.org/10.5281/zenodo.21867002 (version 2).

Ma, D. S., Correll, J., & Wittenbrink, B. (2015). The Chicago face database: A free stimulus set of faces and norming data. *Behavior Research Methods, 47*(4), 1122–1135. https://doi.org/10.3758/s13428-014-0532-5
