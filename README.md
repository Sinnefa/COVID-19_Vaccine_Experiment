# COVID-19 Vaccine Experiment

Through a computational analysis it seems like Foot-And-Mouth vaccines might represent a starting point to create a vaccine against the coronavirus COVID-19.

# Abstract
Vaccines act recognizing pathogens. http://www.violinet.org/index.php is a website which archives vaccines and their targets. By scanning the sequence of all pathogens for each vaccine one can associate vaccines with their recognized targets. Building a TSV file containing these associations and adding COVID-19 one can compare all vaccines and find which one recognises sequences similar to those of COVID-19 published here: https://www.ncbi.nlm.nih.gov/nuccore/MN908947. Furthermore SWISS-MODEL published the 3d structure which might further aid targeting this virus (https://swissmodel.expasy.org/repository/species/2697049). This analysis shows that FMDV (Foot-And-Mouth Virus) vaccine might worth further investigations.

# Results
The two vaccines which reported a significant z-score are:
* FMDV DNA Vaccine encoding P1 and non-structural proteins 2A, 3C, and 3D et. similia http://www.violinet.org/vaxquery/query_detail.php?c_pathogen_id=206#Vaccine_Information
* Feline infectiour peritonitis virus 3abc mutant vaccine et. similia
See complete list **vaccines-human.tsv**

It is interesting to notice that the two viruses, despite belonging to two distinct families, are both RNA viruses and sperical.

Aligning proteins (BLOSUM62, open: 10, extend: 1) it seems like Foot-And-Mouth vaccines might partially recognize two COVID-19 proteins. In particular, the COVID-19 envelop protein:
* https://www.ncbi.nlm.nih.gov/protein/QHD43418.1 which seems similar to https://www.ncbi.nlm.nih.gov/protein/NP_740466.1?report=genpept.
* https://www.ncbi.nlm.nih.gov/protein/QHD43419.1 which seems similar to https://www.ncbi.nlm.nih.gov/protein/NP_740461.1?report=genpept

Plus the following:
* https://www.ncbi.nlm.nih.gov/protein/1798172433 which seems similar to https://www.ncbi.nlm.nih.gov/protein/CAC22182.2

Rows are COVID-19 proteins
Columns are Vaccineice FMDV target Pathoges as reported in VIOLIN.

||||||||||
|--- |--- |--- |--- |--- |--- |--- |--- |--- |
||ABR13034.1|**CAC22182.2**|CAC34727.1|**NP_740461.1**|**NP_740466.1**|NP_740467.1|AAT01695.1|AAK97050.1|
|QHD43415.1|22.14%|36.84%|21.31%|66.67%|43.48%|32.61%|23.33%|27.72%|
|QHD43416.1|35.71%|34.78%|40.00%|57.14%|50.00%|23.68%|31.82%|34.09%|
|QHD43417.1|27.08%|35.71%|20.97%|37.50%|29.41%|46.15%|24.29%|24.29%|
|**QHD43418.1**|46.15%|33.33%|37.50%|37.50%|**75.00%**|40.00%|33.33%|33.33%|
|**QHD43419.1**|33.33%|33.33%|31.58%|**60.00%**|26.09%|50.00%|26.09%|25.00%|
|QHD43420.1|45.45%|40.00%|57.14%|18.75%|28.57%|42.86%|18.97%|36.36%|
|QHD43421.1|40.00%|28.57%|30.43%|42.86%|33.33%|25.00%|20.63%|20.34%|
|QHD43422.1|31.25%|45.45%|28.57%|42.86%|38.10%|31.25%|38.10%|35.14%|
|QHD43423.2|43.75%|46.15%|31.34%|30.77%|38.46%|22.81%|22.81%|22.29%|
|**QHI42199.1**|60.00%|**75.00%**|31.25%|50.00%|37.50%|66.67%|40.00%|27.78%|

# Methods
I downloaded all elements containing the word "Virus" from http://www.violinet.org/violinml/index.php for each one of them I collected all the pathogens sequences. Secondly, I transformed these sequences in 3-grams with a sliding-window strateg. Each vaccine followed by its 3-grams is a row in a PAndas DataFrame which is then used to compute cosine similarity against COVID-19 - also broken down in 3-grams. This step allowed a ranking (see **vaccines-human.tsv**) by similairty which highlighted which vaccine was potentially able to recognize COVID-19 sequences.

Finally, I aligned protein sequences and derived similarities against Foot-And-Moth Virus, which seemed to be the most similar with a z-score >2

# Attached data
In this repository, other than the source code, you can find two file
1) **vaccines-human.tsv** which contains a ranked list of vaccines containing the word "Human" with cosine similarity and z-score
2) **vaccines.tsv** which contains a ranked list of vaccines for any organism with cosine similarity and z-score
3) **COVID-19.zip** which contains all fast from COVID-19 https://www.ncbi.nlm.nih.gov/nuccore/MN908947
4) **FMDV.zip** which contains all Foot-And-Mouth proteins reported in http://www.violinet.org/vaxquery/query_detail.php?c_pathogen_id=206
5) **vaccines-virus-sequence-human.tsv** a file containing Vaccines (Human), Virus name and sequences
6) **vaccines-virus-sequence.tsv** a file containing Vaccines, Virus name and sequences

# Conclusion
Despite being a preliminary experiment this analysis can be inspirational to experiment known vaccines againt unknown viruses.

# Contacts
Alberto Calderone, Ph.D. - sinnefa@gmail.com
