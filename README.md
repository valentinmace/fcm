
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

- 2- The second one is used to convert a corpus from a Semeval 2010 format to a format usable by the FCM


## Installation

This repository is for Windows use, a linux version might come in a near future and it should be relatively easy to make it yourself

For both scripts, no installation is needed, you just need python 3, however make sure to have gzip installed if you wish to use the converting script (2nd one)


## Usage



## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

* 0.2.1
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Remove `setDefaultXYZ()`
    * ADD: Add `init()`
* 0.1.1
    * FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!)
* 0.1.0
    * The first proper release
    * CHANGE: Rename `foo()` to `bar()`
* 0.0.1
    * Work in progress

## Meta

Macé Valentin – [LinkedIn](https://www.linkedin.com/in/valentin-mac%C3%A9-310683165/) – valentin.mace@kedgebs.com

Distributed under the MIT license. See ``LICENSE`` for more information.
