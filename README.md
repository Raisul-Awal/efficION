## efficION <br/> <br/> <br/> <img align = "center" width="700" alt="image" src="https://github.com/mitkeng/efficION/assets/97419520/1bb3418f-9207-4d26-8546-d691a93af168">

### Introduction 
efficION is a python program for predicting mass spectrometry relevant chemical ionization efficiency. Two interacting deep neural network models are implemented for log ionization efficiency (logIE) value prediction and error attenuation; one sequential model (*i.e.*, model 1) predicts logIE while a second sequential model (*i.e.*, model 1) attempts to correct for residual logIE prediction error produced by model 1.
<br />
<br /><img align = "center" width="800" alt="image" src="https://github.com/mitkeng/efficION/assets/97419520/68bb2584-95dc-4f1b-85da-dafc5388521a">


#
### Functionality
The program supports single logIE query or batch chemical logIE query. For single query, either a canonical SMILE or chemical name is applicable, along with a required solution pH value; for batch quiery, the following csv file data format is required:
|| SMILES | pH|
|--| ------------- | ------------- |
|1| C1=CNC(=O)NC1=O| 7.2|
|n| ... | ...|

Currently, efficION is only appropriate for predicting logIE relating to the ESI ionization technique. 

#
### Performance

<img align = "left" width="400" alt="focus" src="https://github.com/mitkeng/efficION/assets/97419520/8f8bf4bc-e028-4cb7-9ba9-4897faf6da0f">
<img align = "center" width="400" alt="focus" src="https://github.com/mitkeng/efficION/assets/97419520/bb441331-f8c2-4f29-93a0-4a888476dffd)">

<br />


#
### Accessible
 [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">](https://colab.research.google.com/drive/1t9ki6sLRUjbidTl5rcPJr5BlZCi6TnFT?usp=sharing) <code style="color : grey">to access the efficION platform.</code>
<br />


#
### Reference
Liigand, J., Wang, T., Kellogg, J. et al. Quantification for non-targeted LC/MS screening without standard substances. Sci Rep 10, 5808 (2020). https://doi.org/10.1038/s41598-020-62573-z
