import redis

# connect to Redis server
r = redis.Redis(host='localhost', port=6379)

# sample product dictionary
product = {
    'id': 'basketball',
    'quantity': '15',
    'price': '19.99',
}

def product_update(redis_client, product):

    with redis_client.pipeline() as pipe:

        # use hincrby to increment the quantity field
        pipe.hincrby(product["id"], 'quantity', 50)

        # use hset to set the new price for the product
        pipe.hset(product["id"], 'price', 29.99)

        # execute the pipeline
        pipe.execute()

# result
updated_quantity = r.hget(product['id'],'quantity').decode('utf8')
updated_price = r.hget(product['id'],'price').decode('utf8')

print(f"Updated Quantity: {updated_quantity}")
print(f"Updated Price: {updated_price}")

