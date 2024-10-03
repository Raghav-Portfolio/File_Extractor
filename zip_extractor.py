import zipfile

def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)
        
if __name__=='__main__':
    extract_archive(archive_path='C:/Users/1000490/Desktop/Python/Bonus_Examples/extractor/compressed.zip', dest_dir='C:/Users/1000490/Desktop/Python/Bonus_Examples/extractor')