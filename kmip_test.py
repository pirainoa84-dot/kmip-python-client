import ssl
from kmip.pie.client import ProxyKmipClient
from kmip import enums


# CONFIG

CTM_HOST = "kmip.ciphertrustmanager.local"
CTM_PORT = 5696

CA_FILE = "/opt/kmip/ca/ctm_ca.pem"
CERT_FILE = "/opt/kmip/tenant_a/client.pem"
KEY_FILE = "/opt/kmip/tenant_a/client.key"


_original_wrap_socket = ssl.wrap_socket

def patched_wrap_socket(sock, *args, **kwargs):
  
    kwargs.pop("keyfile", None)
    kwargs.pop("certfile", None)
    kwargs.pop("ca_certs", None)
    kwargs.pop("cert_reqs", None)
    kwargs.pop("ssl_version", None)

  
    server_hostname = kwargs.get("server_hostname", CTM_HOST)
    context = ssl.create_default_context(cafile=CA_FILE)

    
    context.load_cert_chain(
        certfile=CERT_FILE,
        keyfile=KEY_FILE
    )

    
    context.check_hostname = False
    context.verify_mode = ssl.CERT_REQUIRED

    return context.wrap_socket(sock, server_hostname=server_hostname)


ssl.wrap_socket = patched_wrap_socket

# TEST KMIP

def run():
    print("\n=== KMIP TEST ===")

    client = ProxyKmipClient(
        hostname=CTM_HOST,
        port=CTM_PORT,
        cert=CERT_FILE,
        key=KEY_FILE,
        ca=CA_FILE
    )

    with client:
        print("[OK] Connessione stabilita")

        key_id = client.create(
            enums.CryptographicAlgorithm.AES,
            256
        )
        print("[OK] Key created:", key_id)

        key = client.get(key_id)
        print("[OK] Key retrieved:", key.unique_identifier)

# MAIN

if __name__ == "__main__":
    run()
