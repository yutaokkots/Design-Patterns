# Chain of Responsibility

Decouple the senders and receivers by giving multiple objects a chance to handle a request. 

Chain the receiving objects, and pass the request along the chain, until an object can handle it. 
```
┌───────────┐       ┌───────────┐ 
│Req. Sender├──//──>│Receiver   │
└───────────┘       └───────────┘
```

Decouple the sender and receiver:

```
┌───────────┐        
│Req. Sender├───┐
└───────────┘   │       * no need to know the
    ┌───────────┘           chain's structure or
    │   ┌───────────┐       keep track of references
    └─> │Handler    │       to its members
        └─────┬─────┘
    ┌─────────┘         * allows adding or removing
    │   ┌───────────┐       responsibilities
    └─> │Handler    │       dynamically
        └─────┬─────┘
    ┌─────────┘  
    │   ┌───────────┐
    └─> │Handler    │
        └─────┬─────┘
    ┌ ─ ─ ─ ─ ┘  
    │   ┌ ─ ─ ─ ─ ─ ┐
    └─> │Handler... │
        └ ─ ─ ┬ ─ ─ ┘
              │     ┌───────────┐
              └───> │Receiver   │
                    └───────────┘
```

"Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. 
Chain the receiving objects and pass the request along the chain until an object handles it. 
There is a potentially <u>variable number of "handler" objects</u> and a <u>stream of requests that must be handled</u>."

"Do not use Chain of Responsibility when each request is only handled by one handler, 
or, when the client object knows which service object should handle the request."<sup>[1]</sup>

## **UML diagram for Chain of Responsibility pattern**

```       
                                            successor
┌───────────┐           ┌───────────────┐<>──────┐
│Client     ├─────────> │AbstractHandler├────────┘
└───────────┘           ├───────────────┤
                        │HandleRequest()│
                        └───────┬───────┘
                                △
                    ┌───────────┴───────┐
            ┌───────┴───────┐   ┌───────┴───────┐
            │ConcrHandler1  │   │ConcrHandler2  │
            ├───────────────┤   ├───────────────┤
            │HandleRequest()│   │HandleRequest()│
            └───────────────┘   └───────────────┘   
```
## **Benefits**

* Single Responsibility Principle

* Open/Closed Principle

## **Comparisons with other design patterns**

The chain-of-responsibility pattern is structurally nearly identical to the decorator pattern, the difference being that for the decorator, all classes handle the request, while for the chain of responsibility, exactly one of the classes in the chain handles the request. 

## **Conceptual Examples**

* vending machine coin slot - a single slot accepts all coins, and each coin is routed to the appropriate storage area. <sup>[2]</sup>

* HTTP request processor (see example below)

## **Example of an HTTP request Processor** 

The following is an example that implements the Chain of Responsibility pattern for processing an HTTP request. <sup>[3]</sup>

```       
                                            successor
┌───────────┐           ┌───────────────┐<>──────┐
│Client     ├─────────> │AbstractHandler├────────┘
└───────────┘           ├───────────────┤
                        │HandleRequest()│
                        └────────┬──────┘
                                 △
                        ┌───┬───┬┴──┬───┐
                        │   │   │   │   │
                ┌───────┴───┼───┼┐  │   │
            ┌─> │Error404   │   ││  │   │   
            │   ├ ─ ┌───────┴───┼┴──┼┐  │  
            │   │han│DynmicHTML │   ││  │    
            │   └───├ ─ ┌───────┴───┼┴──┼┐                      
            │   ┌─> │han│APIcall    │   ││                       
            │   │   └───├ ─ ┌───────┴───┼┴──┐        
            │   │       │han│StaticFile │   │               
            │   │   ┌─> └───├ ─ ┌───────┴───┴───┐               
┌─────────────────────┐     │han│CorsReqHandler │               
│RequestProcessorChain│───> └───├───────────────┤         
├─────────────────────┤         │handleRequest()│
│ add()               │───┐     │addCorsHeader()│             
│ process()           │   └─>   └───────────────┘           
└─────────────────────┘    
```

The following defines the abstract base class for the Handler, AbstractRequestHandler. It contains an @abstractmethod called handle_request().

```
abstract_handler.py

"""Abstract Base class for Handler for Chain of Responsibility."""
from abc import ABC, abstractmethod

class AbstractRequestHandler(ABC):
    """AbstractHandler class for handling in chain."""
    
    @abstractmethod
    def handle_request(self, request, response):
        """HandleRequest function."""
        ...
```

The various concrete Handlers (or successors) are defined in the following:

```
handlers.py

"""Defines the Concrete message handlers."""
from abstract_handler import AbstractRequestHandler

class CorsRequestHandler(AbstractRequestHandler):
    """Concrete handler to handle Cors request."""
    def handle_request(self, request, response):
        print(f"{self.__class__.__name__} is handling this request.")
        self.add_cors_headers(response)

    def add_cors_headers(self, response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "x-requested-with"
        response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        print("CORS response headers added.")
        print(f"{response.headers = }")

class StaticFileRequestHandler(AbstractRequestHandler):
    """Concrete handler to handle static file request."""
    def handle_request(self, request, response):
        if request.data["request-type"] == "static-file":
            print(f"{self.__class__.__name__} is handling this request.")
            return True
        print(f"{self.__class__.__name__} is passing the request because no static-file found.")

class APICallRequestHandler(AbstractRequestHandler):
    """Concrete handler to handle API call request."""
    def handle_request(self, request, response):
        if request.data["request-type"] == "api-call":
            print(f"{self.__class__.__name__} is handling this request.")
            return True
        print(f"{self.__class__.__name__} is passing the request because no api-call found.")

class DynamicHTMLRequestHandler(AbstractRequestHandler):
    """Concrete handler to handle dynamic HTML request."""
    def handle_request(self, request, response):
        if request.data["request-type"] == "dynamic-html":
            print(f"{self.__class__.__name__} is handling this request.")
            return True
        print(f"{self.__class__.__name__} is passing the request because no dynamic-html found.")

class Error404RequestHandler(AbstractRequestHandler):
    """Concrete handler to handle Error 404 request."""
    def handle_request(self, request, response):
        print(f"{self.__class__.__name__} is handling this request.")
        return True
```

Additionally, and HttpRequest object and HttpResponse objects are defined by classes in the following:

```
http_reqres.py

"""HTTPRequest and HTTPResponse classes"""

class HttpRequest:
    def __init__(self, data):
        self.data = data

class HttpResponse:
    def __init__(self):
        self.headers = {}
```

A chain class that allows adding the Handlers to the program flow

```
req_processor_chain.py

"""Defines the Chain class that organizes the handlers."""
from typing import List
from http_reqres import HttpRequest, HttpResponse
from abstract_handler import AbstractRequestHandler

class RequestProcessorChain:
    """Chain class that handles the entire sequence of processes."""
    def __init__(self):
        self._handlers: List[AbstractRequestHandler] = []

    def add(self, handler):
        self._handlers.append(handler)

    def process(self, data={}):
        req = HttpRequest(data)
        res = HttpResponse()

        for handler in self._handlers:
            if handler.handle_request(req, res):
                break
```

And finally, the main.py file for running the file. 

```
"""Main.py file for handling the request_processor"""
from req_processor_chain import RequestProcessorChain
from handlers import CorsRequestHandler, StaticFileRequestHandler, APICallRequestHandler, DynamicHTMLRequestHandler, Error404RequestHandler

def main():
    request_processor = RequestProcessorChain()

    request_processor.add(CorsRequestHandler())
    request_processor.add(StaticFileRequestHandler())
    request_processor.add(APICallRequestHandler())
    request_processor.add(DynamicHTMLRequestHandler())
    request_processor.add(Error404RequestHandler())

    example_set_of_requests = ["static-file", "api-call", "dynamic-html", "amazon.com"]
    for idx, req_type in enumerate(example_set_of_requests):
        data = {
            "number": idx+1, 
            "request-type": req_type
            }
        print("Processing request with data " + str(data))
        request_processor.process(data)
        print("\n")

    """
        Processing request with data {'number': 1, 'request-type': 'static-file'}
        CorsRequestHandler is handling this request.
        CORS response headers added.
        response.headers = {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'x-requested-with', 'Access-Control-Allow-Methods': 'POST, GET, OPTIONS'}
        StaticFileRequestHandler is handling this request.


        Processing request with data {'number': 2, 'request-type': 'api-call'}
        CorsRequestHandler is handling this request.
        CORS response headers added.
        response.headers = {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'x-requested-with', 'Access-Control-Allow-Methods': 'POST, GET, OPTIONS'}
        StaticFileRequestHandler is passing the request because no static-file found.
        APICallRequestHandler is handling this request.


        Processing request with data {'number': 3, 'request-type': 'dynamic-html'}
        CorsRequestHandler is handling this request.
        CORS response headers added.
        response.headers = {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'x-requested-with', 'Access-Control-Allow-Methods': 'POST, GET, OPTIONS'}
        StaticFileRequestHandler is passing the request because no static-file found.
        APICallRequestHandler is passing the request because no api-call found.
        DynamicHTMLRequestHandler is handling this request.


        Processing request with data {'number': 4, 'request-type': 'amazon.com'}
        CorsRequestHandler is handling this request.
        CORS response headers added.
        response.headers = {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'x-requested-with', 'Access-Control-Allow-Methods': 'POST, GET, OPTIONS'}
        StaticFileRequestHandler is passing the request because no static-file found.
        APICallRequestHandler is passing the request because no api-call found.
        DynamicHTMLRequestHandler is passing the request because no dynamic-html found.
        Error404RequestHandler is handling this request.
    """

if __name__ == "__main__":
    main()
```

<hr/>

<sup>[1]</sup> "Chain Of Responsibility Pattern." Portland Pattern Repository. http://wiki.c2.com/?ChainOfResponsibilityPattern. July 8, 2014. Retrieved Dec. 30, 2023.

<sup>[2]</sup> Chain of Responsibility. Object Oriented Design. https://www.oodesign.com/chain-of-responsibility-pattern. Retrieved Dec. 30, 2023.

<sup>[3]</sup> Chain of Responsibility Design Pattern Python for Web Developers. Smart Coder Career. Adam Faryna https://smartcodercareer.com/blog/chain-of-responsibility-design-pattern-python-for-web-developers/. Retrieved Dec. 30, 2023.
