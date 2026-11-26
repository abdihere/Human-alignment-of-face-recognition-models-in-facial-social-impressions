# Glossary

## The study in brief

1. A face-recognition network turns a photograph into a list of numbers, its **embedding**. Two photographs of the same person should receive similar embeddings.
2. **Alignment** asks whether the network's sense of which faces look alike matches people's. People ranked four faces by their similarity to a fifth; the network ranks them by the distance between embeddings; alignment is how well the two rankings agree.
3. From an embedding, a simple linear read-out can learn to predict how people rated a face on a trait such as trustworthiness.
4. People's impressions are entangled: faces seen as kind are also seen as trustworthy. A network's trustworthiness prediction can track kindness even more than people's ratings do. **Excess leakage** measures that extra entanglement.
5. The main question is whether more aligned networks show less excess leakage, independent of how well they recognise faces.

## Terms

| Term | Meaning |
|---|---|
| **Alignment** | Mean Spearman correlation between a model's and people's rankings of four candidate faces by similarity to a reference face, over the similarity trials of Hojjati et al. (2026). The H1 predictor uses the trials with USAFD faces only. |
| **AUC** | Area under the ROC curve, a common measure of recognition accuracy; not used because it is near 1.0 for several models. |
| **CFD** | Chicago Face Database: standardised photographs with self-reported demographics and their own trait ratings. |
| **Copy check** | The test of whether a candidate model duplicates one already in the set, using representational similarity and row-wise cosine. |
| **CR1** | A small-sample correction for cluster-robust standard errors. |
| **d′ (d-prime)** | Recognition accuracy: the distance between the similarity scores of same-person and different-person photograph pairs, in units of their pooled standard deviation. |
| **Discriminant validity** | The extent to which a measure of one construct does not also measure other constructs (Campbell & Fiske, 1959). |
| **Effective rank** | A continuous count of the dimensions in a set of scores: the exponential of the entropy of the normalised eigenvalues. |
| **Embedding** | The vector a model produces for a face (128 to 4,096 numbers here). |
| **Excess leakage, ELᵢⱼ** | Lᵢⱼ − ρᵢ · rᵢⱼ / Rᵢ: how much a model's prediction of trait *i* tracks human ratings of trait *j*, beyond what the human correlation between the traits and the model's accuracy on *i* explain. |
| **Family** | A group of models sharing an architecture lineage and training data, treated as one cluster in the inference. |
| **Halo effect** | The tendency of an overall impression to colour judgments of separate traits (Thorndike, 1920). |
| **Hold-out set** | The 544 USAFD faces that appear in no similarity trial, and therefore in no transformation's training data. |
| **L(m)** | A model's overall excess leakage: the mean of sign(rᵢⱼ) · ELᵢⱼ over the 182 ordered pairs of the 14 traits. |
| **Leave one family out** | Refitting the H1 model 12 times, each time without one family, to check that no single family drives the result. |
| **Lens model** | Brunswik's (1956) account of perception as inferring hidden attributes from observable cues. |
| **Main set** | The 1,678 USAFD faces that appear in at least one similarity trial. |
| **Manipulation check** | The test that the alignment transformation actually raises alignment on similarity trials it was not trained on. |
| **Matched-spectrum control** | A random transformation with the same singular values as the real one, which changes the geometry of the embedding by the same amount without its learned content. |
| **Noise-matched null** | The human ratings degraded with noise to a model's accuracy; it shows what structure prediction error alone produces. |
| **Out-of-fold prediction** | A prediction for a face made by a read-out fitted without that face. |
| **Placebo transformation** | The alignment transformation trained on triplets whose order was flipped at random, so that it learns no human similarity information. |
| **Reliability, Rᵢ** | Agreement between two random halves of the raters of each face, corrected to full length with the Spearman–Brown formula. |
| **Ridge regression** | Linear regression with a penalty that shrinks the weights; the penalty is chosen by cross-validation. |
| **ρᵢ (trait accuracy)** | The correlation between a model's predicted and the human scores for trait *i*. |
| **rᵢⱼ** | The correlation between the human scores of traits *i* and *j*. |
| **RSA** | Representational similarity analysis: the correlation between two models' face-to-face distance matrices. |
| **Row-wise cosine** | The cosine between two models' embeddings of the same face; high only when the models share weights. |
| **Transformation** | Hojjati et al.'s learned linear map that brings a model's face distances closer to people's similarity rankings. |
| **Triplet** | A reference face with two candidates, the one people ranked as more similar and the one ranked as less similar; the unit of training for the transformation. |
| **USAFD** | The 10k US Adult Faces Database (Bainbridge et al., 2013); this study uses its 2,222 rated faces. |
| **Wild cluster bootstrap-t** | A test that resamples the residuals of whole clusters with random weights; reliable with few clusters (Cameron et al., 2008). |

## References

Bainbridge, W. A., Isola, P., & Oliva, A. (2013). The intrinsic memorability of face photographs. *Journal of Experimental Psychology: General, 142*(4), 1323–1334. https://doi.org/10.1037/a0033872

Brunswik, E. (1956). *Perception and the representative design of psychological experiments*. University of California Press.

Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. *The Review of Economics and Statistics, 90*(3), 414–427. https://doi.org/10.1162/rest.90.3.414

Campbell, D. T., & Fiske, D. W. (1959). Convergent and discriminant validation by the multitrait-multimethod matrix. *Psychological Bulletin, 56*(2), 81–105. https://doi.org/10.1037/h0046016

Hojjati, S., Keshvari Ghadikolai, D., Shakeripour, A., Bahmani, Z., Shibata, K., Lau, H., & Moharramipour, A. (2026). *Trade-off between performance and human-like perception in face recognition models* [Preprint, version 4]. PsyArXiv. https://doi.org/10.31234/osf.io/bz3f9_v4

Thorndike, E. L. (1920). A constant error in psychological ratings. *Journal of Applied Psychology, 4*(1), 25–29. https://doi.org/10.1037/h0071663
