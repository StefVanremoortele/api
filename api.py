from __future__ import print_function
from flask import Flask

import logging

import grpc
import public_search_pb2
import public_search_pb2_grpc

app = Flask(__name__)


def test_grpc():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = public_search_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(public_search_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)

@app.route("/")
def hello_world():
    test_grpc()
    return "Hello, World!"