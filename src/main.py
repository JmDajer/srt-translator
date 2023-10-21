from srt_translator import SrtTranslator

EST = "et"
ENGLISH = "en"
UKRAINIAN = "uk"

# Add the output and input folder so the translator can find the place
# where the .srt files are and where to put the translaited versions.
INPUT_FOLDER_PATH = ""
OUTPUT_FOLDER_PATH = ""

def main():
    srtt = SrtTranslator()
    srtt.translateFolder(INPUT_FOLDER_PATH, OUTPUT_FOLDER_PATH)

if __name__ == '__main__':
    main()