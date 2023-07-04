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


## Update:
you can now pass startup arguments and choose between gui or cli. This update was to learn how to implement startup arguments for future projects.

Usage:

    python -m main cli numbers -- starts the program in the terminal and puts out the numbers table (you can choose numbers, top100 or weekdays)

    python -m main gui -- starts the program wuth the Graphical User Interface (in development)
