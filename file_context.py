from logger.log import logger
import os
import traceback


@logger.catch()
def process_file_context(file_path: str) -> dict:
    """Read and process a file's content.
    
    Args:
        file_path: Path to the file
        context: Dictionary to store file content
    
    Returns:
        Updated context dictionary
    """
    if not file_path:
        logger.warning("No file path provided")
        return ""
    
    try:
        # Normalize path separators for cross-platform compatibility
        normalized_path = os.path.normpath(file_path)
        
        # Check if file exists
        if not os.path.isfile(normalized_path):
            logger.error(f"File not found: {normalized_path}")
            return ""
        
        # Read file content with universal newlines mode
        with open(normalized_path, "r", encoding="utf-8", newline=None) as f:
            content = f.read()
            
        return content
        
    except Exception as e:
        logger.error(f"Error reading file {normalized_path}: {e}")
        logger.error(traceback.format_exc())
        return ""