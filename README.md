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

- The first (main) one is used to run the FCM on a chosen corpus, tuning learning rate and number of epochs, using one or many word embeddings and finally getting results in a file
- The second one is used to convert a corpus from a Semeval 2010 format to a format usable by the FCM

![](header.png)

## Installation

OS X & Linux:

```sh
npm install my-crazy-module --save
```

Windows:

```sh
edit autoexec.bat
```

## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

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

Your Name – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
