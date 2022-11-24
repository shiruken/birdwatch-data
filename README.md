[![Update Data](https://github.com/shiruken/birdwatch-data/actions/workflows/main.yml/badge.svg)](https://github.com/shiruken/birdwatch-data/actions/workflows/main.yml)

# Birdwatch Data

Automated scraping of [Birdwatch](https://twitter.github.io/communitynotes/) data using GitHub Actions. Downloads the [daily data releases](https://twitter.com/i/communitynotes/download-data) from Twitter, runs the Birdwatch algorithm to score notes and users, and commits changes to the repository. Published to https://birdwatch.csullender.com/.

## Available Files

* [Notes](https://birdwatch.csullender.com/notes-00000.tsv)
* [Ratings](https://birdwatch.csullender.com/ratings-00000.tsv)
* [Note Status History](https://birdwatch.csullender.com/noteStatusHistory-00000.tsv)
* [Scored Notes](https://birdwatch.csullender.com/scoredNotes.tsv)*
* [Scored Authors](https://birdwatch.csullender.com/helpfulnessScores.tsv)*

\* Generated by scoring algorithm
