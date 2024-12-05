load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "drive_robot",
    srcs = ["drive_robot.py"],
    deps = [
        "//bearrobotics/api/v0/common:annotations_py_proto",
        "//bearrobotics/api/v0/common:math_py_proto",
        "//bearrobotics/api/v0/robot:robot_api_service_py_grpc",
        "//bearrobotics/api/v0/robot:robot_api_service_py_proto",
        "@grpc//src/python/grpcio/grpc:grpcio",
    ],
)

py_binary(
    name = "get_system_info",
    srcs = ["get_system_info.py"],
    deps = [
        "//bearrobotics/api/v0/common:annotations_py_proto",
        "//bearrobotics/api/v0/robot:robot_api_service_py_grpc",
        "//bearrobotics/api/v0/robot:robot_api_service_py_proto",
        "@grpc//src/python/grpcio/grpc:grpcio",
    ],
)
