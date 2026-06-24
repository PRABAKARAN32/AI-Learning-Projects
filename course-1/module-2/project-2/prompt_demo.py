from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

from connect_llm import connect_gemini 

llm = connect_gemini()

def single_prompt_demo():
    print("\n--- PromptTemplete ---")

    topic = input("Enter the Topic: ")
    tone = input("Choose tone (funny / formal / simple): ")
    length = input("Choose length (short / medium / long): ")

    template_text = (
        "Write a {tone} explanation about the topic: {topic}. "
        "Make the explanation {length} and easy to understand."
    )

    prompt = PromptTemplate(
        input_variables=["tone", "topic", "length"],
        template=template_text
    )

    final_prompt = prompt.format(
        tone=tone,
        topic=topic,
        length=length
    )
    print("\nGenerated Prompt:")
    print(final_prompt)

    print("\nSending to Gemini...\n")
    response = llm.invoke(final_prompt)

    print("Gemini Response:")
    print(response.content)


def chart_prompt_templet():

    print("\n--- ChatPromptTemplate ---")

    system_role = input("Enter system instruction (e.g., You are a tutor): ")
    user_question = input("Enter user message: ")
    # tone = input("Choose AI tone (friendly / strict / expert): ")

    chat_template = ChatPromptTemplate.from_messages([
        ("system", "{system_role}"),
        ("user", "{user_question}"),
        # ("assistant", "Respond in a {tone} tone.")
    ])

    # Format chat messages
    formatted_chat = chat_template.format_messages(
        system_role=system_role,
        user_question=user_question,
        # tone=tone
    )

    # print(formatted_chat)

    print("\nGenerated Chat Prompt:")
    for msg in formatted_chat:
            print(f"{msg.type.upper()}: {msg.content}")

    print("\nSending to Gemini...\n")
    response = llm.invoke(formatted_chat)

    print("Gemini Reply:")
    print(response.content)
    