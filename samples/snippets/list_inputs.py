#!/usr/bin/env python

# Copyright 2022 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Live Stream sample for listing all inputs in a location.
Example usage:
    python list_inputs.py --project_number <project-number> --location <location>
"""

# [START livestream_list_inputs]

import argparse

from google.cloud.video.live_stream_v1.services.livestream_service import (
    LivestreamServiceClient,
)


def list_inputs(project_number, location):
    """Lists all inputs in a location.
    Args:
        project_number: The GCP project number.
        location: The location of the inputs."""

    client = LivestreamServiceClient()

    parent = f"projects/{project_number}/locations/{location}"
    page_result = client.list_inputs(parent=parent)
    print("Inputs:")

    responses = []
    for response in page_result:
        print(response.name)
        responses.append(response)

    return responses


# [END livestream_list_inputs]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project_number", help="Your Cloud project number.", required=True
    )
    parser.add_argument(
        "--location",
        help="The location of the inputs.",
        required=True,
    )
    args = parser.parse_args()
    list_inputs(
        args.project_number,
        args.location,
    )
