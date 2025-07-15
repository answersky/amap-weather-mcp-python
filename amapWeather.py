from mcp.server.fastmcp import FastMCP
import requests
from cityCode import getCityCode
import os

"""
客户端本地调用的配置
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "D:\\code\\mcp-server-python",
        "run",
        "amapWeather.py"
      ],
      "env": {
        "AMAP_MAPS_API_KEY": "api_key"
      }
    }
  }
}
"""

mcp = FastMCP("amap weather")

def get_weather(city_code):
    # 通过环境变量来获取
    AMAP_MAPS_API_KEY=os.getenv("AMAP_MAPS_API_KEY")
    url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={city_code}&key={AMAP_MAPS_API_KEY}&extensions=all"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        # 返回响应，确保它是JSON格式
        return {"error": f"Request failed:"}

# 获取天气信息的工具
@mcp.tool()
def get_city_weather(city):
    """获取指定城市的天气信息。

    参数:
    city (str): 城市名称

    返回:
    str: 天气信息描述
    """
    city_code=getCityCode(city)
    city_weather_info = get_weather(city_code)
    return city_weather_info

if __name__ == "__main__":
    # get_city_weather('北京')
    mcp.run(transport='stdio')