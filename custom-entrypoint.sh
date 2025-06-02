#!/bin/bash
# Custom entrypoint script to run chroma-mcp server with MCP transport

# Install additional package for HTTP transport
pip install fastapi uvicorn

# Start the MCP server with HTTP transport
python -m mcp.server.http --port 8080 -- chroma-mcp