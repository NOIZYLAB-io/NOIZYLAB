export SWIFTLY_HOME_DIR="/Users/rsp_ms/.swiftly"
export SWIFTLY_BIN_DIR="/Users/rsp_ms/.swiftly/bin"
export SWIFTLY_TOOLCHAINS_DIR="/Users/rsp_ms/Library/Developer/Toolchains"
if [[ ":$PATH:" != *":$SWIFTLY_BIN_DIR:"* ]]; then
    export PATH="$SWIFTLY_BIN_DIR:$PATH"
fi
