# goit-cs-hw-04 - Search in files with Multithreading and Multiprocessing

## Overview

This project demonstrates two approaches to processing a list of files concurrently to search for specific keywords. The two methods used are:

- Multithreading: Using Python's threading module.
- Multiprocessing: Using Python's multiprocessing module.
  Both approaches aim to improve the efficiency of file processing by parallelizing the tasks.

## Features

- Concurrent file processing using threads or processes.
- Efficient distribution of files among threads/processes.
- Measurement of execution time for performance comparison.
- Error handling for file system operations.
- Return results in a dictionary format where the key is the search keyword and the value is a list of file paths containing that keyword.

## Requirements

Python 3.x

## Usage

- Clone the repository:

      git clone https://github.com/alexvekh/goit-cs-hw-04.git

- Use:

  - mt_search.py - for multitreading search,
  - mp_search.py - for multiprocessing search

- correct actual data in code:

  - files
  - keywords
  - num_threads or num_processes

- run file with python

      python mt_search.py
      python mp_search.py
