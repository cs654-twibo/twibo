import json
import logging
import time

from aiohttp import web

from db import tweet


logger = logging.getLogger(__name__)

routes = web.RouteTableDef()


@routes.post('/tweet/create')
async def create(request):
    data = await request.post()
    user_id = data['user_id']
    tweet_id = data['tweet_id']
    content = data['content']
    timestamp = data['ts']
    t1 = time.time()
    await tweet.create(user_id, tweet_id, content, timestamp)
    t2 = time.time()
    return web.json_response({
        'times': {
            'full': t2 - t1
        }
    })


@routes.get('/tweet/get')
async def get(request):
    query = request.rel_url.query
    user_id = query['user_id']
    limit = int(query.get('limit', 10))
    t1 = time.time()
    tweets = await tweet.get(user_id, limit)
    t2 = time.time()
    return web.json_response({
        'tweets': tweets,
        'times': {
            'full': t2 - t1
        }
    })
