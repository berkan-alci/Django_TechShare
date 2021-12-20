import redis
import json
import os

rds = redis.StrictRedis(port = os.environ.get('REDIS_PORT'), db=0)

class Redis:
    def set(cache_key, data):
        data = json.dumps(data)
        rds.set(cache_key, data)

        return True
    
    def get(cache_key):
        data = rds.get(cache_key)
       
        if not data:
            return None
        
        data = data.decode("utf-8")
        data = json.loads(data)
        
        return data