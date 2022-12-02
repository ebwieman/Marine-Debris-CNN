import pandas as pd

training_with_repeats = "data/dar2015v7-1_640x640_8class_train.csv"
training_without_repeats = "data/dar2015v7-1_640x640_8class_train_no_repeats.csv"


def process_training_data(input, output):
    """Edit initial training data to only include one example per image"""
    df = pd.read_csv(training_with_repeats, sep=",")
    df.drop_duplicates(subset=['filename'], inplace=True)

    df.to_csv(training_without_repeats, index=False)


if __name__ == "__main__":
    process_training_data(training_with_repeats, training_without_repeats)