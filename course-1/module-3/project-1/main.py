from connect_llm import connect_llm
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from encoding import read_transcript
from format_llm_output import format_output

# Import for Memory

from langgraph.checkpoint.memory import InMemorySaver


SYSTEM_PROMPT = """
You are an Intelligent Meeting Notes Assistant.

This agent works across multiple messages in the same session, and must remember:
- What the user said earlier
- What you previously explained
- The meeting transcript you already analyzed

If the user asks a question like:
- “Can you remind me what the meeting was about?”
- “What did you extract earlier?”
- “What decisions did we identify?”

– you should use your memory of previous steps to answer.

Your tasks:
- Extract key discussion points
- Extract decisions
- Extract action items and owners
- Create summaries when needed
- Support follow-up questions that depend on earlier context

Rules:
- Do not invent details not present in the transcript or prior messages
- Keep answers clear and structured
- Use tools when helpful

"""

# Tool  that LLM can use

def extract_key_points(text: str):
    """Extract lines containing discussions or updates."""

    lines = text.split("\n")
    points = []

    for line in lines:
        if "discuss" in line.lower() or "update" in line.lower():
            points.append(line.strip())

    return "\n".join(points) if points else "No key points found"


def extract_action_items(text: str):
    """Extract lines that mention action items."""

    lines = text.split("\n")

    action = []

    for line in lines:
        if any(word in line.lower() for word in ["action", "will", "needs", "should"]):
            action.append(line.strip())

    return "\n".join(action) if action else "No action items found."

def summarize_metting(text: str):
    """Returning a simple short summary of the meeting."""

    lines = text.split("\n")[:10]
    return f"Summary: \n" + "\n".join(lines)


# Create an instance of memory
memory = InMemorySaver()
# Connect to the LLM model
model = connect_llm()


tools = [extract_key_points, extract_action_items, summarize_metting]

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
    # Add short-term memory to the create_agent framework
    checkpointer=memory
)

THREAD_ID = "meeting-session-1"

def main():
    transcript = read_transcript("transcript2.txt")

    print("First, the agent will analyze the meeting transcript...\n")

    #First call - seed the memory with transcript
    result = agent.invoke({
        "messages":[
            HumanMessage(
                content="Here is the meeting transcript. Please analyze it:\n\n"
                    + transcript
                )
            ]
    },
    {"configurable": {"thread_id": THREAD_ID}},
    )

    print("------Agent Output------")
    print("Agent:\n")

    content = result["messages"][-1].content

    formated_output = format_output(content)

    print(formated_output)

    print("\n Now you can ask follow-up questions.")
    print("Type 'exit' to stop \n")

    # Interactive loop
    while True:
        user_input = input("You: ")

        if user_input.lower().strip() == "exit":
            print("\nEnding demo. Goodbye!\n")
            break

        response = agent.invoke(
            {"messages": [HumanMessage(content=user_input)]},
            {"configurable": {"thread_id": THREAD_ID}},
        )

        content = response["messages"][-1].content

        formated_output = format_output(content)

        print("\nAgent:", formated_output, "\n")

if __name__ == "__main__":
    main()

