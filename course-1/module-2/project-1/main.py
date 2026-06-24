import time
import sys

from gemini_provider import gemini_response

# Loading animation for better user experience
def loading(message="Processing"):
    for _ in range(3):
        for dot in [".", "..", "..."]:
            sys.stdout.write(f"\r{message}{dot}")
            sys.stdout.flush()
            time.sleep(0.3)
    print("\r", end="")

def banner():
    print("Gemini LLM CLI Application")

def main():
    banner()
    print("Enter your prompt below. Type 'exit()' to quit.\n")

    while True:

        #Read user input
        prompt = input("Prompt: ").strip()

        #Exit Condition
        if prompt.lower() in ["exit", "Exit", "quit"]:
            print("\nExiting the application.\n")
            break
        if not  prompt:
            continue

        # Show Generating Response
        loading("Generating Response")

        try:
            output = gemini_response(prompt)

            print("\n Response")
            print(output)
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()