# SPANISH NOVEL GENERATOR

This proyect aims to stablish a concept prove of a finetuned language model that helps the user to generate an an story that takes care of the actual concept. This would help a writer con ensanche the creativity. The model will be fine tuned to Spanish language. 

## 1. Generate txt files from .epub

1. From proyect root folder, create a 'books/txt' and 'books/epub' directories
2. Put all required .epub files on 'books/epub'
3. From proyect roon folder, run:

```bash
python3 script/epub2txt-generator.py --workdir $(pwd)
```
	 
