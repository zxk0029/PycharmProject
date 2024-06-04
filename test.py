from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 解析请求的URL
        url = self.path
        print(f"Forwarding request to {url}")

        # 使用requests库发送请求
        response = requests.get(url, stream=True)

        # 将请求头转发给客户端
        self.send_response(response.status_code)
        for header, value in response.headers.items():
            self.send_header(header, value)
        self.end_headers()

        # 转发内容
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                self.wfile.write(chunk)

    def log_message(self, format, *args):
        # 禁用日志记录
        return

def run(server_class=HTTPServer, handler_class=ProxyHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
