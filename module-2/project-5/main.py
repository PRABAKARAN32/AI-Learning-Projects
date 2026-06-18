from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from connect_llm import connect_llm

def ai_agents():
    llm = connect_llm()

    print("=" * 60)
    print("LCEL Chain Examples")
    print("=" * 60)

    is_exit = False

    while True:
        if is_exit:
            option = input(
                "Do you want to continue or exit\n"
                "For continue simply press Enter\n"
                "For exit Enter `exit`, `Exit`, `quit`, `Quit`: "
            )

            if option.lower() in ['exit', 'quit']:
                break

        is_exit = True
        
        role = input("Enter the role to set the AI to act as it (e.g., senior software_engineer, senior cloud_architect, senior ai_engineer)")
        topic = input("Enter the Topic that you need to Explain: ")
        tone = input("Enter the Tone that you need to set (e.g., friendly / professional / dramatic)")

        prompt = ChatPromptTemplate.from_template(
            "You're the {role} and you need to clearly explain in detail about the {topic} from your experience and the tone of your explanation should be {tone}. If needed, provide examples too, and explain them for better understanding."
        )

        simple_chain = prompt | llm | StrOutputParser()

        result = simple_chain.invoke({
            "role": role,
            "topic": topic,
            "tone": tone,
        })

        print("\nOutput:", result)

def main():
    ai_agents()

if __name__ == "__main__":
    main()