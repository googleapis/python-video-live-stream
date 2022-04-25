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

"""Google Cloud Live Stream sample for deleting a channel.
Example usage:
    python delete_channel.py --project_number <project-number> --location <location> --channel_id <channel-id>
"""

# [START livestream_delete_channel]

import argparse

from google.cloud.video.live_stream_v1.services.livestream_service import (
    LivestreamServiceClient,
)


def delete_channel(project_number, location, channel_id):
    """Deletes a channel.
    Args:
        project_number: The GCP project number.
        location: The location of the channel.
        channel_id: The user-defined channel ID."""

    client = LivestreamServiceClient()

    name = f"projects/{project_number}/locations/{location}/channels/{channel_id}"
    response = client.delete_channel(name=name)
    print("Deleted channel")

    return response


# [END livestream_delete_channel]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project_number", help="Your Cloud project number.", required=True
    )
    parser.add_argument(
        "--location",
        help="The location of the channel.",
        required=True,
    )
    parser.add_argument(
        "--channel_id",
        help="The user-defined channel ID.",
        required=True,
    )
    args = parser.parse_args()
    delete_channel(
        args.project_number,
        args.location,
        args.channel_id,
    )
