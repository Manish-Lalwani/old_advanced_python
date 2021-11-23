from pydiscover import server
"""
IN pydiscover 
Server sends data
Client recieve data
"""

#server will send required details to cabinet cclient
#will recieve ip address so has to also act as an client
if __name__ == "__main__":
    
    server.server_discover(answer='example.cfg',
                        magic='magic_word',
                        listen_ip='0.0.0.0',
                        port=40000,
                        password='password',
                        disable_hidden=True)


