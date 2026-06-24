from langchain_core.runnables import (
    RunnablePassthrough,
    RunnableParallel,
    RunnableLambda
)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from connect_llm import connect_llm

llm = connect_llm()

def runnabel_passthrough():
    countery = input("Enter the Countery name : ")


    prompt_temp_1 = ChatPromptTemplate.from_template(
        "Give me the Detailed overview of the countery {countery} and most viseted torist place and what are the special of torist place."
        )
    
    prompt_temp_2 = ChatPromptTemplate.from_template(
        "Give me 5 strong poins why I need to visit the country {countery}."
    )

    prompt_temp_3 = ChatPromptTemplate.from_template(
        "Give me some of Guidenc and torisum rules to be followed to the {countery}"
    )


    #Prompts
    

    chain1 = prompt_temp_1 | llm | StrOutputParser()
    chain2 = prompt_temp_2 | llm | StrOutputParser()
    chain3 = prompt_temp_3 | llm | StrOutputParser()

    # print("Chain 1", chain1)
    # print("Chain 2", chain2)


    parell_chain = RunnableParallel(
        {
        "prompt_1": prompt_temp_1 | RunnableLambda(lambda x: x.to_string()),
        "prompt_2": prompt_temp_1 | RunnableLambda(lambda x: x.to_string()),
        "prompt_3": prompt_temp_1 | RunnableLambda(lambda x: x.to_string()),
        "result1": chain1,
        "result2": chain2,
        "result3": chain3,
        "input" : RunnablePassthrough()
        }
    )

    result = parell_chain.invoke({
        "countery":countery,
    })


    print("Runnabel Passthrough Outputs \n: ")

    print("Prompt 1 : ", result["prompt_1"])

    print("Responce 1 :", result["result1"])

    print("Prompt 2", result["prompt_2"])

    print("Responce 2 :", result["result2"])

    print("Prompt 3", result["prompt_3"])

    print("Responce 3 :", result["result3"])

    print("Input : ", result["input"])

