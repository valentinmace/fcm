
# Fcm
>The Fcm is a compositional embedding model for relation classification combining unlexicalized linguistic context
and word embeddings

>Fcm paper (Gormley et al. 2015): http://www.cs.cmu.edu/~mgormley/papers/gormley+yu+dredze.emnlp.2015.pdf

<p align="center">
  <img src="./data/corpus/raw_to_formated_script/notebook/img/fcm_nn.png"
       width="400" height="260">
</p>

The main purpose of this repository is to run the FCM for the relation classification task on several corpus, using multiples word embeddings and to compute results (such as micro-f1, macro-f1, weighted-f1 etc.)

This repository is made of multiple pieces, the heart being the FCM C++ implementation by Mo Yu from: https://github.com/Gorov/FCM_nips_workshop

I have build two python scripts around it:

- 1- The first (main) one is used to run the FCM on a chosen corpus, tuning learning rate and number of epochs, using one or many word embeddings and finally getting results in a file

- 2- The second one is used to convert a corpus from a Semeval 2010 format to a format usable by the FCM, if you ever wish to use my work on another corpus and if you can easily have your corpus in a Semeval 2010 format ..

I already provide Semeval 2010, Semeval 2018 and reAce 2005 corpus with all results using several word embeddings (see ``results/macro_f1`` folder)

## Installation

This repository is for Windows use, a linux version might come in a near future and it should be relatively easy to make it yourself

For both scripts, no installation is needed, you just need python 3, however make sure to have gzip installed if you wish to use the converting script (2nd one)


## Usage main script

Clone or download the repository

Open a terminal in the ``fcm_global.py`` folder and execute:
```sh
python fcm_global.py <train data> <test_data> <epochs> <learning rate> [word embeddings]
```
Example:
```sh
python fcm_global.py python fcm_global.py semeval2018_train semeval2018_test 30 0.005
```
Notes:
- If you do not write a word embedding argument, it will run on every word embeddings available in the ``data/word_emb`` folder
- Train data and test data files have to be in the ``data/corpus/formated folder``
- In this repo I only provide one small word embeddings (github size restriction) but you can get bigger and better performing on my drive at https://drive.google.com/drive/folders/18KrHhJcpOouFEf1Dgqw8N6Hpg6gxEZjH

## Meta

Macé Valentin – [LinkedIn](https://www.linkedin.com/in/valentin-mac%C3%A9-310683165/) – valentin.mace@kedgebs.com

Distributed under the MIT license. See ``LICENSE`` for more information.
