from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

from connect_llm import connect_llm

llm = connect_llm()


class Prompting:

    # Zero Shot Prompting
    def zero_shot_prompting(self):
        topic = input("Enter the topic: ")

        prompt_draft = (
            "Explain the topic of {topic} in short format."
        )

        prompt = PromptTemplate(
            input_variables=["topic"],
            template=prompt_draft
        )

        final_prompt = prompt.format(
            topic=topic
        )

        print(f" User: {final_prompt} \n")

        print("LLM is generating ...")

        response = llm.invoke(final_prompt)

        print(f" LLM Response {response.content} \n")

        print(
            f"LLM Total token Used \n "
            f"Input Tokens = {response.usage_metadata['input_tokens']} \n "
            f"Output Tokens = {response.usage_metadata['output_tokens']} \n "
            f"Total Tokens = {response.usage_metadata['total_tokens']}"
        )

    # Few Shot Prompting
    def few_shot_prompting(self):
        topic = input("Enter the topic: ")

        prompt_draft = (
            "Explain the topic of {topic} in short format, which needs to be in technical terms, "
            "and if the user asks for content related to any topic, explain it with examples if required."
        )

        prompt = PromptTemplate(
            input_variables=["topic"],
            template=prompt_draft
        )

        final_prompt = prompt.format(
            topic=topic
        )

        print(f" User: {final_prompt} \n")

        print("LLM is generating ...")

        response = llm.invoke(final_prompt)

        print(f" LLM Response {response.content} \n")

        print(
            f"LLM Total token Used \n "
            f"Input Tokens = {response.usage_metadata['input_tokens']} \n "
            f"Output Tokens = {response.usage_metadata['output_tokens']} \n "
            f"Total Tokens = {response.usage_metadata['total_tokens']}"
        )

    # Chain of Thoughts
    def chain_of_thoughts(self):

        topic = input("Enter the topic: ")

        prompt_draft1 = (
            "Explain the topic of {topic} in brief format."
        )

        prompt = PromptTemplate(
            input_variables=["topic"],
            template=prompt_draft1
        )

        final_prompt1 = prompt.format(
            topic=topic
        )

        print(f" User: {final_prompt1} \n")

        print("LLM is generating ...")

        response1 = llm.invoke(final_prompt1)

        print(f"Responce 1 :{response1.content}")


        prompt_draft2 = (
            "Give me 5 important points from the below elaborated paragraph. {response1}"
        )

        prompt = PromptTemplate(
            input_variables=["response1"],
            template=prompt_draft2
        )

        final_prompt2 = prompt.format(
            response1=response1.content
        )

        print(f" User: {final_prompt2} \n")

        response2 = llm.invoke(final_prompt2)

        print(f" LLM Response 1 {response2.content} \n")

        input_token = response1.usage_metadata['input_tokens'] + response2.usage_metadata['input_tokens']
        output_token = response1.usage_metadata['output_tokens'] + response2.usage_metadata['output_tokens']
        total_token = response1.usage_metadata['total_tokens'] + response2.usage_metadata['total_tokens']

        print(
            f"LLM Total token Used \n "
            f"Input Tokens = {input_token} \n "
            f"Output Tokens = {output_token} \n "
            f"Total Tokens = {total_token}"
        )

    # Higher Order Prompting
    def higher_order_prompting(self):
        topic = input("Enter the topic: ")
        tone = input("Enter the tone (professional, friendly, strict): ")
        length = input("Enter the length of the response (short, medium, long): ")

        prompt_draft = (
            "Explain the topic of {topic} in {length} format, which needs to be in technical terms, "
            "and if the user asks for content related to any topic, explain it with examples if required. "
            "The tone of the response should be {tone}."
        )

        prompt = PromptTemplate(
            input_variables=["topic"],
            template=prompt_draft
        )

        final_prompt = prompt.format(
            topic=topic,
            tone=tone,
            length=length
        )

        print(f" User: {final_prompt} \n")

        print("LLM is generating ...")

        response = llm.invoke(final_prompt)

        print(f" LLM Response {response.content} \n")

        print(
            f"LLM Total token Used \n "
            f"Input Tokens = {response.usage_metadata['input_tokens']} \n "
            f"Output Tokens = {response.usage_metadata['output_tokens']} \n "
            f"Total Tokens = {response.usage_metadata['total_tokens']}"
        )