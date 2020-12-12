from src.converter import Converter

if __name__ == '__main__':
    converter = Converter('../testsubfiles/testsub.srt', convert_to='sbv')
    converter.convert(converted_file_name='converttestfile', converted_file_path='..')
