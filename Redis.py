#!/usr/bin/env python3
# Marco Gabriel
# Luis Alvarado
# CPSC 449
# 2023-11-01
# marcog10@csu.fullerton.edu
# @PMarcoG10
#
# Exercise 3
#
# Redis program to get top 5 players
#

"""This is how the program works"""

import redis

def main():
    """Main function to run the program"""
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

if __name__ == '__main__':
    main()
