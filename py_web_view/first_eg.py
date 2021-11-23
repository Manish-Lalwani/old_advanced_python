import webview
import time


def reload(window):
	while True:
		time.sleep(10)
		print('reloading')
		window.load_url('http://127.0.0.1:8000/crud_operation_app/list/')



#window = webview.create_window('Woah dude!', 'https://pywebview.flowrl.com')
#window = webview.create_window('Impersonator UI', '/home/xyz/projects/impersonator/files/index.html')
window = webview.create_window('Impersonator UI','http://127.0.0.1:8000/crud_operation_app/loader/',minimized=True)
#webview.start(reload,window,http_server=True)
webview.start(window,http_server=True)