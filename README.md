# Simple Data Mapping Project
> Script for mapping data from API to pydantic's BaseModel class.

<!-- > Live demo [_here_](https://www.example.com). <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Project Status](#project-status)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
Simple script that will pull the newest articles from the provided API every 5 minutes,
then map them into a format defined in the models.py file (class Article)
and finally print them out. 


## Technologies Used
- Python - version 3.8


## Setup

To run this code you need Python veriosn 3.8 or higher and requirements shown in requirements.txt. 

You can easly start using this code following these instructions below (for Linux users).


1. Open Terminal.

2. Change the current working directory to the location where you want the cloned directory.

3. Type git clone, and then paste the URl given below.

 &nbsp; &nbsp; &nbsp; &nbsp; "git clone https://github.com/mendyk-ja/simple_data_mapping.git"
 
4. Change the current working directory to the location: simple_data_mapping/.

 &nbsp; &nbsp; &nbsp; &nbsp; cd simple_data_mapping/

5. Create virtual environment for project script.
 
 &nbsp; &nbsp; &nbsp; &nbsp; virtualenv venv 
 
6. Activate virtual environment.
 
 &nbsp; &nbsp; &nbsp; &nbsp; source venv/bin/activate
 
7. Install requirements from requirements.txt
 
 &nbsp; &nbsp; &nbsp; &nbsp; pip3 install -r requirements.txt
 
8. Run project script.
 
 &nbsp; &nbsp; &nbsp; &nbsp; python3 simple_data_mapping.py

## Project Status
Project is: complete, but some improvements will be still done.

## Contact
Created by [Jacek Mendyk](https://www.linkedin.com/in/jacekmendyk/) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
