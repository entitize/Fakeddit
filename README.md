# Fakeddit

Kai Nakamura, Sharon Levy, and William Yang Wang. 2019. r/Fakeddit: A New Multimodal Benchmark Dataset for Fine-grained Fake News Detection
It's not a subreddit. It's named Fakeddit because Fake News + Reddit = Fakeddit

Paper: _

Our lab: http://nlp.cs.ucsb.edu/index.html

## Getting Started

Follow the instructions to download the dataset. You can download text, metadata, comment data, and image data.

Note that released test set is public. Private test set is used for leaderboard. 

Please let us know if you encounter any problems by opening an issue or by directly contacting us.

### Installation

#### Download text, metadata, and comments
Download the v1.0 dataset from [here](https://drive.google.com/open?id=1ZuCV2_jkUZCYPyCtOhijU7t4bIkYLk9V)

#### Download image data 

Follow the steps [here](https://github.com/reddit-archive/reddit/wiki/OAuth2) to obtain `client_id`, `client_secret`, and `user_agent`

Fork or clone this repository and install required python libraries

```
$ git clone https://github.com/entitize/Fakeddit
$ cd Fakeddit
$ pip install -r requirements.txt
```
Copy `image_downloader.py` to the same directory/folder as where you downloaded the tsv files. 

Run `image_downloader.py`  in the new directory/folder

```
$ python image_downloader.py file client_id client_secret user_agent
```

substitute `file` with either `train.tsv`, `validate.tsv`, or `test.tsv`

substitute `client_id`, `client_scret` and `user_agent` with your own values

Note that you must run the `image_downloader.py` script 3 times to download the entire public dataset

If you encounter an error, make sure the command line parameters you set don't have any `(` or `)` or any other funny characters

### Usage

`train.tsv`, `validate.tsv`, and `test.tsv` contain text and metadata for the training, validation, and public testing datasets respectively.

`comments.tsv` consists of comments made by Reddit users on submissions in the entire released dataset. Use the `submission_id` column to identify which submission the comment is associated with. Note that one submission can have zero, one, or multiple comments.