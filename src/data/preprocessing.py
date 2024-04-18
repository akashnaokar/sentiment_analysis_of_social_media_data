import pandas as pd
import matplotlib as plt
import os
import string
import re
# pd.options.display.max_colwidth = 150

def preprocessdata(cfg):
    data_dir = cfg.paths.data_dir
    raw_data_dir= cfg.paths.raw_data_dir
    processed_data_dir = cfg.paths.processed_data_dir

    raw_data = cfg.files.raw_data_file
    processed_data = cfg.files.processed_data_file
    cleaned_data = cfg.files.cleaned_data

    file = os.path.join(raw_data_dir, raw_data)

    # Read file as a dataframe and drop unnecessary columns
    df = read_and_drop_csv(file)

    # Replace the NaN with 'na'
    handle_missing_values(df)

    # remove URLs, special characters, emoticons, and convert to lower case
    df.gender = df.gender.apply(clean_data)
    df.description = df.description.apply(clean_data)
    df.text = df.text.apply(clean_data)

    write_csv(df, processed_data_dir, processed_data)


#----------------------------#------------------------------------#----------------------------------#


def read_and_drop_csv(path):

    dataframe = pd.read_csv(path, encoding='latin_1')
    
    dataframe.drop(columns=['_unit_id', '_golden', '_unit_state', '_trusted_judgments',
                            '_last_judgment_at',  'profile_yn', 'gender:confidence',
                            'profile_yn:confidence', 'created', 'fav_number', 'retweet_count', 'tweet_created',
                            'gender_gold', 'link_color', 'name', 'profile_yn_gold', 'profileimage',
                            'sidebar_color', 'tweet_coord', 'tweet_count', 'tweet_id', 'tweet_location', 'user_timezone'], inplace=True)

    return dataframe

def handle_missing_values(dataframe):
    return dataframe.fillna('NA', inplace=True)

def clean_data(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)

    # Remove special characters
    text = re.sub(r'[^A-Za-z0-9\s]+', '', text)

    # Remove punctuations
    for char in string.punctuation:
        text = text.replace(char, '')

    emoj = re.compile("["
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    u"\U00002500-\U00002BEF"  # chinese char
    u"\U00002702-\U000027B0"
    u"\U000024C2-\U0001F251"
    u"\U0001f926-\U0001f937"
    u"\U00010000-\U0010ffff"
    u"\u2640-\u2642" 
    u"\u2600-\u2B55"
    u"\u200d"
    u"\u23cf"
    u"\u23e9"
    u"\u231a"
    u"\ufe0f"  # dingbats
    u"\u3030"
                    "]+", re.UNICODE)
    
    text = re.sub(emoj, '', text)

    text = text.lower()

    return text

    
def write_csv(df, output_path, file_name, overwrite=False):
    if not os.path.exists(os.path.join(output_path, file_name)) or overwrite:
        df.to_csv(os.path.join(output_path, file_name), index=True)
        print('File written')
    else:
        overwrite_confirmation = input('File already exists. Do you want to overwrite it? (y/n): ')
        if overwrite_confirmation.lower() == 'y':
            df.to_csv(os.path.join(output_path, file_name), index=True)
            print('File overwritten')
        else:
            print('File not overwritten')


