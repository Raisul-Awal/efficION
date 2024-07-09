## efficION

### Introduction 
efficION is a python program for predicting mass spectrometry relevant chemical ionization efficiency. Two interacting deep neural network models are implemented for log ionization efficiency (logIE) value prediction and error attenuation; one sequential model (*i.e.*, model 1) predicts logIE while a second sequential model (*i.e.*, model 1) attempts to correct for residual logIE prediction error produced by model 1.

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
### Requirements


