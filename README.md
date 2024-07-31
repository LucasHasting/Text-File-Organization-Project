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
    git clone https://github.com/LucasHasting/IP-Subnet-Calculator.git
    ```

2. Navigate to the project directory and execute the program:

    ```sh
    cd IP-Subnet-Calculator
    py subnetting.py
    ```
### Option 2: without git
1. Download the project as a zip file
2. [Extract the zip file](https://www.wikihow.com/Unzip-a-File)
3. In windows, the subnetting.py file can be clicked to execute

#### Run from the command line
1. Find the location of the files
2. Copy the path
3. go to the command line and run the following:
   ```sh
   cd /path/to/files
   py subnetting.py
   ```

## Usage

The program asks the user to enter an IP address and subnet mask in dotted decimal form, and will output the network address, usables range, and the broadcast address.

## Example

![EXAMPLE](example.png)

## Program-Overview

[subnetting.py](https://github.com/LucasHasting/IP-Subnet-Calculator/blob/main/subnetting.py): contains the main driver of the program and is what needs to be executed.   
[functions_and_constants.py](https://github.com/LucasHasting/IP-Subnet-Calculator/blob/main/functions_and_constants.py): contains the constants used in both programs and the functions used in subnetting.py


## Notice-for-when-the-code-is-read
This project's purpose is the execution of the code, not the beauty of it. This project was a side project I made in highschool. As such, the code is poorly written and hard to read, I appologize for that, but I no longer remember how I made this as it was most likely over complicated and I no longer wish to remember how I made it. 
