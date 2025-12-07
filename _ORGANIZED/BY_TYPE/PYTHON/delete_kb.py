import httpx
from BASE.services.knowledge_bases import get_knowledge_base_by_id, delete_knowledge_base, update_knowledge_base_cloud_id
from BASE.vdb.qdrant import get_qdrant_client
from logger.log import logger
import constants
from startup_config import delete_kb_path
import json
from ipc import IPC
ipc_ = IPC.connect()

@logger.catch()
async def delete_kb_from_cloud(kbid: str, cloud_id: str):
    """Delete a knowledge base from cloud storage."""
    session = ipc_.get("current_session") if ipc_.get("current_session") else None
    if not session:
        logger.error("No session provided for cloud KB delete")
        return {"status": "error", "message": "No session provided"}
    try:
        async with httpx.AsyncClient(verify=constants.SSL_CONTEXT) as client:
            response = await client.post(
                f"{constants.cloud}/knowledge/delete",
                json={"kbid": cloud_id},
                headers={"X-Session": session,
                "Content-Type": "application/json"},
            )
            return response.json()
    except Exception as e:
        logger.error(f"Error deleting knowledge base from cloud: {e}")
        raise


@logger.catch()
async def delete_local_storage(kbid: str):
    """Delete knowledge base from local storage (Qdrant + database)."""
    # Delete from Qdrant collection
    try:
        qdrant_client = get_qdrant_client()
        collection_name = kbid

        collections = await qdrant_client.get_collections()
        collection_names = [col.name for col in collections.collections]

        if collection_name in collection_names:
            await qdrant_client.delete_collection(collection_name)
            logger.info(f"Qdrant collection '{collection_name}' deleted successfully")
        else:
            logger.warning(f"Qdrant collection '{collection_name}' not found")

    except Exception as e:
        logger.error(f"Error deleting Qdrant collection: {e}")
        # Continue with database deletion even if Qdrant deletion fails

    # Delete from database
    delete_result = delete_knowledge_base(kbid)
    return delete_result


@logger.catch()
async def delete_kb_source(kbid: str):
    """
    Delete a knowledge base by ID with source-based logic.

    Args:
        kbid: Knowledge base ID to delete
        source: Source to delete from ("both", "local", "cloud")

    Returns:
        Dictionary with deletion status and message
    """

    # logger.info(f"Processing delete request for knowledge base: {kbid}, source: {source}")

    try:
        # Check if knowledge base exists
        kb_info = get_knowledge_base_by_id(kbid)
        logger.info(f"kb_info: {json.dumps(kb_info, indent=2)}")
        if not kb_info:
            logger.warning(f"Knowledge base not found: {kbid}")
            return {"status": "error", "message": f"Knowledge base not found: {kbid}"}

        logger.info(f"Found knowledge base: {kb_info.get('name', 'Unknown')}")

        cloud_id = kb_info.get("cloud_id")

        # # Handle cloud deletion
        # if source in ["BOTH", "REMOTE"]:
        #     if cloud_id:
        #         try:
        #             await delete_kb_from_cloud(kbid, cloud_id)
        #             logger.info(f"Knowledge base deleted from cloud: {cloud_id}")

        #             # Update cloud_id to null after successful cloud deletion
        #             update_knowledge_base_cloud_id(kbid, None)
        #             logger.info(f"Cloud ID cleared for knowledge base: {kbid}")

        #         except Exception as e:
        #             logger.error(f"Error deleting from cloud: {e}")
        #             if source == "cloud":
        #                 return {"status": "error", "message": f"Failed to delete from cloud: {str(e)}"}
        #     else:
        #         logger.warning(f"No cloud_id found for knowledge base: {kbid}")
        #         if source == "cloud":
        #             return {"status": "error", "message": "Knowledge base has no cloud_id"}

        # # Handle local deletion
        # if source in ["both", "LOCAL"]:
        #     delete_result = await delete_local_storage(kbid)

        #     if delete_result.deleted_count > 0:
        #         logger.info(f"Knowledge base deleted from local storage: {kbid}")
        #     else:
        #         logger.error(f"Failed to delete knowledge base from local storage: {kbid}")
        #         return {"status": "error", "message": "Failed to delete from local storage"}

        # # Determine success message based on source
        # if source == "both":
        #     message = "Knowledge base successfully deleted from both cloud and local storage"
        # elif source == "cloud":
        #     message = "Knowledge base successfully deleted from cloud storage"
        # else:
        #     message = "Knowledge base successfully deleted from local storage"

        delete_result = await delete_local_storage(kbid)
        if cloud_id:
            await delete_kb_from_cloud(kbid, cloud_id)

        if delete_result.deleted_count > 0:
            logger.info(f"Knowledge base deleted from local storage: {kbid}")
        else:
            logger.error(f"Failed to delete knowledge base from local storage: {kbid}")
            return {"status": "error", "message": "Failed to delete from local storage"}
        
        message = "Knowledge base successfully deleted from local storage"
        if cloud_id:
            message = "Knowledge base successfully deleted from both local and cloud storage"

        if kb_info["type"] == "codebase":
            print(f"inside kb_info codebase type")
            print(f"kb_info: {json.dumps(kb_info, indent=2)}")
            delete_kb_path(kb_info.get("metadata", {}).get("path", ""))

        return {
            "status": "success",
            "message": message,
            "kbid": kbid
        }

    except Exception as e:
        logger.error(f"Error deleting knowledge base {kbid}: {e}")
        return {"status": "error", "message": f"Error deleting knowledge base: {str(e)}"}