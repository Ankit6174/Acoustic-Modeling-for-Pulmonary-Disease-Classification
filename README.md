# Acoustic Modeling for Pulmonary Disease Classification

This repository is a machine learning and deep learning pipeline for pulmonary disease classification using acoustic lung sound data. It collects the complete workflow from exploratory data analysis and feature engineering to model training, augmentation experiments, and inference.

![Project overview](Slide%2016_9%20-%202.jpg)

## What’s in this project

- `ICBHI_final_database/` – raw lung sound recordings and annotations from the ICBHI dataset.
- `Data Augmentation.ipynb` – experiments and methods for augmenting acoustic data.
- `EDA.ipynb` – exploratory data analysis and dataset inspection.
- `Feature Engineering.ipynb` – feature extraction and preprocessing for modeling.
- `Model Training Pipeline.ipynb` – the main training workflow and pipeline steps.
- `Inference.ipynb` – inference examples using saved models.
- `Model Training/` – additional experiment notebooks, model outputs, and organized training artifacts.

## Quick summary

I built this project to classify pulmonary disease from acoustic signals using the ICBHI dataset. The repo is centered on notebook-driven research, so the key work happens in the notebooks listed above.

## Recommended workflow

1. Open `EDA.ipynb` to understand the dataset and distribution.
2. Run `Feature Engineering.ipynb` to extract features and prepare training data.
3. Use `Data Augmentation.ipynb` to test augmentation techniques if needed.
4. Train and validate models in `Model Training Pipeline.ipynb`.
5. Try `Inference.ipynb` for prediction examples on saved models.

## Future next step

Eventually I want to build a website and REST API around this model, so users can upload a respiratory cycle and get a pulmonary disease prediction from our model’s API. This repo is the core model development, and the next phase will be turning it into an app where the model can be used from the web.