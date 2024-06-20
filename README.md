# News Summarizer

## Demo
 ![demo-gif](https://github.com/jivaniyash/news-summarizer/blob/main/demo/gradio_demo.gif)

## Usage
This repository provides a news summarizer assistant using openai model - `gpt-3.5-turbo-0125` powered by Gradio. Follow the instructions below to set up and run the application. 

## Overview 
1. User selects News Category, Date, Character Limit & Output tone.
2. News Summarizer takes in the selected News Article from the `news` directory (<NEWS-API> in production)
3. Using OpenAI's Chat-completion Api, News Article is sent as a context along with output description as a context.
4. News Summary is displayed in Front-End using Gradio. 

## Requirements
- Python 3.7 or higher
- virtualenv
- git
- OpenAI API key

## Steps to Start the App

### 1. Clone the Repository
```sh
git clone https://github.com/jivaniyash/news-summarizer
```

### 2. Set up a Virtual Environment
```sh
virtualenv venv
source venv/bin/activate
```

### 3. Install Python Requirements
```sh
pip install -r requirements.txt
```

### 4. Run the App
At first run, it will take time to load the files properly.
```sh
gradio ./app.py 
```