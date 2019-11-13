import logging
import random

import grpc

from route_guide import route_guide_pb2, route_guide_resources, route_guide_pb2_grpc


def make_route_note(message, latitude, longitude):
    return route_guide_pb2.RouteNote(
        message=message,
        location=route_guide_pb2.Point(latitude=latitude, longitude=longitude),
    )


def guide_get_one_feature(stub, point):
    feature = stub.get_feature(point)
    if not feature.location:
        logging.warning('Server returned incomplete feature')
        return

    if feature.name:
        logging.info(f'Feature called {feature.name} at {feature.location}')
    else:
        logging.info(f'Found no feature at {feature.location}')


def guide_get_feature(stub):
    guide_get_one_feature(
        stub, route_guide_pb2.Point(latitude=409146138, longitude=-746188906)
    )
    guide_get_one_feature(stub, route_guide_pb2.Point(latitude=0, longitude=0))


def guide_list_features(stub):
    rectangle = route_guide_pb2.Rectangle(
        lo=route_guide_pb2.Point(latitude=400000000, longitude=-750000000),
        hi=route_guide_pb2.Point(latitude=420000000, longitude=-730000000),
    )
    print(f'Looking for features between 40, -75 and 42, -73')

    features = stub.list_features(rectangle)

    for feature in features:
        print(f'Feature called {feature.name} at {feature.location}')


def generate_route(feature_list):
    for _ in range(0, 10):
        random_feature = feature_list[random.randint(0, len(feature_list) - 1)]
        print(f'Visiting point {random_feature.location}')
        yield random_feature.location


def guide_record_route(stub):
    feature_list = route_guide_resources.read_route_guide_database()

    route_iterator = generate_route(feature_list)
    route_summary = stub.record_route(route_iterator)
    print("Finished trip with %s points " % route_summary.point_count)
    print("Passed %s features " % route_summary.feature_count)
    print("Travelled %s meters " % route_summary.distance)
    print("It took %s seconds " % route_summary.elapsed_time)


def generate_messages():
    messages = [
        make_route_note("First message", 0, 0),
        make_route_note("Second message", 0, 1),
        make_route_note("Third message", 1, 0),
        make_route_note("Fourth message", 0, 0),
        make_route_note("Fifth message", 1, 0),
    ]
    for msg in messages:
        print("Sending %s at %s" % (msg.message, msg.location))
        yield msg


def guide_route_chat(stub):
    responses = stub.route_chat(generate_messages())
    for response in responses:
        print(f'Received message {response.message} at {response.location}')


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)
        print('-------------- get_feature --------------')
        guide_get_feature(stub)
        print('-------------- get_features --------------')
        guide_list_features(stub)
        print('-------------- record_route --------------')
        guide_record_route(stub)
        print("-------------- route_chat --------------")
        guide_route_chat(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
