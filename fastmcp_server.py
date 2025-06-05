from fastmcp import FastMCP
# Create an MCP server
mcp = FastMCP("Demo 🚀")
# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
if __name__ == "__main__":
    # Start the server
    #mcp.run(host="localhost", port=6274)
    mcp.run()
    print("MCP server is running on http://localhost:6274")