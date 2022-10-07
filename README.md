# SPANISH NOVEL GENERATOR

This proyect aims to stablish a concept prove of a finetuned language model that helps the user to generate an an story that takes care of the actual concept. This would help a writer con ensanche the creativity. The model will be fine tuned to Spanish language. 

### Installation

1. [Install CONDA](https://anaconda.org/conda-forge/conda)
2. Create new environment called `tgen`:
```bash
conda create --name tgen python=3.8
```
3. Activate environment:
```bash
conda activate tgen
```
4. Install python packages:
```bash
conda install -r requirements.txt 
```

### Prepare Data
#### 1. Generate txt files from .epub

1. From proyect root folder, create a 'books/txt' and 'books/epub' directories
2. Put all required .epub files on 'books/epub'
3. From proyect roon folder, run:

```bash
python3 script/epub2txt-generator.py --workdir $(pwd)
```
	 
