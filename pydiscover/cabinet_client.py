from pydiscover import client


if __name__ == "__main__":
    try:
        response, server = client.discover(magic="magic_word",
                                    port=40000,
                                    password="password",
                                    timeout=10)

        print("Discovered server: '%s - Response: \"%s\"" % (server, str(response)))
    except Exception as e:
        print(e)