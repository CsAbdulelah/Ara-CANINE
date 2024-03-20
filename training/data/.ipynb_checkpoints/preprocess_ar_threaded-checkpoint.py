import argparse
import re
from arabert.preprocess import ArabertPreprocessor
import nltk
import multiprocessing
from tqdm import tqdm

model_name = "aubmindlab/bert-base-arabertv02"
arabert_prep = ArabertPreprocessor(model_name=model_name, apply_farasa_segmentation=False)
min_text_length = 10
max_text_length = 2048

def filter_text(text):
    # Filter out text containing equations
    if "\displaystyle" in text:
        return False
    return True

def preprocess_lines(line):
    processed_lines = []
    if line:
        sentences = nltk.sent_tokenize(line)
        for sentence in sentences:
            sentence = sentence.strip()
            sentence = arabert_prep.preprocess(sentence)
            if min_text_length <= len(sentence) <= max_text_length and filter_text(sentence):
                processed_lines.append(sentence)
    return processed_lines

def process_line(line):
    return preprocess_lines(line)

def main(args):
    with open(args.input_file, "r") as input_file, open(args.output_file, "w") as output_file:
        lines = input_file.readlines()

        # Create a multiprocessing pool
        with multiprocessing.Pool(7) as pool:
            processed_lines = []

            # Map the process_line function to the input lines using the pool with tqdm
            with tqdm(total=len(lines), desc="Processing") as pbar:
                for result in pool.imap_unordered(process_line, lines):
                    processed_lines.extend(result)
                    pbar.update()

            # Write the processed lines to the output file
            output_file.write('\n'.join(processed_lines))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, required=True)
    parser.add_argument("--output_file", type=str, required=True)
    args = parser.parse_args()
    main(args)
