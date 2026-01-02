"""
Multi-Agent System for Research and Summarization

This module implements a coordinated multi-agent system using LangChain
where a research agent gathers information and a summarizer agent condenses it.

Dependencies:
    - langchain >= 0.1.0
    - python-dotenv
"""

import logging
from typing import Optional
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.llms import OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.callbacks import get_openai_callback

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


class MultiAgentSystem:
    """A coordinated multi-agent system for research and summarization."""

    def __init__(self, temperature: float = 0, verbose: bool = True):
        """
        Initialize the multi-agent system.

        Args:
            temperature: LLM temperature for creativity vs determinism (0-1)
            verbose: Whether to log agent actions
        """
        self.temperature = temperature
        self.verbose = verbose
        self.llm = OpenAI(temperature=temperature)
        self.search = SerpAPIWrapper()
        self._setup_agents()

    def _setup_agents(self) -> None:
        """Initialize research and summarizer agents."""
        try:
            # Define tools
            research_tool = Tool(
                name="Web Research",
                func=self.search.run,
                description="Searches the web to answer questions"
            )

            summarizer_tool = Tool(
                name="Text Summarizer",
                func=self._summarize_text,
                description="Condenses provided text into a concise summary"
            )

            # Create agents
            self.research_agent = initialize_agent(
                tools=[research_tool],
                llm=self.llm,
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                verbose=self.verbose
            )

            self.summarizer_agent = initialize_agent(
                tools=[summarizer_tool],
                llm=self.llm,
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                verbose=self.verbose
            )

            logger.info("Agents initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize agents: {e}")
            raise

    def _summarize_text(self, text: str) -> str:
        """
        Summarize the given text.

        Args:
            text: Text to summarize

        Returns:
            Summarized text
        """
        if not text:
            return "No text provided to summarize"
        return self.llm.predict(f"Summarize this concisely:\n\n{text}")

    def process_query(self, query: str) -> Optional[dict]:
        """
        Process a query through research and summarization agents.

        Args:
            query: The research query

        Returns:
            Dictionary with research results and summary, or None if failed
        """
        if not query or not isinstance(query, str):
            logger.warning("Invalid query provided")
            return None

        try:
            logger.info(f"Processing query: {query}")

            with get_openai_callback() as cb:
                # Research phase
                logger.info("Starting research phase...")
                research_result = self.research_agent.run(query)

                # Summarization phase
                logger.info("Starting summarization phase...")
                summary = self.summarizer_agent.run(research_result)

                # Log token usage
                logger.info(
                    f"Tokens used - Total: {cb.total_tokens}, "
                    f"Prompt: {cb.prompt_tokens}, "
                    f"Completion: {cb.completion_tokens}"
                )

            return {
                "query": query,
                "research": research_result,
                "summary": summary,
                "token_usage": {
                    "total_tokens": cb.total_tokens,
                    "prompt_tokens": cb.prompt_tokens,
                    "completion_tokens": cb.completion_tokens
                }
            }

        except Exception as e:
            logger.error(f"Error processing query: {e}")
            return None


def main():
    """Main entry point for the multi-agent system."""
    try:
        # Initialize system
        system = MultiAgentSystem(temperature=0, verbose=True)

        # Example query
        query = "Latest advancements in quantum computing in 2025"

        # Process the query
        results = system.process_query(query)

        if results:
            print("\n" + "="*80)
            print("FINAL RESULTS")
            print("="*80)
            print(f"\nQuery: {results['query']}")
            print(f"\nResearch Results:\n{results['research']}")
            print(f"\nSummary:\n{results['summary']}")
            print(f"\nToken Usage: {results['token_usage']}")
        else:
            logger.error("Failed to process query")

    except Exception as e:
        logger.error(f"Fatal error in main: {e}")
        raise


if __name__ == "__main__":
    main()
