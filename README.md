## 高德地图天气预报
    该高德地图天气预报 MCP Server 发布在 PyPI。

## 提供接口类型
    提供了标准的studio协议
    
## MCP 工具列表
### 未来天气预报服务
    get_city_weather
    获取指定城市的天气信息。

    参数:
    city (str): 城市名称

    返回:
    str: 天气信息描述

## 本地运行
###  从github上拉取源码，安装依赖
    pip install uv
    uv add mcp[cli]
    1.先测试是否能运行 uv run --with mcp mcp run amapWeather.py
    2.开启MCP Inspector进行mcp 服务调试
        mcp dev mcpServer.py
