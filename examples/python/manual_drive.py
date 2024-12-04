import argparse
import grpc
import time

from bearrobotics.api.v0.robot import robot_api_service_pb2_grpc
from bearrobotics.api.v0.robot import robot_api_service_pb2
from bearrobotics.api.v0.common import math_pb2

DEFAULT_ROBOT_IP = "10.10.127.2"
DEFAULT_ROBOT_API_SERVER_PORT = 5123


def run(server_ip, linear_velocity, angular_velocity):
    """
    Sets up a gRPC connection and starts the streaming function.
    """
    with grpc.insecure_channel(server_ip) as channel:
        stub = robot_api_service_pb2_grpc.RobotAPIServiceStub(channel)
        print("Connected to robot.")

        def request_generator():
            while True:
                request = robot_api_service_pb2.DriveRobotRequest(
                    twist=math_pb2.Twist(linear_velocity=linear_velocity,
                                         angular_velocity=angular_velocity))
                print(
                    f"Sending: linear={linear_velocity}, angular={angular_velocity}"
                )
                yield request
                time.sleep(1 / 5)

        response_stream = stub.DriveRobot(request_generator())

        for response in response_stream:
            print(f"Received response: {response}")


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Send gRPC DriveRobotRequest stream at 5 Hz.")
    parser.add_argument("-l",
                        "--linear_velocity",
                        type=float,
                        default=0.0,
                        help="Linear velocity in meters per second (m/s).")
    parser.add_argument("-a",
                        "--angular_velocity",
                        type=float,
                        default=0.0,
                        help="Angular velocity in radians per second (rad/s).")

    parser.add_argument("--robot_ip",
                        type=str,
                        default=DEFAULT_ROBOT_IP,
                        help="Robot IP address.")
    parser.add_argument("--robot_port",
                        type=int,
                        default=DEFAULT_ROBOT_API_SERVER_PORT,
                        help="Robot API server port.")

    args = parser.parse_args()

    # Run the main function with parsed arguments
    run(f"{args.robot_ip}:{args.robot_port}", args.linear_velocity,
        args.angular_velocity)
