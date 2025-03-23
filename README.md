# LINGVOBAZA - The Language Base

Lingvobaza is a system I created to generate audio files using Google's text to speech python library.

The `/scripts/generate-audio-from-csv.py` script reads the csv file in `/data/phrases.csv` and generates corresponding audio files.

The CSV has the following layout: 

| id | category | english_phrase | russian_phrase | explanation_ru | explanation_en | audio_generated |
|----|----------|----------------|----------------|----------------|----------------|-----------------|
| 1 | directions | You can find him under the tree. | Его можно найти под деревом. | Под... Под… Под | This is the word for under (this is a preposition) | yes/no |

- The script reads the csv and checks if the `audio_generated` field is marked yes or no. 
    - Fields marked yes are skipped and not regenerated.
    - This allows phrases to be added over time. 

- For each phrase that is not generated, a subdirectory based on category is created, and the first four words of 
the english phrase are used as the filename. 

- The resulting audio file reads the English phrase, then the Russian phrase, then the Russian explanation, and then English explanation. 

## USING THE SYSTEM 

- Simply clone the repository or set up the file structure, populate your CSV as described above, and run the `generate-audio-from-csv.py` script.
- Then you can use the audio player of your choice to listen to the files. 
    - I am using ffplay on Debian to play files from the cli


## FUTURE IMPROVEMENTS 

- Possibly to build a front end audio player to listen from the web on any device.
- Possibly to build a `play_all` script to loop through all files in the audio directories
- Possibly to add a `shuffle` feature to either web front end or playthrough scripts


## Comments and suggestions

- Please reach out on Github or [Substack](https://stackedcache.substack.com/) with any ideas or improvements
