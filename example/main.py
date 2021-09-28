from cloud_functions_utils import decode


def main(event, context):
    data = decode(event["data"])
    print(data)
