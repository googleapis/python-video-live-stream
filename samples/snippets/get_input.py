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

"""Google Cloud Live Stream sample for getting an input.
Example usage:
    python get_input.py --project_number <project-number> --location <location> --input_id <input-id>
"""

# [START livestream_get_input]

import argparse

from google.cloud.video.live_stream_v1.services.livestream_service import (
    LivestreamServiceClient,
)


def get_input(project_number: str, location: str, input_id: str) -> str:
    """Gets an input.
    Args:
        project_number: The GCP project number.
        location: The location of the input.
        input_id: The user-defined input ID."""

    client = LivestreamServiceClient()

    name = f"projects/{project_number}/locations/{location}/inputs/{input_id}"
    response = client.get_input(name=name)
    print(f"Input: {response.name}")

    return response


# [END livestream_get_input]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project_number", help="Your Cloud project number.", required=True
    )
    parser.add_argument(
        "--location",
        help="The location of the input.",
        required=True,
    )
    parser.add_argument(
        "--input_id",
        help="The user-defined input ID.",
        required=True,
    )
    args = parser.parse_args()
    get_input(
        args.project_number,
        args.location,
        args.input_id,
    )
