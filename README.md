# Introduction
This repository contains solutions to [homework 2](https://github.com/lucamaiano/ADM/tree/master/2022/Homework_2) for the 2022 class of  Algorithms for Data Mining at La Sapienza.

# Contributors:
* Gabriele Tromboni
* Ludovica Mazza
* Jonas Barth

# Structure

The main components of the repository are:

* `main.ipynb`: a jupyter notebook with all solutions to the homework.
* `docs`: folder containing source and exported diagram files.
* `plotting`: a python package containing functions related to plotting instagram data.
* `posts`: a python package containing functions related to instagram post data. 
* `CommandLine.sh`: a bash script that retrieves the first `n` posts with descriptions longer than `l` characters and outputs the profiles that posted them.


# Getting started
Before running the notebook, it is necessary to install the required packages. If using Anaconda, most of them will already be installed.

1. Create a virtual environment
    ```bash
    python -m venv env
    ```

2. Activate virtual environment 
   ```bash
   # On Windows
   env/Scripts/activate

   # On Linux
   env/bin/activate
   ```

3. Install requirements
   ```bash
   pip install -r requirements.txt
   ```
