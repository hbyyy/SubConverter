import os
import re


class Converter:
    def __init__(self, filepath, convert_to):
        self.filepath = filepath
        self.convert_to = convert_to
        self.contents = []
        self.filename = ''
        self.extension = ''
        self.converted_contents = ''

        self.file = self._load_file()
        self._load_contents()

    def _load_file(self):
        name, ext = os.path.splitext(self.filepath)
        self.filename = os.path.basename(name)
        self.extension = ext
        if ext == '.srt':
            self.convert_to = '.sbv'
        else:
            self.convert_to = '.srt'
        file = open(self.filepath, 'r')
        return file

    def _load_contents(self):
        file = self._load_file()
        raw_contents = file.read()
        file.close()
        self.contents = raw_contents.split('\n\n')

    def _convert_block_srt_to_sbv(self, block):
        result = re.sub('([0-9][0-9]:[0-9][0-9]:[0-9][0-9]),([0-9][0-9][0-9])', '\\1.\\2', block, count=2)
        result = re.sub('^[0-9]+\n', '', result, count=1)
        result = re.sub(' --> ', ',', result, count=1)
        return result

    def _convert_srt_to_sbv(self):
        convert = list(map(self._convert_block_srt_to_sbv, self.contents))
        self.converted_contents = '\n\n'.join(convert)

    def convert(self, converted_file_name, converted_file_path=None):
        self._convert_srt_to_sbv()
        if converted_file_path:
            save_path = f'{converted_file_path}/{converted_file_name}{self.convert_to}'
        else:
            save_path = f'{converted_file_name}{self.convert_to}'

        with open(save_path, 'w') as f:
            f.write(self.converted_contents)
