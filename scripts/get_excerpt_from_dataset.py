import pandas as pd

def get_excerpt_from_dataset(src_dir, dataset, row_num):
    '''
    Given a dataset of story excerpt conditions and start and ends and a row number, 
    gets the story text from the stories in src_dir at the specific row number
    '''
    id = dataset['id'][row_num]
    start = dataset['start'][row_num]
    end = dataset['end'][row_num]
    story_file = open(src_dir + id + '.txt')
    story = story_file.read()
    story_file.close()
    return story[start:end]

if __name__ == '__main__':
    # example how-to-use, getting first four rows of the dataset
    database = '../data/retouched_texts/'
    dataset_fn = '../data/labeled_csv_dataset.csv'
    df = pd.read_csv(dataset_fn)
    print(get_excerpt_from_dataset(database, df, 0))
    print(get_excerpt_from_dataset(database, df, 1))
    print(get_excerpt_from_dataset(database, df, 2))
    print(get_excerpt_from_dataset(database, df, 3))
