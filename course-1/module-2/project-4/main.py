from context_persona import PERSONA
from connect_llm import connect_llm

from langchain_core.prompts import PromptTemplate


llm = connect_llm()

# Define the User context
def get_user_context():
    print("Select Your Persona")
    print("software_engineer")
    print("cloud_architect")
    print("ai_engineer")
    print("cybersecurity_engineer")

    persona = input("  ")
    tone = input("Enter the Tone (eg : friendly / professional / straight): ")
    response_way = input("Enter the way of response you need : (eg : JSON , Bullet Point ...): ")
    length = input("Enter the Length of the response You need : (short / medium / long): ")
    query = input("Enter Your Query : ")

    return {"persona" : persona, "tone": tone or "not preferred" , "response_way" : response_way or "Free Text", "length" : length , "query": query}

# The main Functionality of the user
def context_engineering(persona_key, tone, length, response_way, query):
    persona = PERSONA[persona_key]['persona']
    role = PERSONA[persona_key]['role']

    prompt = f"{persona} and your role is {role} make tone of the response in {tone} and the query is {query}, You need to response in the way of {response_way} and the length of the response should be {length}"

    response = llm.invoke(prompt)
    print(response.content)

    llm_token_usage(response.usage_metadata)


def llm_token_usage(tokens):
    print(f"Input Tokens : {tokens['input_tokens']}")
    print(f"Output Tokens : {tokens['output_tokens']}")
    print(f"Total Tokens : {tokens['total_tokens']}")

def main():

    print("Enter the Following Details Correctly :")
    while True:
        option = input("Welcome back, Enter to interact with llm or `exit`, `quit` to exit")

        if option in ["Exit", "exit", "quit", "Quit"]:
            print("Thank You")
            break
        user_context_inputs = get_user_context()
        persona = user_context_inputs["persona"]
        tone = user_context_inputs["tone"]
        response_way = user_context_inputs["response_way"]
        length = user_context_inputs["length"]
        query = user_context_inputs["query"]
        context_engineering(persona, tone, response_way, length, query)

if __name__ == "__main__":
    main()