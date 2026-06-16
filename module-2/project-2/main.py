from prompt_demo import single_prompt_demo, chart_prompt_templet

def main():

    print("\n Hi There Select You'er Choice")

    while True:
        print("\n 1. Single Prompt Agent")
        print("\n 2. Chart Prompt Agent")
        print("\n `exit`, `quit` for exit")

        option = input("")

        if option in ['exit', 'quit']:
            break
        elif option == '1':
            single_prompt_demo()
        elif option == '2':
            chart_prompt_templet()
        else:
            continue




if __name__ == "__main__":
    main()