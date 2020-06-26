# Bloatectomy
Bloatectomy: a method for the identification and removal of duplicate text in the bloated notes of electronic health records and other documents. Takes in a list of notes or a single file (.docx, .txt, .rtf, etc) or single string to be marked for duplicates which can then be highlighted, bolded, or removed. Marked output and tokens are output.

# Paper
For details about how the package works and our reasons for developing it, read the paper here https://github.com/MIT-LCP/bloatectomy/blob/master/bloatectomy_paper.pdf

# Requirements
- Python>=3.7.x (in order for the regular expressions to work correctly)
- re
- sys
- pandas (optional, only necessary if using MIMIC III data)
- docx (optional, only necessary if input or output is a word/docx file)

# Installation
using anaconda or miniconda
```
conda install -c summerkrankin bloatectomy
```

using pip via PyPI  
make sure to install it to python3 if your default is python2
```
python3 -m pip install bloatectomy
```
using pip via github
```
python3 -m pip install git+git://github.com/MIT-LCP/bloatectomy
```
manual install by cloning the repository
```
git clone git://github.com/MIT-LCP/bloatectomy
cd bloatectomy
python3 setup.py install
```

# Input
The input for Bloatectomy can be a string, or a text file (txt, rtf), or a word (docx) document. See examples below for implementation of each. 

# Output

- **bloatectomized_file.html** = The default output is the input text with highlighted duplicates in html format. The file can be renamed using `filename=`.
- **[filename]_original_token_numbers.txt** = The numbered tokens of the original input text can be exported as a text file by setting `output_original_tokens=True`. 
- **[filename]_token_numbers.txt** = The numbered tokens of the marked output can be exported as a text file by setting `output_numbered_tokens=True` (the token numbers of the two numbered token files will only differ if the `style='remov'` parameter is set).  

# Examples

To use with example text or load ipynb examples, download the repository or just the bloatectomy_examples folder. 
This is the simplest use with default parameters. We only specify the type of marking and the type of output.
```
from bloatectomy import bloatectomy

text = ''Assessment and Plan
61 yo male Hep C cirrhosis
Abd pain:
-other labs: PT / PTT / INR:16.6//    1.5, CK / CKMB /
ICU Care
-other labs: PT / PTT / INR:16.6//    1.5, CK / CKMB /
Assessment and Plan
'''

bloatectomy(text)
```

This example highlights duplicates and creates an html, displays the result in the console, specifies the location and name of the output (`filename=`).

```
bloatectomy('text', 
            style='highlight',
            display=True,
            filename='./output/sample_txt_output',
            output='html')
```

This example removes duplicates and creates an html, displays the result in the console, specifies the location and name of the output (`filename=`), and exports the numbered tokens (useful for dissecting how the text is tokenized). 

```
bloatectomy('text', 
            style='remov',
            display=True,
            filename='./output/sample_txt_remov_output',
            output='html',
            output_numbered_tokens=True,
            output_original_tokens=True)
```

This example takes in the single text file (i.e., sample_text.txt) to be marked for duplicates. The marked output, original numbered tokens and marked numbered tokens are exported. Note that the tokens in the two numbered token files will have the same token numbers unless they style parameter is set to "remov" ```style='remov'```.

```
bloatectomy('./input/sample_text.txt',
             filename='./output/sampletxt_output',
             style='highlight',
             output='html',
             output_numbered_tokens=True,
             output_original_tokens=True )
```

This example takes in and exports a word document and marks duplicates in bold. 
```
bloatectomy('./input/sample_text.docx',
            style='bold',
            output='docx',
            filename='./output/sample_docx_output')
```

This example takes in an .rtf file and exports a word document with duplicates removed. 
```
bloatectomy('./input/sample_text.rtf',
            style='remov',
            output='docx',
            filename='./output/sample_docx_output')
```

# Documentation

```
class bloatectomy(input_text,
                  path = '',
                  filename='bloatectomized_file',
                  display=False,
                  style='highlight',
                  output='html',
                  output_numbered_tokens=False,
                  output_original_tokens=False,
                  regex1=r"(.+?\.[\s\n]+)",
                  regex2=r"(?=\n\s*[A-Z1-9#-]+.*)",
                  postgres_engine=None,
                  postgres_table=None)
```
## Parameters  
**input_text**: file, str, list  
An input document (.txt, .rtf, .docx), a string of text, or list of hadm_ids for postgres mimiciii database or the raw text.

**style**: str, optional, default=`highlight`  
How to denote a duplicate. The following are allowed: `highlight`, `bold`, `remov`.

**output**: str, optional, default=`html`  
Type of marked output file as an html or a word document (docx). The following are allowed: `html`, `docx`.

**filename**: str, optional, default=`bloatectomized_file`
A string to name output file of the marked document.

**path**: str, optional, default=`' '`  
The directory for output files.

**output_numbered_tokens**: bool, optional, default=`False`  
If set to `True`, a .txt file with each token enumerated and marked for duplication is output as `[filename]_token_numbers.txt`. This is useful when diagnosing your own regular expression for tokenization or testing the `remov` option for **style**.

**output_original_tokens**: bool, optional, default=`False`  
If set to  `True`, a .txt file with each original (non-marked) token enumerated but not marked for duplication, is output as `[filename]_original_token_numbers.txt`. This is useful when diagnosing your own regular expression for tokenization or testing the `remov` option for **style**.

**display**: bool, optional, default=`False`  
If set to `True`, the bloatectomized text will display in the console on completion.

**regex1**: str, optional, default=`r"(.+?\.[\s\n]+)"`  
The regular expression for the first tokenization. Split on a period (.) followed by one or more white space characters (space, tab, line breaks) or a line feed character. This can be replaced with any valid regular expression to change the way tokens are created.

**regex2**: str, optional, default=`r"(?=\n\s*[A-Z1-9#-]+.*)"`  
The regular expression for the second tokenization. Split on any line feed character followed by an uppercase letter, a number, or a dash. This can be replaced with any valid regular expression to change how sub-tokens are created.

**postgres_engine**: str, optional
The postgres connection. Only relevant for use with the MIMIC III dataset. When data is pulled from postgres the hadm_id of the file will be appended to the `filename` if set or the default `bloatectomized_file`. See the jupyter notebook [mimic_bloatectomy_example](./bloatectomy_examples/mimic_bloatectomy_example.ipynb) for the example code.

**postgres_table**: str, optional
The name of the postgres table containing the concatenated notes. Only relevant for use with the MIMIC III dataset. When data is pulled from postgres the hadm_id of the file will be appended to the `filename` if set or the default `bloatectomized_file`. See the jupyter notebook [mimic_bloatectomy_example](./bloatectomy_examples/mimic_bloatectomy_example.ipynb) for the example code.

# Contributing

We encourage you to share any additions or changes to our package. To contribute, please:

Fork the repository using the following link: https://github.com/MIT-LCP/bloatectomy/fork. For a background on GitHub forks, see: https://help.github.com/articles/fork-a-repo/

Commit your changes to the forked repository.

Submit a pull request to the MIMIC code repository, using the method described at: https://help.github.com/articles/using-pull-requests/

## License

By committing your code to the Bloatectomy Repository you agree to release the code under the [GNU General Public License v3.0](LICENSE.txt) in this repository.

## Issues or Bugs

Please feel free to create an issue for any questions, bugs, or suggestions you may have about our package or even the documentation (i.e. additional examples). We appreciate any feedback. 
