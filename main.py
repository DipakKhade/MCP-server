from fastmcp import FastMCP
import os
from typing import List

mcp = FastMCP("assistance")

@mcp.tool()
def totalProjects()->List[str]:
    return os.listdir('/Users/dipakkhade/projects') 

if __name__ == "__main__":
    try:
        print('starting MCP Server...')
        mcp.run()
    except KeyboardInterrupt:
        print("Exiting")
    
