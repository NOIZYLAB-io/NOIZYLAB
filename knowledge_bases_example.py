"""
Example usage of the refactored knowledge_bases service.
This demonstrates how to use the functional MicroMongo-based implementation.
"""

from BASE.services.knowledge_bases import (
    create_knowledge_base,
    get_knowledge_base_by_name,
    get_knowledge_base_by_id,
    exists_knowledge_base_by_name,
    exists_knowledge_base_by_id,
    update_knowledge_base,
    delete_knowledge_base,
    list_all_knowledge_bases,
    count_knowledge_bases
)


def example_usage():
    """
    Example function showing how to use the knowledge bases service.
    """
    
    # Create a new knowledge base
    kb_id = create_knowledge_base(
        name="My Test KB",
        kbid="kb_001",
        metadata={
            "path": "/path/to/documents",
            "description": "Test knowledge base",
            "created_at": "2024-01-01"
        },
        is_auto_indexed=False
    )
    print(f"Created knowledge base with ID: {kb_id}")
    
    # Check if knowledge base exists
    if exists_knowledge_base_by_name("My Test KB"):
        print("Knowledge base exists!")
    
    # Get knowledge base by name
    kb = get_knowledge_base_by_name("My Test KB")
    if kb:
        print(f"Found KB: {kb['name']} with ID: {kb['id']}")
    
    # Get knowledge base by ID
    kb_by_id = get_knowledge_base_by_id("kb_001")
    if kb_by_id:
        print(f"Found KB by ID: {kb_by_id['name']}")
    
    # Update knowledge base
    update_result = update_knowledge_base("kb_001", {
        "metadata.description": "Updated description",
        "last_updated": "2024-01-02"
    })
    print(f"Update result: {update_result.modified_count} documents modified")
    
    # List all knowledge bases
    all_kbs = list_all_knowledge_bases()
    print(f"Total knowledge bases: {len(all_kbs)}")
    for kb in all_kbs:
        print(f"  - {kb['name']} (ID: {kb['id']})")
    
    # Count knowledge bases
    total_count = count_knowledge_bases()
    print(f"Knowledge base count: {total_count}")
    
    # Delete knowledge base
    delete_result = delete_knowledge_base("kb_001")
    print(f"Delete result: {delete_result.deleted_count} documents deleted")


def create_auto_indexed_example():
    """
    Example of creating an auto-indexed knowledge base.
    """
    
    # Create an auto-indexed knowledge base
    kb_id = create_knowledge_base(
        name="Auto-Indexed KB",
        kbid="auto_kb_001",
        metadata={
            "path": "/path/to/auto/documents",
            "type": "auto_indexed",
            "scan_interval": "1h"
        },
        is_auto_indexed=True
    )
    print(f"Created auto-indexed KB with ID: {kb_id}")


if __name__ == "__main__":
    print("=== Knowledge Bases Service Example ===")
    example_usage()
    
    print("\n=== Auto-Indexed Example ===")
    create_auto_indexed_example()
