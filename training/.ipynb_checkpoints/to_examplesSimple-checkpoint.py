import argparse
import pandas as pd
from tqdm import tqdm

from shiba import CodepointTokenizer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_data', required=True)
    parser.add_argument('--output_data', required=True)
    parser.add_argument('--max_length', type=int, default=2048, help='Max length in tokens, including [CLS] and [SEP] tokens')

    args = parser.parse_args()

    infile = open(args.input_data)
    tokenizer = CodepointTokenizer()

    data = []
    above2048 = 0
    for line in tqdm(infile):
        line_text = line.strip()

        if len(line_text) <= args.max_length:
            encoded_example = tokenizer.encode([line_text])
            assert len(encoded_example['input_ids']) <= args.max_length

            data.append({'input_ids': encoded_example['input_ids'].tolist()})
        else:
            above2048+=1

    infile.close()
    print(above2048)
    # Create a Pandas DataFrame from the processed data
    df = pd.DataFrame(data)

    # Write the DataFrame to a Parquet file
    df.to_parquet(args.output_data, index=False)

if __name__ == '__main__':
    main()
