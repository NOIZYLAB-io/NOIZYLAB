import httpx
from BASE.services.knowledge_bases import list_all_knowledge_bases
from logger.log import logger
import constants
from ipc import IPC
import time

ipc_ = IPC.connect()


@logger.catch()
def determine_sync_status(kb_dict: dict) -> dict:
    """Determine cloud synchronization status for a knowledge base."""
    cloud_id = kb_dict.get("cloud_id")
    source = kb_dict.get("source", "").upper()

    if source == "REMOTE":
        return {
            "sync_status": "synced",
            "can_upload": False,
            "can_sync": False,
            "cloud_sync_available": True,
        }

    if not cloud_id:
        return {
            "sync_status": "upload_needed",
            "can_upload": True,
            "can_sync": False,
            "cloud_sync_available": True,
        }
    else:
        return {
            "sync_status": "sync_available",
            "can_upload": False,
            "can_sync": True,
            "cloud_sync_available": True,
        }


@logger.catch()
async def fetch_cloud_knowledge_bases() -> list:
    """Fetch knowledge bases from cloud API."""

    session = ipc_.get("current_session") if ipc_.get("current_session") else None

    if not session:
        logger.error("No session provided for cloud KB fetch")
        return []

    try:
        async with httpx.AsyncClient(verify=constants.SSL_CONTEXT) as client:
            response = await client.get(
                f"{constants.codebase}/cloud_sync/collections/test",
                headers={"x-session": session},
            )
            logger.info(f"Response: {response.json()}")
        if response.status_code != 200:
            logger.error(f"Cloud KB request failed with status {response.status_code}")
            return []

        response_data = response.json()

        # Handle both legacy and new API response formats
        if "knowledge_bases" in response_data:
            knowledge_bases = response_data["knowledge_bases"]
        else:
            personal_kbs = response_data.get("personal", [])
            for kb in personal_kbs:
                kb["scope"] = "personal"
            shared_kbs = response_data.get("shared", [])
            print("SHARED KBS:", shared_kbs)
            for kb in shared_kbs:
                kb["scope"] = "organization"
            knowledge_bases = personal_kbs + shared_kbs

        # Convert cloud KBs to local format
        cloud_kbs = []
        for kb in knowledge_bases:
            cloud_kb = {
                **kb,
                "id": kb.get("uuid", ""),
                "cloud_id": kb.get("uuid", ""),
                "name": kb.get("name", "Unknown"),
                "description": kb.get("description", ""),
                "type": kb.get("type", "codebase"),
                "source": "REMOTE",
                "status": "ready",
                "isAutoIndexed": False,
                "scope": kb.get("scope", "personal"),
                "syncConfig": {"enabled": True, "lastSynced": time.time() * 1000},
                "metadata": kb.get("metadata", {}),
            }

            cloud_kbs.append(cloud_kb)

        logger.info(f"Retrieved {len(cloud_kbs)} knowledge bases from cloud")
        return cloud_kbs

    except Exception as e:
        logger.error(f"Error fetching cloud knowledge bases: {e}")
        return []


@logger.catch()
async def list_knowledge_bases(include_cloud: bool = False):
    """
    List all knowledge bases with optional cloud integration.

    Args:
        include_cloud: Whether to fetch and include cloud knowledge bases
        session: Session token for cloud API authentication

    Returns:
        Dictionary with list of knowledge bases and status
    """
    logger.info(
        f"Processing knowledge base list request (include_cloud: {include_cloud})"
    )

    try:
        # Get local knowledge bases from the database
        local_kbs = list_all_knowledge_bases()
        logger.info(f"Found {len(local_kbs)} local knowledge bases")

        # Enhance local KBs with sync status
        enhanced_local_kbs = []
        for kb in local_kbs:
            sync_info = determine_sync_status(kb)
            enhanced_kb = kb.copy()
            enhanced_kb.update(sync_info)
            enhanced_local_kbs.append(enhanced_kb)

        # Initialize combined list with local KBs
        combined_kbs = enhanced_local_kbs
        cloud_count = 0

        # Fetch cloud KBs if requested
        if include_cloud:
            try:
                cloud_kbs = await fetch_cloud_knowledge_bases()
                cloud_count = len(cloud_kbs)

                # Enhance cloud KBs with sync status
                enhanced_cloud_kbs = []
                for kb in cloud_kbs:
                    sync_info = determine_sync_status(kb)
                    enhanced_kb = kb.copy()
                    enhanced_kb.update(sync_info)
                    enhanced_cloud_kbs.append(enhanced_kb)

                # Combine local and cloud KBs (avoiding duplicates by cloud_id)
                local_cloud_ids = {
                    kb.get("cloud_id")
                    for kb in enhanced_local_kbs
                    if kb.get("cloud_id")
                }

                for cloud_kb in enhanced_cloud_kbs:
                    cloud_id = cloud_kb.get("cloud_id")
                    if cloud_id not in local_cloud_ids:
                        combined_kbs.append(cloud_kb)

                logger.info(
                    f"Added {len(enhanced_cloud_kbs)} cloud KBs, {len(combined_kbs) - len(enhanced_local_kbs)} unique"
                )

            except Exception as e:
                logger.error(f"Error fetching cloud knowledge bases: {e}")
                # Continue with local KBs only

        total_count = len(combined_kbs)

        if total_count == 0:
            return []

        return combined_kbs

    except Exception as e:
        logger.error(f"Error listing knowledge bases: {e}")
        return []
