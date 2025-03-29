import redis

redis_conn = redis.Redis(host="localhost", port=6379, db=0)

# para insert e update
redis_conn.set("chave_1", "trocando meu valor")

# select
meu_valor = redis_conn.get("chave_1").decode("utf-8")

# delete de dados
redis_conn.delete("chave_1")

### comandos para hash
meu_hash = { # chave de exemplo
    "nome": "joao", # field: values
    "idade": 30,
    "cidade": "sao paulo"
}
redis_conn.hset("meu_hash", "nome", "joao")
redis_conn.hset("meu_hash", "idade", "30")
redis_conn.hset("meu_hash", "cidade", "sao paulo")

valor_1 = redis_conn.hget("meu_hash", "nome").decode("utf-8")

redis_conn.hdel("meu_hash", "cidade")

## buscas por existencia
elem = redis_conn.exists("chave_1")
print(elem)

elem2 = redis_conn.hexists("meu_hash", "nome")
print(elem2)