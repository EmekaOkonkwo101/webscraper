from django.shortcuts import render
from scrapy import cmdline
from rest_framework import decorators, permissions, response, status
from django.http import JsonResponse
from scrapy import signals
from scrapy.crawler import CrawlerProcess
import asyncio
from scrapy.signalmanager import dispatcher
from webscraper.spiders.crawling_spider import CrawlingSpider
from django.views.decorators.csrf import csrf_exempt
from management.commands.run_scraper import Command as ScraperCommand
# @decorators.permission_classes((permissions.AllowAny,))
# @decorators.api_view(["POST"])
# scraper/views.py


def run_scraper(request):
    # Run the Scrapy spider
    ScraperCommand().handle()

    return response({'status': 'success', 'message': 'Scrapy spider executed'}, status=200)
# @csrf_exempt
# async def run_scraper(request):
    
#     # Define a function to handle spider completion
#     def spider_completed():
#         # This function will be called when the spider completes its crawling process
#         response_data = {
#             'status': 'Scrapy spider has completed crawling.'
#             # Add any other data you want to include in the response
#         }
#         return response(response_data, status=200)

#     # Start the Scrapy crawler
#     def start_crawler():
#         # Create a CrawlerRunner instance
#         runner = CrawlerProcess(settings={
#             'LOG_ENABLED': True  # Disable logging if needed
#         })

#         # Add a callback to handle spider completion
#         dispatcher.connect(spider_completed, signal=signals.spider_closed)

#         # Start the crawler with the spider
#         runner.crawl(CrawlingSpider)
        
#         asyncio.ensure_future(runner.start())
        
    
#     await asyncio.sleep(1000)
    
#     # Wait for the crawler to complete
#     start_crawler()

#     # Return a response
#     return response({'status': 'Running Scrapy spider.'}, status=200)




# from django.core.handlers.asgi import ASGIRequest
# from django.core.handlers.base import BaseHandler

# @csrf_exempt
# async def asgi_application(scope, receive, send):
#     request = ASGIRequest(scope)
#     handler = BaseHandler()
#     response = await handler.get_response_async(request, run_scraper)
#     await response(scope, receive, send)