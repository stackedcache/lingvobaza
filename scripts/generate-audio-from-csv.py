import csv 
import os
import re
from gtts import gTTS
from pydub import AudioSegment

CSV_PATH = '../data/phrases.csv'
AUDIO_OUTPUT_DIR = '../audio/phrases'

# Function to sanitze file name of punctuation and symbols 
def sanitize_filename(phrase):
    words = phrase.lower().split()[:4]
    base = '_'.join(words)
    return re.sub(r'[^a-z0-9_]', '', base) # Remove all but letters, numbers, and underscores


# Function to slow down audio 
def slow_down(audio, factor=0.8):
    return audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * factor)
    }).set_frame_rate(audio.frame_rate)


with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# Check if files need to be generated 
to_generate = [row for row in rows if row['audio_generated'].strip().lower() == 'no']
if not to_generate:
    print("All files already generated!")
    exit()
else:
    count = len(to_generate)
    print(count, " Files to generate!")

for row in rows:
    if row['audio_generated'].strip().lower() == 'yes':
        continue # Skip generated files 
    
# Print and exit if all files are generated already 
    phrase_id = row['id']
    category = row['category']
    english = row['english_phrase']
    russian = row['russian_phrase']
    explanation = row['explanation']
    
    safe_base = sanitize_filename(english)
    filename = f"{phrase_id}_{safe_base}.mp3"
    category_path = os.path.join(AUDIO_OUTPUT_DIR, category)
    os.makedirs(category_path, exist_ok=True)
    output_path = os.path.join(category_path, filename)


# GENERATE AUDIO SEGMENTS 

    print(f"[+] Generating: {filename}")

    english_tts = gTTS(english, lang='en')
    russian_tts = gTTS(russian, lang='ru')
    explanation_tts = gTTS(explanation, lang='en') if explanation else None 

# Save Temp files 
    english_path = 'english_temp.mp3'
    russian_path = 'russian_temp.mp3'
    explanation_path = 'explanation_temp.mp3'

    english_tts.save(english_path)
    russian_tts.save(russian_path)
    if explanation_tts: 
        explanation_tts.save(explanation_path)

# LOAD AND PROCESS 
    english_audio = AudioSegment.from_file(english_path)
    russian_audio = AudioSegment.from_file(russian_path)
    russian_slow = slow_down(russian_audio)

    segments = [english_audio, russian_audio, russian_slow]
    if explanation_tts:
        explanation_audio = AudioSegment.from_file(explanation_path)
        segments.append(explanation_audio)

    final_audio = sum(segments)
    final_audio.export(output_path, format='mp3')


# Mark as generated is csv file 
    row['audio_generated'] = 'yes'

    for f in [english_path, russian_path, explanation_path if explanation else None]:
        if f and os.path.exists(f):
            os.remove(f)

with open (CSV_PATH, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Done generating new audio files")
