# Jarvis-Clone
This is an AI voice assistant like Jarvis from Iron Man.
---
## Get Started
1. Clone this repository.
2. Type the follwoing command in your terminal to install the required python modules:
```git
pip install -r requirements.txt
```
3. Once the required modules have been installed, create a file named `.env`.
4. Declare the following variables in your `.env` file:
|Variable|Value|
|:-------|:---:|
|houndify-client-id|Your houndify client id|
|houndify-client-key|Your houndify client key|
|deepseek-client-key|Your deepseek-r1-distill-llama-70b:free api key from OpenRouter|
|wake-word|Any wake word of your choice eg. Jarvis|
|termination-phrase|Any phrase of your choice eg. Stop|