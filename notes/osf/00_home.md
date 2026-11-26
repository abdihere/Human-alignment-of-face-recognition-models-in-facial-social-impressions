# Human alignment of face-recognition models and facial social impressions

**Status:** Ongoing

## The study

Face-recognition models turn a face into a list of numbers. Some models judge face similarity more like people do than others; this is their _alignment_. This thesis asks whether more aligned models give more **specific** predictions of people's social impressions of faces (trustworthy, kind, attractive, …). The measure is **excess leakage**: how much a model's prediction of one trait tracks other traits beyond the entanglement already present in people's own ratings.

## Research questions

|         | Question                                                                                                                                                       | Role                       |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| **H1**  | Across 16 models, is higher alignment associated with lower excess leakage, controlling for recognition accuracy (d′, d′²) and mean trait-prediction accuracy? | the only confirmatory test |
| **H1b** | Does Hojjati et al.'s alignment transformation, retrained without the evaluation faces, lower excess leakage on 544 unseen faces?                              | secondary                  |
| **Q2**  | Does the structure of predicted impressions become richer than prediction noise alone would produce as alignment rises?                                        | exploratory                |
| **Q3**  | Do predictions show larger demographic gaps than people's ratings (gender, White vs non-White, their combination, age), and does this change with alignment?   | exploratory                |
| **Q4**  | Does measured memorability relate to alignment differently from the social traits?                                                                             | exploratory                |

## Data and models

- **Data:** 2,222 rated faces from Bainbridge et al. (2013); similarity trials and model embeddings from Hojjati et al. (2026); the Chicago Face Database as an external check.
- **Models:** 16 face-recognition models in 12 families: the 14 recognition models in the Hojjati et al. release and two openly available networks (w600k_r50, IRV1-casia).
- **Sharing:** no images, raw ratings or CFD rows are shared here.

## Pages

1. Data and materials
2. Models, pipelines and the freeze
3. Measures and analysis plan
4. Hypotheses and decision rules
5. Validation and power
6. Rules and fallbacks
7. Existing data and disclosures
8. Primer and glossary
9. Where things live and what results mean

## Links

- [Open Science Framework](https://osf.io/n5hdm)
- [Code repository](https://github.com/abdihere/Human-alignment-of-face-recognition-models-in-facial-social-impressions)
