from mcp.server.fastmcp import FastMCP



mcp = FastMCP("测试MCP For Python")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a+b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# if __name__ == "__main__":
#     print("Hello from mcp-server-python!")
#     mcp.run(transport='stdio')
