---
applyTo: '{_SCRIPT_FILE_IDENTIFIER}'
---

## Instructions

**Important**:
Do refer to these below mentioned files:
{_REFERENCE_FILES_}

**Context:**
This JSON object represents the HTTP request structure. The `request` key in the JSON can be used for both pre-request and post-response script, whereas `response` key in the JSON will be used in post-response script. The pre-request script instructions file will use this `request` JSON to create appropriate pre-request scripts. The post-response script instructions file will use both `request` JSON and `response` JSON to create appropriate post-response scripts.

**Request JSON:**
{_JSON_DATA_}
