from dotenv import load_dotenv
load_dotenv()
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

#build-in tool


search_tools= TavilySearchResults(max_results =5)

llm=GoogleGenerativeAI(model="gemini-3-flash-preview")

prompt=ChatPromptTemplate.from_template(
    """ 
    you are a helpful assistant

    summarize the following news in clear bullet points
    {news}
    """
)

chain = prompt | llm | StrOutputParser()

topic=input("Enter the topic to get the result:")

news_result= search_tools.run(f"Latest {topic} news:")
result=chain.invoke({"news":news_result})

print(result)

print("\nSources:")
if isinstance(news_result, list):
    for item in news_result:
        print("-", item["url"])
 