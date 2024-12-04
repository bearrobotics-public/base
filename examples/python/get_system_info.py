import grpc
from bearrobotics.api.v0.robot import robot_api_service_pb2_grpc
from bearrobotics.api.v0.robot import robot_api_service_pb2

ROBOT_IP = "10.10.127.2"
ROBOT_API_SERVER_PORT = 5123


def run():
    print("Getting system info...")
    with grpc.insecure_channel(
            f"{ROBOT_IP}:{ROBOT_API_SERVER_PORT}") as channel:
        stub = robot_api_service_pb2_grpc.RobotAPIServiceStub(channel)
        response = stub.GetSystemInfo(
            robot_api_service_pb2.GetSystemInfoRequest())
    print("Received: ", response)


if __name__ == "__main__":
    run()
