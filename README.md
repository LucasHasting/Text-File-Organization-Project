# Text File Organization Project
This repositroy holds a python project that will show the content of a txt file based on a heading and sub-heading. It uses a Cisco IOS Cheat Sheet that I made as an example.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Program-Overview](#program-overview)
- [Notice-for-when-the-code-is-read](#notice-for-when-the-code-is-read)

## Installation

This project does not require any external pip packages. You only need [Python](https://www.python.org/downloads/) installed on your system.

### Option 1: using [git](https://git-scm.com/downloads)
1. Clone the repository:

    ```sh
    git clone https://github.com/LucasHasting/Text-File-Organization-Project.git
    ```

2. Navigate to the project directory and execute the program:

    ```sh
    cd Text-File-Organization-Project
    py main.py
    ```
### Option 2: without git
1. Download the project as a zip file
2. [Extract the zip file](https://www.wikihow.com/Unzip-a-File)

#### Run from the command line
1. Find the location of the files
2. Copy the path
3. go to the command line and run the following:
   ```sh
   cd /path/to/files
   py main.py
   ```

## Usage

The program uses a command line user interface to display contents of a text file. It first asks for an input file, then it displays a numbered menu to select a heading and subheading, all other text that is not selected is filtered out. The screen is cleared durring each transistion. The txt file must use specefic characters to determine a heading and subheading and this can only be changed by modifing lines 4 and 5 in the source code. See [Notice-for-when-the-code-is-read](#notice-for-when-the-code-is-read) for a reason why this is.

## Example

![EXAMPLE](example.png)

## Program-Overview

[main.py](https://github.com/LucasHasting/Text-File-Organization-Project/blob/main/main.py): The entire program.

## Notice-for-when-the-code-is-read
This project's purpose is the execution of the code, not the beauty of it. This project was a side project I made in highschool. As such, the code is poorly written and hard to read, I appologize for that, but I no longer remember how I made this as it was most likely over complicated and I no longer wish to remember how I made it. 
