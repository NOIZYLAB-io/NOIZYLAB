
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.llms import OpenAI
from langchain.utilities import SerpAPIWrapper

# Initialize the language model
llm = OpenAI(temperature=0)

# Set up the search tool using SerpAPI
search = SerpAPIWrapper()

# Define the tools for each agent
research_tool = Tool(
    name="Web Research",
    func=search.run,
    description="Useful for answering questions by searching the web."
)

summarizer_tool = Tool(
    name="Summarizer",
    func=llm.predict,
    description="Summarizes the given text into a concise format."
)

# Create the research agent
research_agent = initialize_agent(
    tools=[research_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Create the summarizer agent
summarizer_agent = initialize_agent(
    tools=[summarizer_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Example query
query = "Latest advancements in quantum computing"

# Run the research agent
research_result = research_agent.run(query)

# Run the summarizer agent
summary = summarizer_agent.run(research_result)

# Print the final summary
print("Final Summary:")
print(summary)
