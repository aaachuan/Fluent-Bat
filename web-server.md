### web-server

#### simple C/S example

执行命令打开HTTP服务监听8000端口：
```
C:\Users\Administrator\Python\Fluent-Bat\Scripts\web-server>python -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```
这时马上用浏览器访问localhost:8000显示资源文件：
```
Directory listing for /
requestest.py
server.py
```
使用chrome devtools请求详情：
General
```
Request URL: http://localhost:8000/
Request Method: GET
Status Code: 200 OK (from disk cache)
Remote Address: 127.0.0.1:8000
Referrer Policy: no-referrer-when-downgrade
```
Response Headers(View source)
```
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.7.4
Date: Mon, 07 Oct 2019 13:53:48 GMT
Content-type: text/html; charset=utf-8
Content-Length: 391
```

[Inspect Network Activity In Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/network)

服务端：
```
127.0.0.1 - - [07/Oct/2019 21:47:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [07/Oct/2019 21:49:45] "GET /requestest.py HTTP/1.1" 304 -
127.0.0.1 - - [07/Oct/2019 21:49:52] "GET /server.py HTTP/1.1" 304 -
127.0.0.1 - - [07/Oct/2019 21:50:24] "GET / HTTP/1.1" 200 -
```
过程中每次刷新请求服务端会输出如`127.0.0.1 - - [07/Oct/2019 21:50:24] "GET / HTTP/1.1" 200 -`，但是对于已加载的文件`/requestest.py`和`/server.py`
加入到cache而不再输出类似的请求。

当然，也可以编写程序来对服务发起HTTP请求：
```
import requests
r = requests.get('http://127.0.0.1:8000/')
print(r)
```
```
<Response [200]>
```
可以使用tcpdump监听本地网卡tcp连接进一步查看详情，windows有 LBNL's Network Research Group在UNIX系统上开发的tcpdump基础上，
二次开发的Microolap TCPDUMP for Windows，几乎和类UNIX系统上的一模一样。

[Command-line sniffer (packet capture tool) for Windows](http://www.microolap.com/products/network/tcpdump/)

```
C:\Users\Administrator\Python>tcpdump -D

********************************************************************
**                                                                **
**              Tcpdump v4.9.2 (September 03, 2017)               **
**                   http://www.tcpdump.org                       **
**                                                                **
** Tcpdump for Windows is built with Microolap Packet Sniffer SDK **
**              Microolap EtherSensor product family              **
**               >>> build 5072.01 June 10, 2019 <<<              **
**                                                                **
**        Copyright(c) 1997 - 2019 Microolap Technologies         **
**       http://microolap.com/products/network/ethersensor        **
**         http://microolap.com/products/network/tcpdump          **
**                                                                **
**                  XP/2003/Vista/2008/Win7/Win8                  **
**                 Win2012/Win10/Win2016/Win2019                  **
**               (UEFI and Secure Boot compatible)                **
**                                                                **
**                       Trial license.                           **
**                                                                **
********************************************************************

1.\Device\NdisWanBh (WAN Miniport (Network Monitor))
2.\Device\{28FFE6D3-45BC-44D5-9538-C24C545FBFD0} (Broadcom NetLink (TM) Fast Ethernet)
3.\Device\{31E2C8B0-7003-4991-B7A9-603E4BB2EC35} (Broadcom 802.11g 网络适配器)
```

[Socket With Python](https://gist.github.com/aaachuan)
