from google.protobuf import timestamp_pb2

seconds_per_day = 86400


def is_resource_stale(create_time):
    """Checks the create timestamp to see if the resource is stale (and should be deleted).
    Args:
        create_time: Creation time in Timestamp format."""
    timestamp = timestamp_pb2.Timestamp()
    timestamp.FromDatetime(create_time)
    now = timestamp_pb2.Timestamp()
    now.GetCurrentTime()
    if (now.seconds - timestamp.seconds) > (2 * seconds_per_day):
        return True
    else:
        return False
