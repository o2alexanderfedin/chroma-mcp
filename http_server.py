#!/usr/bin/env python3
"""
HTTP server wrapper for Chroma MCP.
This script starts a Chroma MCP server with HTTP transport.
"""

import asyncio
import argparse
import importlib.util
import sys
import os
from pathlib import Path

# Parse command line arguments
parser = argparse.ArgumentParser(description='Start Chroma MCP server with HTTP transport')
parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to bind to')
parser.add_argument('--port', type=int, default=8080, help='Port to bind to')
args = parser.parse_args()

# Import the FastMCP instance from the chroma_mcp module
spec = importlib.util.spec_from_file_location(
    "chroma_mcp",
    Path(__file__).parent / "src" / "chroma_mcp" / "server.py"
)
server_module = importlib.util.module_from_spec(spec)
sys.modules["chroma_mcp"] = server_module
spec.loader.exec_module(server_module)

# Get the FastMCP instance
mcp = server_module.mcp

# Initialize the client if needed
parser = server_module.create_parser()
args_for_client = parser.parse_args([])  # Parse an empty list to get default values
server_module.get_chroma_client(args_for_client)  # Initialize the client

# Run the server with HTTP transport
print(f"Starting Chroma MCP server with HTTP transport on {args.host}:{args.port}")
asyncio.run(mcp.run_server(host=args.host, port=args.port))