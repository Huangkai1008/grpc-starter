""""""
import logging
import math
import time
from concurrent import futures

import grpc

from route_guide import (
    Point,
    route_guide_pb2_grpc,
    route_guide_resources,
    route_guide_pb2,
)


def get_feature(feature_db, point):
    for feature in feature_db:
        if feature.location == point:
            return feature
    return None


def get_distance(start: Point, end: Point) -> float:
    """获取两坐标之间的距离

    Args:
        start: 开始坐标
        end: 结束坐标

    """
    coord_factor = 10000000.0
    lat_1 = start.latitude / coord_factor
    lat_2 = end.latitude / coord_factor
    lon_1 = start.longitude / coord_factor
    lon_2 = end.longitude / coord_factor
    lat_rad_1 = math.radians(lat_1)
    lat_rad_2 = math.radians(lat_2)
    delta_lat_rad = math.radians(lat_2 - lat_1)
    delta_lon_rad = math.radians(lon_2 - lon_1)

    a = pow(math.sin(delta_lat_rad / 2), 2) + (
            math.cos(lat_rad_1) * math.cos(lat_rad_2) * pow(math.sin(delta_lon_rad / 2), 2)
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    r = 6371000  # 地球的平均半径
    return r * c


class RouteGuideServicer(route_guide_pb2_grpc.RouteGuideServicer):
    """导航服务器"""

    def __init__(self):
        self.db: list = route_guide_resources.read_route_guide_database()

    def get_feature(self, request, context):
        feature = get_feature(self.db, request)
        return feature or route_guide_pb2.Feature(name='', location=request)

    def list_features(self, request, context):
        left = min(request.lo.longitude, request.hi.longitude)
        right = max(request.lo.longitude, request.hi.longitude)
        top = max(request.lo.latitude, request.hi.latitude)
        bottom = min(request.lo.latitude, request.hi.latitude)
        for feature in self.db:
            if (
                    left <= feature.location.longitude <= right
                    and bottom <= feature.location.latitude <= top
            ):
                yield feature

    def record_route(self, request_iterator, context):
        point_count = 0
        feature_count = 0
        distance = 0.0
        prev_point = None

        start_time = time.perf_counter()
        for point in request_iterator:
            point_count += 1
            if get_feature(self.db, point):
                feature_count += 1
            if prev_point:
                distance += get_distance(prev_point, point)
            prev_point = point

        elapsed_time = time.perf_counter() - start_time
        return route_guide_pb2.RouteSummary(
            point_count=point_count,
            feature_count=feature_count,
            distance=int(distance),
            elapsed_time=int(elapsed_time),
        )

    def route_chat(self, request_iterator, context):
        prev_notes = []
        for new_note in request_iterator:
            for prev_note in prev_notes:
                if prev_note.location == new_note.location:
                    yield prev_note
            prev_notes.append(new_note)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    route_guide_pb2_grpc.add_RouteGuideServicer_to_server(
        RouteGuideServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    logging.info('RPC Server Start ...')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
