load("@grpc//bazel:python_rules.bzl", "py_grpc_library", "py_proto_library")
load("@rules_proto//proto:defs.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "status_proto",
    srcs = ["status.proto"],
    deps = [
        ":robot_proto",
        "//bearrobotics/api/v0/common:math_proto",
    ],
)

py_proto_library(
    name = "status_py_proto",
    deps = [":status_proto"],
)

proto_library(
    name = "robot_proto",
    srcs = ["robot.proto"],
)

py_proto_library(
    name = "robot_py_proto",
    deps = [":robot_proto"],
)

proto_library(
    name = "network_proto",
    srcs = ["network.proto"],
)

py_proto_library(
    name = "network_py_proto",
    deps = [":network_proto"],
)

proto_library(
    name = "system_proto",
    srcs = ["system.proto"],
    deps = [":network_proto"],
)

py_proto_library(
    name = "system_py_proto",
    deps = [":system_proto"],
)

proto_library(
    name = "robot_api_service_proto",
    srcs = [
        "robot_api_service.proto",
    ],
    deps = [
        ":network_proto",
        ":robot_proto",
        ":status_proto",
        ":system_proto",
        "//bearrobotics/api/v0/common:annotations_proto",
        "//bearrobotics/api/v0/common:math_proto",
    ],
)

py_proto_library(
    name = "robot_api_service_py_proto",
    deps = [":robot_api_service_proto"],
)

py_grpc_library(
    name = "robot_api_service_py_grpc",
    srcs = [":robot_api_service_proto"],
    deps = [":robot_api_service_py_proto"],
)
