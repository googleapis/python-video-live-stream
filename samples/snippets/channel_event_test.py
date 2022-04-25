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

import os
import uuid

from google.cloud import storage
import pytest

import create_channel
import create_channel_event
import create_input
import delete_channel
import delete_channel_event
import delete_input
import get_channel_event
import list_channel_events
import start_channel
import stop_channel

project_name = os.environ["GOOGLE_CLOUD_PROJECT"]
project_number = os.environ["GOOGLE_CLOUD_PROJECT_NUMBER"]
location = "us-central1"
input_id = f"python-test-input-{uuid.uuid4()}"
channel_id = f"python-test-channel-{uuid.uuid4()}"
event_id = f"python-test-event-{uuid.uuid4()}"
output_bucket_name = f"python-test-bucket-{uuid.uuid4()}"
output_uri = f"gs://{output_bucket_name}/channel-test/"


@pytest.fixture(scope="module")
def test_bucket():
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(output_bucket_name)

    yield bucket
    bucket.delete(force=True)


def test_channel_event_operations(capsys, test_bucket):

    # Set up

    channel_name_project_id = (
        f"projects/{project_name}/locations/{location}/channels/{channel_id}"
    )

    event_name_project_id = f"projects/{project_name}/locations/{location}/channels/{channel_id}/events/{event_id}"
    event_name_project_number = f"projects/{project_number}/locations/{location}/channels/{channel_id}/events/{event_id}"

    create_input.create_input(project_number, location, input_id)

    create_channel.create_channel(
        project_number, location, channel_id, input_id, output_uri
    )
    out, _ = capsys.readouterr()
    assert channel_name_project_id in out

    start_channel.start_channel(project_number, location, channel_id)
    out, _ = capsys.readouterr()
    assert "Started channel" in out

    # Tests

    create_channel_event.create_channel_event(
        project_number, location, channel_id, event_id
    )
    out, _ = capsys.readouterr()
    assert event_name_project_id in out

    get_channel_event.get_channel_event(project_number, location, channel_id, event_id)
    out, _ = capsys.readouterr()
    assert event_name_project_number in out

    list_channel_events.list_channel_events(project_number, location, channel_id)
    out, _ = capsys.readouterr()
    assert event_name_project_number in out

    delete_channel_event.delete_channel_event(
        project_number, location, channel_id, event_id
    )
    out, _ = capsys.readouterr()
    assert "Deleted channel event" in out

    # Clean up

    stop_channel.stop_channel(project_number, location, channel_id)
    out, _ = capsys.readouterr()
    assert "Stopped channel" in out

    delete_channel.delete_channel(project_number, location, channel_id)
    out, _ = capsys.readouterr()
    assert "Deleted channel" in out

    delete_input.delete_input(project_number, location, input_id)
