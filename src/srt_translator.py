from deep_translator import GoogleTranslator
from tqdm import tqdm
import pysrt
import os

class SrtTranslator:

    translator = GoogleTranslator(source="en", target="et")

    def translateFile(self, file_path, output_path, folder_path):
        files_subtitles = pysrt.open(file_path)

        for i in tqdm(range(len(files_subtitles))):
            translated_subtitle = SrtTranslator.translator.translate(files_subtitles[i].text)
            files_subtitles[i].text = translated_subtitle

        dir_name = os.path.dirname(folder_path)
        save_folder = os.path.join(dir_name, output_path)
        dirs = os.listdir(dir_name)
        if not output_path in dirs:
            os.mkdir(save_folder)

        file_name = "[EST]" + os.path.basename(file_path)
        save_path = os.path.join(save_folder, file_name)

        files_subtitles.save(save_path)

    def translateFolder(self, folder_path, output_path):
        file_names = os.listdir(folder_path)

        for i in tqdm(range(len(file_names))):
            file_name = file_names[i]
            file_path = os.path.join(folder_path, file_name)
            self.translateFile(file_path, output_path, folder_path)