import pandas as pd
from kafka import KafkaProducer, KafkaConsumer 
from time import sleep
from json import dumps
import json

producer = KafkaProducer(bootstrap_servers='44.202.33.47:9092',
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


df = pd.read_csv("indexProcessed.csv")


while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('testing2', value=dict_stock)
    sleep(1)

producer.flush()

