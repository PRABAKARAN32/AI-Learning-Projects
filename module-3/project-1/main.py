from connect_llm import connect_llm
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from encoding import read_transcript

from format_llm_output import format_output


SYSTEM_PROMPT = """
You are an Intelligent Meeting Notes Assistant.

Your responsibilities:
- Identify key discussion points from the meeting transcript
- Extract decisions made during the meeting
- Extract action items along with responsible owners
- Produce a clean, structured summary

Rules:
- Use tools when necessary
- Do NOT add information that is not in the transcript
- Be accurate, factual, and concise
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

# Connect to the LLM model
model = connect_llm()


tools = [extract_key_points, extract_action_items, summarize_metting]

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=SYSTEM_PROMPT
)

def main():
    transcript = read_transcript("transcript2.txt")

    print("\n--- Agent Output ---\n")

    #invoke
    result = agent.invoke({
        "messages":[HumanMessage(content=transcript)]
    })

    content = result["messages"][-1].content

    # print(content)

    formated_output = format_output(content)

    print(formated_output)


if __name__ == "__main__":
    main()

