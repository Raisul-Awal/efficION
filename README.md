[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org) [![tensorflow](https://img.shields.io/badge/TensorFlow-1.12-FF6F00.svg?style=flat&logo=tensorflow)](https://www.tensorflow.org) ![user](https://img.shields.io/badge/GoogleColab-grey?style=flat&logo=googlecolab) ![user](https://img.shields.io/badge/Chemodeling-App-yellow?) ![user](https://img.shields.io/badge/Userfriend-1.0-sgreen?) 

# efficION: ionization efficiency prediction <br/> <br/> <br/> <img align = "center" width="650" alt="image" src="https://github.com/mitkeng/efficION/assets/97419520/1bb3418f-9207-4d26-8546-d691a93af168">

### Introduction 
efficION is a python program for predicting mass spectrometry relevant compound ionization efficiency. Two interacting deep neural network models are implemented for log ionization efficiency (logIE) value prediction and error attenuation; one sequential model (*i.e.*, model 1) predicts logIE while a second sequential model (*i.e.*, model 2) attempts to correct for residual logIE prediction error produced by model 1.
<br />
<br /><img align = "center" width="800" alt="image" src="https://github.com/mitkeng/efficION/assets/97419520/68bb2584-95dc-4f1b-85da-dafc5388521a">


#
### Functionality
The program supports single logIE query or batch chemical logIE queries. For single query, either a canonical SMILE or chemical name is applicable, along with a required solution pH value; for batch queries, the following csv file data format is required:
|| SMILES| pH|
|--| ------------- | ------------- |
|1| C1=CNC(=O)NC1=O| 7.2|
|n| ... | ...|

Upon completion of a task a tabulated result similar to the table below is saved to a csv file.

|| Chemical Name| SMILE| logIE|
|---|------|-----|----|
|1| 1H-pyrimidine-2,4-dione  |	C1=CNC(=O)NC1=O	|0.49364716|
|n| ... | ...|...|

Currently, efficION is only appropriate for predicting logIE relating to the ESI ionization technique. 


#
### Performance

<img align = "left" width="400" alt="focus" src="https://github.com/mitkeng/efficION/assets/97419520/8f8bf4bc-e028-4cb7-9ba9-4897faf6da0f">
<img align = "center" width="400" alt="focus" src="https://github.com/mitkeng/efficION/assets/97419520/bb441331-f8c2-4f29-93a0-4a888476dffd">


#
### Requirement
Google account needed to access Google Colab notebook.

#
### Support
To create a small batch queries csv input file *ad hoc*:
```twig
import pandas as pd

try:
  !touch small_batch.csv
except:
  pass

column_names=["SMILES","pH"]
small_batch=pd.read_csv("small_batch.csv", names=column_names)

comp_list = #list of compounds -> ["C(=O)=O", "O"]
pH_list = #list of corresponding pH values -> [2.7, 7.2]

small_batch['SMILES'] = comp_list
small_batch['pH'] = pH_list

small_batch.to_csv("small_batch.csv", index=False)
```

#
### Accessibility
 [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">](https://colab.research.google.com/drive/1t9ki6sLRUjbidTl5rcPJr5BlZCi6TnFT?usp=sharing) <code style="color : grey">to access the efficION platform.</code>
<img align = "right" width="100" alt="focus" src="https://github.com/mitkeng/efficION/assets/97419520/dba56f1a-cce9-434f-b1c0-7ef836041810">


<br />


#
### Reference
Liigand, J., Wang, T., Kellogg, J. et al. Quantification for non-targeted LC/MS screening without standard substances. Sci Rep 10, 5808 (2020). https://doi.org/10.1038/s41598-020-62573-z


