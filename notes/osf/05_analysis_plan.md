# Analysis plan

This page defines every measure and every step of the analysis, in the order they are carried out. The code is `notebooks/03_analysis.ipynb`. Before registration it has run only on simulated data (*Sensitivity and validation*). After registration it will be run once on the real data, without changes. The notebook refuses to run on real data until the registration link has been entered.

## 1. Predicting traits from each model

The first step reproduces the standard procedure described on *Background and rationale*: for each model, a linear read-out predicts each human trait score from the model's embedding.

- **Features.** The model's embedding, L2-normalised and then standardised using the means and standard deviations of the training faces.
- **Regression.** Ridge regression, fitted separately for each trait. The penalty is chosen by five-fold cross-validation within the training faces, from 25 log-spaced values between 10⁻³ and 10⁴ times the number of training faces, and the model is then refitted on all training faces with the chosen penalty. Ridge is the method used by Keles et al. (2021) and is well suited to embeddings with more dimensions than faces.
- **Targets.** The 14 social traits; the six other attributes (for a sensitivity analysis of Q2); and memorability (Q4).

**Main set: out-of-fold predictions.** The 1,678 main faces are divided into 10 folds, stratified by gender and White/non-White, and each fold is predicted by a model fitted on the other nine. The procedure is repeated with five different partitions. Every face is thus predicted five times, each time by a model that never saw it. The partition is written once from a fixed seed (`results/analysis/folds_10x5.csv`) and checked on every later run. Folds divide faces, not similarity trials; the released splits of Hojjati et al. divide trials and so let a third of the test faces appear in training (*Faces and human ratings*).

**Hold-out set.** One model per trait, fitted on all 1,678 main faces, predicts the 544 hold-out faces and the 597 CFD faces.

## 2. The outcome: excess leakage

For model *m* and an ordered pair of traits (*i*, *j*), four correlations are computed across faces:

- ρᵢ, the correlation between predicted and human scores for trait *i* (the model's accuracy on *i*);
- Lᵢⱼ, the correlation between the prediction of *i* and the human scores of *j* (leakage of *i* into *j*);
- rᵢⱼ, the correlation between the human scores of *i* and *j*;
- Rᵢ, the reliability of the human scores of trait *i* (*Faces and human ratings*).

**Excess leakage** is ELᵢⱼ = Lᵢⱼ − ρᵢ · rᵢⱼ / Rᵢ.

The subtracted term is the leakage a prediction would show if it were the true trait plus independent noise. In that case its correlation with human trait *j* is fully explained by how well it captures trait *i* and how strongly people's ratings of *i* and *j* are related. The ρᵢ factor prevents weak models from appearing less leaky simply because their predictions correlate less with everything; dividing by Rᵢ corrects the human correlation for noise in the ratings. A positive ELᵢⱼ means that the prediction of *i* borrows from trait *j* beyond what human entanglement explains. *Sensitivity and validation* shows that the estimator is zero, to within 0.005, when there is no excess leakage, and rises in proportion when leakage is added.

**L(m)** is the mean of sign(rᵢⱼ) · ELᵢⱼ over the 182 ordered pairs of the 14 traits. Multiplying by the sign of the human correlation counts leakage in the direction of the human relation as positive, so that leakage for negatively related traits does not cancel leakage for positively related ones.

- **Primary outcome:** L(m) on the main set, from the out-of-fold predictions, computed for each of the five partitions and averaged.
- **Hold-out outcome:** L(m) on the 544 hold-out faces, used in the third condition of H1.
- **Uncorrected L(m),** without the reliability correction (ELᵢⱼ = Lᵢⱼ − ρᵢ · rᵢⱼ), as a sensitivity analysis.
- **Independent-rater baseline.** Part of the human correlation rᵢⱼ may itself be halo produced by the same raters judging several traits. As a sensitivity analysis, rᵢⱼ is recomputed with trait *i* scored by one random half of each face's raters and trait *j* by the other half, rescaled to the reliability of full scores and averaged over 50 splits.

Only differences between models are interpreted. The absolute level of L(m) depends on the estimator and is not read on its own.

## 3. H1: alignment and excess leakage

Across the 16 models, L(m) is regressed by ordinary least squares on four standardised predictors:

- alignment (USAFD trials);
- recognition accuracy, centred (d′ − mean d′), and its square, because alignment and accuracy are related nonlinearly (*Models*);
- mean trait accuracy, the mean of ρᵢ over the 14 traits.

The coefficient for alignment carries the test. With 16 observations and 12 families, conventional standard errors would be too optimistic, and standard cluster-robust errors are unreliable with so few clusters. The test therefore uses a **wild cluster bootstrap-t** (Cameron, Gelbach, & Miller, 2008), with the null hypothesis imposed (the model refitted without alignment), Webb's six-point weights drawn per family (Webb, 2023), CR1 cluster-robust standard errors and 9,999 draws. The p-value is one-sided (lower tail). Two further conditions follow: the model is refitted 12 times, each time leaving out one family, and once with hold-out L(m) as the outcome. The decision rule is stated on *Research questions and hypotheses*.

## 4. H1b: the alignment transformation

**The transformation.** Hojjati et al.'s method is used unchanged, with their code from the Zenodo release. Each embedding is L2-normalised and projected onto principal components fitted on the training faces. A 100 × 100 matrix is learned for the first 100 components, with a separate scale for each further component. Training uses triplets of a reference face and two candidates, the one people ranked as more similar and the one ranked as less similar, with a loss weighted by the difference in human ranks (Adam, learning rate 0.002, gradient clipping 0.5, batch size 256, 30 epochs, model-specific L1/L2 penalties from the release). The transformed embedding is the principal-component scores multiplied by the learned matrix.

**Main test, on the hold-out faces.** Hojjati et al.'s released matrices were trained on 140,879 triplets that contain no hold-out face. For the 14 core models the released matrices are used as published. The two extension models have no released matrix, so they are trained with the same code on the same triplets, using the penalties of the core model with the same architecture (ArcFace-50 for the ResNet-50, FaceNet512 for the Inception-ResNet-v1).

For each model, the main and hold-out embeddings are transformed, a ridge read-out is fitted on the main faces, and L(m) is computed on the hold-out faces. **ΔL = L(raw) − L(aligned)**; a positive value means the transformation lowered excess leakage. ΔL is tested with a one-sided Wilcoxon signed-rank test over the 16 models, and a family-clustered bootstrap gives a 95% interval for its mean.

**Controls.** Two control transformations go through the same steps:

- a **placebo**, trained with the same code and triplets but with the order of each triplet flipped at random, so that it learns no human similarity information;
- a **matched-spectrum random matrix**, with the singular values of the real transformation but random orthogonal directions, so that it changes the embedding's geometry by the same amount without the learned content.

**Manipulation check.** Alignment on similarity trials that the transformation did not see is compared before and after transformation, using the trials held out in the supporting analysis below.

**Supporting analysis on the main faces.** One five-fold partition of the main faces (seed 501) is used. For each fold, a transformation is trained on the released triplets that contain none of that fold's faces; a read-out fitted on the other folds' transformed embeddings predicts the fold. ΔL is computed from these out-of-fold predictions.

**Validation of the training code.** Before registration, the code was run for Dlib and SFace on the released triplets with three random seeds. The released matrices' alignment fell inside the range of the retrained ones in both cases (*Sensitivity and validation*).

## 5. Q2: structure of predicted impressions

For each model, the 14 out-of-fold predicted trait scores (averaged over the five partitions) are summarised by:

- the share of variance on the first principal component;
- the effective rank, the exponential of the entropy of the normalised eigenvalues, a continuous count of dimensions;
- the number of components above the 95th percentile of column-shuffled data (parallel analysis, 1,000 shuffles);
- Tucker's congruence between the first two components of the predictions and of the human ratings.

Prediction error by itself changes how many dimensions a set of scores appears to have, so a model's structure cannot be compared with the human structure directly. Each model is therefore compared with a **noise-matched null**: the human scores with noise added until each trait's correlation with the original equals the model's ρᵢ (1,000 replicates). Richness beyond noise is the observed effective rank minus the null median; the excess first-component share is defined in the same way. Across models, each summary is related to alignment by Spearman's ρ, with a family-clustered bootstrap 95% interval. A sensitivity analysis uses all 20 attributes.

## 6. Q3: demographic gaps

On the main set, for each trait, the gap between groups in the predicted scores is compared with the gap in the human scores of the same faces:

- women against men, and White against non-White faces: the difference in Cohen's d (pooled SD);
- age: the difference in Spearman correlation with the continuous age score.

The **disparity index** is the mean absolute excess gap over the 14 traits and three contrasts. Across models, it is related to alignment by Spearman's ρ with a family-clustered bootstrap 95% interval. Race × gender cells, each compared with all other faces, are described; cells with fewer than 50 faces are flagged. CFD ratings are not used here, because they were made relative to faces of the same race and gender.

## 7. Q4: memorability

The target is the logit of the hit rate (rates clipped to [0.005, 0.995]); the logit false-alarm rate and memorability d′ are sensitivity targets. For each target and for each of the 14 traits, alignment is related to out-of-fold prediction accuracy across models by Spearman's ρ. Memorability is classified as *distinct* if its association falls below the 25th percentile of the 14 trait associations, and *not distinct* otherwise. Accuracy is not divided by a reliability ceiling: this would not change a rank correlation across models, and memorability has no reliability estimate.

## 8. Chicago Face Database check

Predictions for the 597 CFD faces, from each model's fit on the main faces, are compared with the CFD ratings of attractiveness, trustworthiness and happiness. Because CFD raters judged faces relative to others of the same race and gender, correlations are computed within race × gender cells with at least 20 faces and pooled by Fisher's z, weighted by n − 3. The check is descriptive.

## 9. Software

Python 3.11 with NumPy 1.26, SciPy, pandas and scikit-learn; TensorFlow 2.21 for the transformation code. The full environment is in `environment/requirements-models.lock.txt` (*Reproducibility*). All random steps use fixed seeds set in the notebook.

## References

Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. *The Review of Economics and Statistics, 90*(3), 414–427. https://doi.org/10.1162/rest.90.3.414

Keles, U., Lin, C., & Adolphs, R. (2021). A cautionary note on predicting social judgments from faces with deep neural networks. *Affective Science, 2*(4), 438–454. https://doi.org/10.1007/s42761-021-00075-5

Webb, M. D. (2023). Reworking wild bootstrap-based inference for clustered errors. *Canadian Journal of Economics, 56*(3), 839–858. https://doi.org/10.1111/caje.12661
