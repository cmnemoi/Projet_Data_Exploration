# Projet Data Exploration

## Etienne Aubry et Charles-Meldhine Madi Mnemoi

Nécessite [Miniconda](https://conda.io/miniconda.html).

Installation des dépendances :

```bash
conda create -n projet_data_exploration python=3.10
conda activate projet_data_exploration
pip install -r requirements.txt
```

Exporter le notebook en tant que pdf (pas essayé, c'est super long) :
```bash
jupyter nbconvert --to webpdf --allow-chromium-download Projet_Data_Exploration.ipynb
```
