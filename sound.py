import pydub
from pydub import AudioSegment

# Specify the input and output filenames
input_file = "sample.m4a"
output_file = "sample.mp3"

# Read the m4a file
try:
  sound = AudioSegment.from_file(input_file, format="m4a")
except FileNotFoundError:
  print(f"Error: Input file '{input_file}' not found.")
  exit()

# Export the sound as MP3
try:
  sound.export(output_file, format="mp3")
  print(f"Successfully converted '{input_file}' to '{output_file}'.")
except Exception as e:
  print(f"Error during conversion: {e}")


