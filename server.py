import http.server
import socketserver

# 指定伺服器的埠號
port = 8080

# 建立一個簡單的伺服器
Handler = http.server.SimpleHTTPRequestHandler

# 啟動伺服器
with socketserver.TCPServer(("", port), Handler) as httpd:
    print(f"Serving at http://localhost:{port}")
    # 常駐運行
    httpd.serve_forever()