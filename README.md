
# Fakeddit

Kai Nakamura, Sharon Levy, and William Yang Wang. 2019. Fakeddit: novel large multimodal fine-grained dataset for automatic fake news detection.
It's not a subreddit. It's named Fakeddit because Fake News + Reddit = Fakeddit

Paper: _

Our lab: http://nlp.cs.ucsb.edu/index.html

## Getting Started

Follow the instructions to download the dataset. You can download text, metadata, comment data, and image data

Note that released test set is public. Private test set is used for leaderboard. 

### Prerequisites
script tested on python 3.5

Follow the steps [here](https://github.com/reddit-archive/reddit/wiki/OAuth2) to obtain `client_id`, `client_secret`, and `user_agent`

### Installing

Download text, comment, and metadata
```
$ git clone https://github.com/entitize/Fakeddit.git
```

Download image data

Install required python libraries

```
$ pip install -r requirements.txt
```

Run image downloader

```
$ python image_downloader.py type client_id client_secret user_agent
```

substitute `type` with either `train`, `validate`, or `test`

substitute `client_id`, `client_scret` and `user_agent` with your own values

If you encounter an error, make sure the command line parameters you set don't have any `(` or `)` or any other funny characters

### Usage

`train.tsv`, `validate.tsv`, and `test.tsv` contain text and metadata for the training, validation, and public testing datasets respectively.

`comments.tsv` consists of comments made by Reddit users on submissions in the entire released dataset. Use the `submission_id` column to identify which submission the comment is associated with. Note that one submission can have zero, one, or multiple comments.



