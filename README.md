# dga-isot

Project Title: Detecting Broad Length Algorithmically Generated Domains
The project aims to implement feature extraction of algorithmically generated domain names using concepts of Information theory.We measure the amount of information conveyed by the domain by analyzing character n-grams and computing the corresponding entropy. At the same, we leverage basic lexical and linguistic characteristics of the domain names which have proven effective at detecting DGAs.

Getting Started
Prereq: Python , weka 3.8

Running
feature_extraction.py can be run to extract features such as length,vowels,consonants and entropy
conditional_probability.py involves splitting the domains into trigrams and calculating the individual probability of ocurrences.

Machine learning using Weka :

-	J48 decision tree
-	Random Forests algorithm
