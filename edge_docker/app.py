import pandas as pd
import ast
import os
import redis
from lightgbm import LGBMClassifier

# if __name__ == '__main__':
#     with open("data/log_tiguan_27_mar_dac.txt") as f:
#         data = ast.literal_eval(f.read())

#     df = pd.DataFrame()
#     for data_value in data:
#         temp_df = pd.DataFrame(data_value[list(data_value)[0]]).sort_values(by="ts_millis:", ascending=True)["value"]
#         temp_df.rename(list(data_value)[0], inplace=True)
#         df = pd.concat([df, temp_df], axis = 1)

#     df.dropna(inplace=True)

#     df["class"] = 0
#     df.loc[:100, ["class"]] = 1
#     df.loc[:100, ["engine_load"]] = 100

#     model = LGBMClassifier()
#     model.fit(df.drop(columns=["class"]), df["class"])

#     redis_conn = redis.Redis(host='localhost', port=6379)
#     while True:
#         [[stream, [[number, parts]]]] = redis_conn.xread(streams={"v2x":"$"}, block=0)
#         keys = [p.decode('utf-8') for p in parts.keys()]
#         vals = [float(p.decode('utf-8')) for p in parts.values()]
#         d = pd.DataFrame(dict(zip(keys, vals)), index=[0])
#         d["predicted_class"] = model.predict(d.drop(columns=["car_id"]))[0]

if __name__ == '__main__':
    while True:
        pass
    