from prompts_technic import Prompting


prompting_technic = Prompting()

while True:
    print(
        "Enter the option to Select and work with the Prompting Technic\n" \
        "1.Zero Shot Prompting\n" \
        "2.Few Shot Prompting\n" \
        "3.Chain of Thoughts\n" \
        "4.Higher Order Prompting\n" \
        "For Exit Enter `quit` or `exit` " \
    )

    option = input("")

    if option in ["quit", "exit", "Quit", "Exit"]:
        break
    elif option == "1":
        prompting_technic.zero_shot_prompting()
    elif option == "2":
        prompting_technic.few_shot_prompting()
    elif option == "3":
        prompting_technic.chain_of_thoughts()
    elif option == "4":
        prompting_technic.higher_order_prompting()
    else:
        continue