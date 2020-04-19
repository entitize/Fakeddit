# Fakeddit

Kai Nakamura, Sharon Levy, and William Yang Wang. 2020. r/Fakeddit: A New Multimodal Benchmark Dataset for Fine-grained Fake News Detection

Paper: https://arxiv.org/abs/1911.03854

Our lab: http://nlp.cs.ucsb.edu/index.html

## Getting Started

Follow the instructions to download the dataset. You can download text, metadata, comment data, and image data.

Note that released test set is public. Private test set is used for leaderboard (coming soon).

Please read the `Usage` section. It is important.  

Please let us know if you encounter any problems by opening an issue or by directly contacting us.

### Installation

#### Download text, metadata, and comments
Download the v2.0 dataset from [here](https://drive.google.com/drive/folders/1DQSGFSLOP22xhL-Px4tFpde3eYpCq7bQ?usp=sharing)

Download the comment data from [here](https://drive.google.com/file/d/14iroKftRkRxF9LCinZVaKxHnwScbUfKb/view?usp=sharing)

#### Download image data 

The `*.tsv` dataset files have an `image_url` column which contain the image urls. 

For convenience, we have provided a script which will download the images for you. Please follow the instructions if you would like to use the attached script.

Fork or clone this repository and install required python libraries

```
$ git clone https://github.com/entitize/Fakeddit
$ cd Fakeddit
$ pip install -r requirements.txt
```
Copy `image_downloader.py` to the same directory/folder as where you downloaded the tsv files. 

Run `image_downloader.py`  in the new directory/folder

```
$ python image_downloader.py file
```

substitute `file` with either `train.tsv`, `validate.tsv`, or `test.tsv`

Note that you must run the `image_downloader.py` script 3 times to download the entire public dataset

### Usage

Please ignore the first four columns in the `.tsv` files. 

`train.tsv`, `validate.tsv`, and `test.tsv` contain text and metadata for the training, validation, and public testing datasets respectively.

If there are `Unnamed`... columns, you can ignore or get rid of them. Use the `clean_title` column to get filtered text data. 

`comments.tsv` consists of comments made by Reddit users on submissions in the entire released dataset. Use the `submission_id` column to identify which submission the comment is associated with. Note that one submission can have zero, one, or multiple comments.

Note: In our paper, only samples that have both image and text were used for the baseline experiments and error analysis.