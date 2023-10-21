from srt_translator import SrtTranslator

# Use these to define what language you are translating from and to.
EST = "et"
ENGLISH = "en"
UKRAINIAN = "uk"
RUSSIAN = "ru"

# Add the output and input folder so the translator can find the place
# where the .srt files are and where to put the translaited versions.
INPUT_FOLDER_PATH = ""
OUTPUT_FOLDER_PATH = ""

def main():
    # Change the language here
    srtt = SrtTranslator(
        source_language=ENGLISH,
        target_language=UKRAINIAN
    )
    srtt.translateFolder(INPUT_FOLDER_PATH, OUTPUT_FOLDER_PATH)

if __name__ == '__main__':
    # When the languages are set and the output and input are added then run the code!
    main()