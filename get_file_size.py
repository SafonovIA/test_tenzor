import os
import time

# Путь до папки, куда загружается файл
path = 'C:\\path\\to\\Downloads'


# Получить все файлы в заданной папке отсортированные по времени
def get_files(folder_path=path):
    """
    folder_path - Путь до папки с загрузками
    """

    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
        ]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
    return files


# Ожидание загрузки новго файла
def wait_for_dowload(timeout=10):
    """
    timeout - Время ожидания
    """

    start_time = time.time()

    while time.time() - start_time < timeout:
        files = get_files()
        extension_file = files[-1].split(".")[-1]
        if extension_file != "crdownload" and extension_file != "tmp":
            return True
        time.sleep(1)

    print('Время ожидания истекло')
    return False


# Получение размера последнего файла
def get_size():
    file = get_files()[-1]
    size = os.path.getsize(f"{path}\\{file}")
    return size // (1024 * 1024)
