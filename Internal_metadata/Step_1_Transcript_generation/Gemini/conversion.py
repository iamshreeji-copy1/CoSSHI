# Configuration
TTS_name = "TTS_name"
Vocoder_name = "Vocoder_name"
gender_of_speaker = "gender_of_speaker"
name_of_speaker = "name_of_speaker"
accent = "accent"

# Input and Output Files
input_file = "/Users/nisarg/Desktop/LLM_Deepfake_Dataset/Internal_metadata/Step_1_Transcript_generation/Gemini/t.txt"
output_file = "/Users/nisarg/Desktop/LLM_Deepfake_Dataset/Internal_metadata/Step_1_Transcript_generation/Gemini/output.txt"


# Processing
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for idx, line in enumerate(infile, start=1):
        line = line.strip()
        if line:  # Skip empty lines
            prefix = f"GPro2.5_{TTS_name}_{Vocoder_name}_{gender_of_speaker}_{name_of_speaker}_{accent}_{idx} | "
            outfile.write(prefix + line + '\n')
