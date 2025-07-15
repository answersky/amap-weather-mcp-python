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
## langchain4j mcp 客户端调用本地mcp服务调试方式
### 客户端代码
    下面代码中的D:\\code\\mcp-server-python  更换成自己从git拉取下来后的代码位置
     @Bean
    public OpenAiMcp openAiMcp(@Qualifier(value = "openAiChatModel") ChatModel chatModel){
        // 构建用于启动本地 Python MCP 服务的命令
        List<String> command = List.of(
                "cmd", "/c",
                "cd /d D:\\code\\mcp-server-python && " +
                        "C:\\Users\\duan\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\uv.exe run --with mcp mcp run amapWeather.py"
        );
        McpTransport transport = new StdioMcpTransport.Builder()
                  //调用本地mcp服务
                 .command(command)
                .environment(Map.of("AMAP_MAPS_API_KEY","高德apikey"))
                .logEvents(true) // 仅当你想在日志中查看流量时
                .build();

        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();


        ToolProvider toolProvider = McpToolProvider.builder()
                .mcpClients(List.of(mcpClient))
                .build();

        return AiServices.builder(OpenAiMcp.class)
                .chatModel(chatModel)
                .toolProvider(toolProvider)
                //按照memoryId（实际就是对应的用户id）对应创建一个chatmemory,放入100条历史记录
                .chatMemoryProvider(memoryId->MessageWindowChatMemory.withMaxMessages(100))
                .build();
    }
