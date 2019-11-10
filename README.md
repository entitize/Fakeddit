
# Fakeddit

Kai Nakamura, Sharon Levy, and William Yang Wang. 2019. Fakeddit: novel large multimodal fine-grained dataset for automatic fake news detection.
It's not a subreddit. It's named Fakeddit because Fake News + Reddit = Fakeddit

Paper: _

Our lab: http://nlp.cs.ucsb.edu/index.html

## Getting Started

Follow the instructions to download the dataset. You can download text, metadata, and image data. 

### Prerequisites
script tested on python 3.5

Follow the steps [here](https://github.com/reddit-archive/reddit/wiki/OAuth2) to obtain `client_id`, `client_secret`, and `user_agent`

### Installing

Download text and metadata
```
$ git clone https://github.com/entitize/Fakeddit.git
```

Download image data
Install required python libraries

```
$ pip install -r /path/to/requirements.txt
```

Run image downloader

```
$ python image_downloader.py type client_id client_secret user_agent
```

substitute `type` with either `train` or `validate`
substitute `client_id`, `client_scret` and `user_agent` with your own values

If you encounter an error, make sure the command line parameters you set don't have any `(` or `)` or any other funny characters