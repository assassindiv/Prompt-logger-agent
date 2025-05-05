# main.py
from datetime import datetime

def log_prompt(prompt):
    with open("prompt_log.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {prompt}\n")

def main():
    print(" Hello! I'm your Prompt Logger Agent.")
    while True:
        user_input = input("What task would you like me to log? (type 'exit' to quit)\n> ")
        if user_input.lower() == 'exit':
            print(" Goodbye! Your prompts are saved.")
            break
        log_prompt(user_input)
        print(" Prompt logged!\n")

        print(" You can ask me to log any task or prompt you have in mind.")
        print(" Just type it in and I'll take care of the rest.")

if __name__ == "__main__":
    main()