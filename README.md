# Jarvis-Clone
This is an AI voice assistant like Jarvis from Iron Man.

#### 📗 Main Features: 
+ 🌐 Can open any link provided with a voice command.
+ 🤖 Can reply to any question with it's AI module.
+ 🚀 Scalable: Can add more functionality if needed.

---

## Get Started

1. Clone this repository.
2. Type the follwoing command in your terminal to install the required python modules:
```git
pip install -r requirements.txt
```
3. Once the required modules have been installed, create a file named `.env`.
4. Declare the following variables in your `.env` file:

| Variable | Value |
| :------- | :---: |
| houndify-client-id | Your houndify client id |
| houndify-client-key | Your houndify client key |
| deepseek-client-key | Your deepseek-r1-distill-llama-70b:free api key from OpenRouter |
| wake-word | Any wake word of your choice (in lowercase). eg. jarvis |
| termination-phrase | Any phrase of your choice (in lowercase). eg. stop |

5. Next edit the `library.py` file for your assistant to function as per your command.
6. Type the following command in your terminal and enjoy:
```git
python main.py
```
OR
```git
python3 main.py
```