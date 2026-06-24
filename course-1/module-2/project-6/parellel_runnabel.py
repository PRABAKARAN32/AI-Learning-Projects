from langchain_core.runnables import (
    RunnableParallel
)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from connect_llm import connect_llm

llm = connect_llm()

def runnabel_parallel():
    countery = input("Enter the Countery name : ")


    prompt_temp_1 = ChatPromptTemplate.from_template(
        "Give me the Detailed overview of the countery {countery} and most viseted torist place and what are the special of torist place."
        )
    
    prompt_temp_2 = ChatPromptTemplate.from_template(
        "Give me 5 strong poins why I need to visit the country {countery}."
    )


    #Prompts
    

    chain1 = prompt_temp_1 | llm | StrOutputParser()
    chain2 = prompt_temp_2 | llm | StrOutputParser()

    # print("Chain 1", chain1)
    # print("Chain 2", chain2)


    parell_chain = RunnableParallel(
        {
        "result1": chain1,
        "result2": chain2
        }
    )

    result = parell_chain.invoke({
        "countery":countery,
    })

    print("Results 1: " , result["result1"])
    print("Results 2: " , result["result2"])