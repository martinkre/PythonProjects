# Simplest Mandarin Trainer
just read what you want to read and learn the characters.
You can convert .txt to .csv with the converter and save them in designated file paths.

Requirements:

    Python Runtime
    
        Pandas

Example:

    python -m convert input_file output_file

    python -m convert input/numbers.txt data/numbers.csv

You can run the main.py with the following commands:

    python -m main numbers  -- shows the numbers from 1 to 20 and from 20 to 100 in increments of 10. After that in increments of 100 to 1000

    python -m main top100 -- shows the top 100 most used characters. It's not perfect, there are duplicates. I got it from ChatGPT, thanks, bro.