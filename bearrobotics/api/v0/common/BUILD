load("@grpc//bazel:python_rules.bzl", "py_proto_library")
load("@rules_proto//proto:defs.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "annotations_proto",
    srcs = ["annotations.proto"],
    deps = ["@com_google_protobuf//:timestamp_proto"],
)

py_proto_library(
    name = "annotations_py_proto",
    deps = [":annotations_proto"],
)

proto_library(
    name = "math_proto",
    srcs = ["math.proto"],
)

py_proto_library(
    name = "math_py_proto",
    deps = ["math_proto"],
)
