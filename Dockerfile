# Dockerfile for NOIZYLAB Tailscale Infrastructure
# This container provides a complete Tailscale setup environment

FROM ubuntu:22.04

# Avoid interactive prompts during build
ENV DEBIAN_FRONTEND=noninteractive
ENV TAILSCALE_VERSION=latest

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    iptables \
    iproute2 \
    gnupg \
    lsb-release \
    jq \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Install Tailscale
RUN curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/jammy.gpg | \
    tee /usr/share/keyrings/tailscale-archive-keyring.gpg >/dev/null && \
    curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/jammy.list | \
    tee /etc/apt/sources.list.d/tailscale.list && \
    apt-get update && \
    apt-get install -y tailscale && \
    rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /noizylab

# Copy NOIZYLAB scripts and configuration
COPY scripts/ /noizylab/scripts/
COPY config/ /noizylab/config/
COPY CODE_MASTER/ /noizylab/CODE_MASTER/
COPY README.md /noizylab/

# Make scripts executable
RUN chmod +x /noizylab/scripts/*.sh

# Create entrypoint script
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
# Start tailscaled in background\n\
/usr/sbin/tailscaled --tun=userspace-networking --socks5-server=localhost:1055 &\n\
\n\
# Wait for tailscaled to start\n\
sleep 2\n\
\n\
# If TAILSCALE_AUTH_KEY is provided, use it for unattended setup\n\
if [ -n "$TAILSCALE_AUTH_KEY" ]; then\n\
    echo "Authenticating with auth key..."\n\
    tailscale up --authkey="$TAILSCALE_AUTH_KEY" --hostname="${TAILSCALE_HOSTNAME:-noizylab-container}"\n\
else\n\
    echo "No auth key provided. Run: tailscale up"\n\
    echo "Visit the URL provided to authenticate"\n\
fi\n\
\n\
# Run health check if connected\n\
if tailscale status &> /dev/null; then\n\
    echo "Running health check..."\n\
    /noizylab/scripts/healthcheck-tailscale.sh\n\
fi\n\
\n\
# Execute command if provided, otherwise start shell\n\
if [ $# -gt 0 ]; then\n\
    exec "$@"\n\
else\n\
    exec /bin/bash\n\
fi\n\
' > /entrypoint.sh && chmod +x /entrypoint.sh

# Expose Tailscale socks proxy port
EXPOSE 1055

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Default command
CMD ["/bin/bash"]

# Labels
LABEL org.opencontainers.image.title="NOIZYLAB Tailscale Infrastructure"
LABEL org.opencontainers.image.description="Complete Tailscale setup for NOIZYLAB infrastructure"
LABEL org.opencontainers.image.vendor="NOIZYLAB"
LABEL org.opencontainers.image.source="https://github.com/NOIZYLAB-io/NOIZYLAB"
