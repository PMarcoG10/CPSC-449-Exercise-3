import redis

# Connect to the Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Assuming your Sorted Set is named 'leaderboard'
players = 'players'

# Retrieve the top 5 users
top_users = redis_client.zrevrange(players, 0, 4, withscores=True)

# Print the top 5 users
print("Top 5 Users on the Leaderboard:")
for rank, (user, score) in enumerate(top_users, start=1):
    print(f"{rank}. User: {user}, Score: {score}")