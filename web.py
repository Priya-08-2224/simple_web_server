from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<html>
<h1> Laptop Cofiguration(PRIYADHARSHINI-24901116) </h1>
<body>
<ol>
<li><b>Device name</b>	priyadharshini </li>

<li><b>Processor	12th Gen Intel(R) Core(TM) i3-1215U   1.20 GHz</li>

<li><b>Installed RAM</b>	16.0 GB (15.7 GB usable)</li>

<li><b>Device ID	5B17F122-2081-486E-9BD2-82F6E6AEF397</li>

<li><b>Product ID</b>	00342-42697-72556-AAOEM</li>

<li><b>System type</b>	64-bit operating system, x64-based processor</li>

<li><b><u>Pen and touch</b></u>	No pen or touch input is available for this display</li>
</ol>
</body>
</html>


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
