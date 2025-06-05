from fastmcp import Client
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
async def main():
    # Connect via stdio to a local script
    async with Client("fastmcp_server.py") as client:
        tools = await client.list_tools()
        #print(f"Available tools: {tools}")
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print(f"Available tools: {tools}")
        print(f"Result: {result[0].text}")
        #print(f"Result: {result.text}")

    # # Connect via SSE
    # async with Client("http://localhost:8000/sse") as client:
    #     # ... use the client
    #     client.call_tool("add", {"a": 5, "b": 3})
    #     print("Connected to SSE server")

if __name__ == "__main__":  
    import asyncio
    asyncio.run(main())
# This code connects to a FastMCP server, lists available tools, and calls a tool.