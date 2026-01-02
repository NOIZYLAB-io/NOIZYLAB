import keyring, os, dotenv

def lock_env():
    env=dotenv.dotenv_values(".env")
    for k,v in env.items():
        if "KEY" in k or "SECRET" in k:
            keyring.set_password("noizy.ai",k,v)
            print(f"🔒 stored {k}")

def unlock_env():
    import dotenv
    for k in dotenv.dotenv_values(".env").keys():
        if "KEY" in k or "SECRET" in k:
            os.environ[k]=keyring.get_password("noizy.ai",k) or ""