import praw
import argparse
import pandas as pd
import os
from tqdm import tqdm as tqdm
import urllib.request
import sys

parser = argparse.ArgumentParser(description='r/Fakeddit image downloader')

parser.add_argument('type', type=str, help='train or validate')
parser.add_argument('client_id', type=str, help='client_id')
parser.add_argument('client_secret', type=str, help='client_secret')
parser.add_argument('user_agent', type=str, help='user_agent')

args = parser.parse_args()


if (args.type != "train" and args.type != "validate" and args.type != "test"):
  print("type must be train or validate")
  sys.exit()

reddit = praw.Reddit(client_id=args.client_id,
                     client_secret=args.client_secret,
                     user_agent=args.user_agent)

df = pd.read_csv(args.type + ".tsv", sep="\t")

pbar = tqdm(total=len(df))

if not os.path.exists("images"):
  os.makedirs("images")

for index, row in df.iterrows():
  if row["hasImage"] == True:
    submission = reddit.submission(id=row["id"])

    # figure out resolution
    num_resolutions = len(submission.preview['images'][0]['resolutions'])
    if num_resolutions < 3:
        # download the best resolution
        image_url = submission.preview['images'][0]['resolutions'][num_resolutions-1]['url']
    else:
        # limit resolution to the 3rd best picture
        image_url = submission.preview['images'][0]['resolutions'][2]['url']
    urllib.request.urlretrieve(image_url, "images/" + row["id"] + ".jpg")
  pbar.update(1)
print("done")

