from vulnbid import app


if not app.config['DEBUG']:
    addr = '0.0.0.0'
    port = 8080
else:
    addr = '127.0.0.1'
    port = 5000

if __name__ == '__main__':
    app.run(addr, port)
