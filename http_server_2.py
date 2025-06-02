#!/usr/bin/env python3
"""
Simple HTTP server for Chroma MCP.
Uses the MCP HTTP server package directly.
"""

import os
import sys
import argparse
import asyncio
from pathlib import Path

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Import the Chroma MCP module
import chroma_mcp.server

# Parse command line arguments
parser = argparse.ArgumentParser(description='Start Chroma MCP server with HTTP transport')
parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to bind to')
parser.add_argument('--port', type=int, default=8080, help='Port to bind to')
args = parser.parse_args()

# Initialize Chroma client
chroma_parser = chroma_mcp.server.create_parser()
chroma_args = chroma_parser.parse_args()
chroma_mcp.server.get_chroma_client(chroma_args)

# Get the MCP instance
mcp = chroma_mcp.server.mcp

# Define async run function
async def run_server():
    # Import server module from MCP
    from mcp.server.http import serve_http
    
    print(f"Starting Chroma MCP HTTP server on {args.host}:{args.port}")
    await serve_http(
        mcp._app,
        host=args.host,
        port=args.port
    )

# Run the server
if __name__ == "__main__":
    asyncio.run(run_server())