import ssl
def client_ssl_context(cert_path, key_path, ca_path):
    ctx = ssl.create_default_context(cafile=ca_path)
    ctx.load_cert_chain(certfile=cert_path, keyfile=key_path)
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_REQUIRED
    return ctx
