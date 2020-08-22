import pandas as pd
import pyarrow as pa
# pip3 install pandas pyarrow redis
import redis
# 方式一
df = pd.DataFrame({'A': [1, 2, 3]})
r = redis.Redis(host='localhost', port=6379, db=0)

context = pa.default_serialization_context()
r.set("key", context.serialize(df).to_buffer().to_pybytes())
df = context.deserialize(r.get("key"))

# 方式二 通过pickle序列化的方式
import pandas as pd
import pickle
import redis

rs = redis.StrictRedis(host='127.0.0.1')

df = pd.DataFrame([range(5)] * 5, index=list('HELLO'), columns=list('HELLO'))

df_bytes = pickle.dumps(df)
rs.set('test_df', df_bytes)

df_bytes_from_redis = rs.get('test_df')
df_from_redis = pickle.loads(df_bytes_from_redis)
print(df_from_redis)

# 方式三 通过df.to_msgpack的方式
import pandas as pd
import pickle
import redis

rs = redis.StrictRedis(host='127.0.0.1')

df = pd.DataFrame([range(5)] * 5, index=list('HELLO'), columns=list('HELLO'))

df_bytes = df.to_msgpack()
rs.set('test_df', df_bytes)

df_bytes_from_redis = rs.get('test_df')
df_from_redis = pd.read_msgpack(df_bytes_from_redis)
print(df_from_redis)
