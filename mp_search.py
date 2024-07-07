from multiprocessing import Queue, Process, Pool, current_process
import os
import time
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def search_in_files(file_list, keywords, queue):
    name = current_process().name
    logger.debug(f"{name} (pid={current_process().pid}) started fo search in {file_list} ...")
    # logger.debug(f"{name} started...")
    results = {keyword: [] for keyword in keywords}
    for file in file_list:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                for keyword in keywords:
                    if keyword in content:
                        results[keyword].append(file)
                # print(f" - - {file} result: {results}") 
                       
        except Exception as e:
            print(f"Error processing file {file}: {e}")
    print(f"- {name} result: {results}") 
    queue.put(results)

def multiprocess_search(files, keywords, num_processes=4):

    processes = []
    queue = Queue()
    files_per_process = len(files) // num_processes

    for i in range(num_processes):
        start_index = i * files_per_process
        end_index = None if i == num_processes - 1 else (i + 1) * files_per_process
        process_files = files[start_index:end_index]
        process = Process(target=search_in_files, args=(process_files, keywords, queue))
        processes.append(process)
        process.start()

    results = {keyword: [] for keyword in keywords}
    for process in processes:
        process_results = queue.get()
        for keyword, files in process_results.items():
            results[keyword].extend(files)

    for process in processes:
        process.join()

    return results

# Приклад використання
if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt", "file6.txt"]
    keywords = ["python", "javascript", "<html>"]
    num_processes = 4

    start_time = time.time()
    results = multiprocess_search(files, keywords, num_processes)
    end_time = time.time()
    print(f"Results: {results}")
    print(f"Execution time: {end_time - start_time} seconds")