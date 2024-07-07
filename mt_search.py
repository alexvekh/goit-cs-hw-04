from threading import Thread, Lock
import logging
import os
from time import time, sleep, ctime
import time

def search_in_files(file_list, keywords, results, lock):
    logging.debug(f"searching in: {file_list} ...")
    local_results = {keyword: [] for keyword in keywords}
    for file in file_list:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                for keyword in keywords:
                    if keyword in content:
                        local_results[keyword].append(file)
        except Exception as e:
            print(f"Error processing file {file}: {e}")
    logging.debug(f"... tread result: {local_results}")
    
    with lock:
        for keyword, files in local_results.items():
            results[keyword].extend(files)

def multithreaded_search(files, keywords, num_threads=3):
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    threads = []
    results = {keyword: [] for keyword in keywords}
    lock = Lock()
    files_per_thread = len(files) // num_threads

    for i in range(num_threads):
        
        start_index = i * files_per_thread
        end_index = None if i == num_threads - 1 else (i + 1) * files_per_thread
        thread_files = files[start_index:end_index]
        thread = Thread(target=search_in_files, args=(thread_files, keywords, results, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

# Приклад використання
if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt", "file6.txt"]
    keywords = ["python", "javascript", "<html>"]
    num_threads = 4
    
    start_time = time.time()
    results = multithreaded_search(files, keywords, num_threads)
    end_time = time.time()
    print(f"Results: {results}")
    print(f"Execution time: {end_time - start_time} seconds")