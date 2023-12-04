import random
import os
import pandas as pd
import re

def generate_sample(story, length=0, at_beginning=False):
    '''
    Given a story, takes a sample from the story either at the beginning or
    somewhere in the middle of a given length

    story: str
    length: int, corresponding to condition
        - 0 = control, min of story length or 500 words
        - 1 = one sentence
        - 2 = min of 3 sentences or 80 words
        - 3 = first paragraph break after 150 words
    at_beginning: bool, corresponds to location of sample in story
        - True = samples from the beginning
        - False = randomly begins sample somewhere in the middle half
    '''
    punctuation = '!.?'
    sentence = f'[^{punctuation}]*[{punctuation}]'
    if at_beginning:
        sample_start = 0
    else:
        sample_start = random.randint(len(story)//4, 3*len(story)//4)
        # makes sample start at the beginning of a sentence
        while story[sample_start-2] not in punctuation and sample_start > 0:
            sample_start -= 1

    # control
    if length == 0:
        return ' '.join(story[sample_start:].split(' ')[:500]), sample_start

    # one sentence
    if length == 1:
        return re.search(sentence, story[sample_start:]).group(0), sample_start

    # min of 3 sentences or 80 words
    if length == 2:
        sentences = (re.search(sentence*3, story[sample_start:]) or 
                     re.search('.*', story[sample_start:])).group(0)
        words = sentences.split(' ')
        if len(words) > 80:
            return ' '.join(words[:80]), sample_start
        return sentences, sample_start

    # first paragraph break after 150 words
    if length == 3:
        # find the first paragraph break nearby to start
        end = sample_start + len(' '.join(story[sample_start:].split(' ')[:150]))
        while end < len(story) and (story[end-1] not in punctuation or story[end] != '\n'):
            end += 1
        return story[sample_start: end], sample_start

def generate_dataset(database, rank_file, data_dir):
    '''
    Given a database of stories, generates dataset of story samples in
    experimental conditions

    database: directory of stories

    conditions:
    - location: 1x beginning, 3x random sample from middle
    - length: 1 sentence, 3 sentences, 1 paragraph, control

    return: .pdpkl database
    '''
    locations = ['beginning', 'middle', 'middle', 'middle']
    lengths = ['control', 'one_sentence', 'few_sentences', 'paragraph']
    id_to_rank = get_ranks(rank_file)

    rows = []
    count = 0
    for story_filename in os.listdir(database):
        story_id = story_filename.split('.txt')[0]
        story_file = open(database + story_filename, 'r')
        story = story_file.read()
        if story_id in id_to_rank:
            for loc in locations:
                for i, length in enumerate(lengths):
                    row = {}
                    story_sample, loc_s =  generate_sample(story, i, loc == 'beginning')
                    row['id'] = story_id
                    row['location_str'] = loc
                    row['location'] = int(loc == 'beginning')
                    row['length_str'] = length
                    row['length'] = i
                    row['start'] = loc_s
                    row['end'] = loc_s + len(story_sample)
                    row['label'] = id_to_rank[story_id]
                    rows.append(row)
            count += 1
        story_file.close()
    print(count)
    print(pd.DataFrame(rows).head())
    pd.to_pickle(pd.DataFrame(rows), data_dir + 'labeled_dataset.pdpkl')
    pd.DataFrame(rows).to_csv(data_dir + 'labeled_csv_dataset.csv')

def get_ranks(rank_file):
    '''Given a file with story ranks, gets the bottom/middle/top rankings
    ranking of 1 means top, 0 means middle, -1 means bottom'''
    id_to_rank = {}
    rankings_df = pd.read_csv(rank_file)
    rankings = sorted(rankings_df['final'])
    top_cutoff = rankings[len(rankings)//4]
    bottom_cutoff = rankings[3*len(rankings)//4]
    for id, ranking in zip(rankings_df['docId'], rankings_df['final']):
        id_to_rank[id] = 1 if ranking <= top_cutoff else 0 if ranking <= bottom_cutoff else -1
    return id_to_rank

# do we want all conditions per story? yes
# all conds in 1 row or each cond in own row? whatever i want
# for paragraph cond do we want to start at the beginning of paragraph? yes
# for above it did not work because stories don't have clear paragraph breaks,
# so just did sentences

if __name__ == '__main__':
    rank_file = '../data/story_ranks.csv'
    database = '../data/retouched_texts/'
    data_dir = '../data/'
    generate_dataset(database, rank_file, data_dir)
