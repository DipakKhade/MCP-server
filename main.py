from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def myname()->str:
    return "My name is Dipak R Khade"



if __name__ == "__main__":
    try:
        mcp.run()
    except KeyboardInterrupt:
        print("Exiting")
    