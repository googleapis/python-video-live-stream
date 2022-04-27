from google.cloud import resourcemanager_v3
from google.protobuf import timestamp_pb2


seconds_per_hour = 3600


def is_resource_stale(create_time: str) -> bool:
    """Checks the create timestamp to see if the resource is stale (and should be deleted).
    Args:
        create_time: Creation time in Timestamp format."""
    timestamp = timestamp_pb2.Timestamp()
    timestamp.FromDatetime(create_time)
    now = timestamp_pb2.Timestamp()
    now.GetCurrentTime()
    if (now.seconds - timestamp.seconds) > (3 * seconds_per_hour):
        return True
    else:
        return False


def get_project_number(project_name: str) -> str:
    client = resourcemanager_v3.ProjectsClient()
    request = resourcemanager_v3.GetProjectRequest(
        name=f"projects/{project_name}"
    )
    response = client.get_project(request=request)
    str_slice = response.name.split("/")
    return str_slice[len(str_slice) - 1].rstrip("\n")
