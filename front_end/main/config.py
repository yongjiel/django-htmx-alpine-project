import os

class Config:
    PROTOCOL = os.environ.get('PROTOCOL', None) or 'http'
    BACKENDPORT = os.environ.get('BACKENDPORT', None) or '8001'
    BACKENDHOST =   os.environ.get('BACKENDHOST', None) or '127.0.0.1'
    BACK_END_HOST = f"{PROTOCOL}://{BACKENDHOST}:{BACKENDPORT}"  # if necessary, update it with your host
                                    # and port
    
    FRONTENDPORT = os.environ.get('FRONTENDPORT', None) or '8002'
    FRONTENDHOST =   os.environ.get('FRONTENDHOST', None) or '127.0.0.1'
    FRONT_END_HOSTS = [f"{PROTOCOL}://{FRONTENDHOST}:{FRONTENDPORT}"]

