"""File containing abstract class for CPIX clients."""

import abc
import os

from google.cloud import secretmanager


class CpixClient(abc.ABC):
  """Abstract class for CPIX clients."""

  @abc.abstractmethod
  def fetch_keys(self, media_id, key_ids):
    """Fetches encryption keys and prepares JSON content to be written to Secret Manager.

    Args:
      media_id (string): Name for your asset, sometimes used by DRM providers to
        show usage and reports.
      key_ids (string[]): List of IDs of any keys to fetch and prepare.

    Returns:
      dict: Object containing key information to be written to Secret Manager.
    """

  @property
  @abc.abstractmethod
  def required_env_vars(self):
    """Returns environment variables which must be set to use the class.

    The `PROJECT` env var is always required and does not need to be included
    in the returned list.

    Returns:
      list: list of strings, names of environment variables which must be
        set.
    """

  def access_secret_version(self, secret_id, version_id):
    client = secretmanager.SecretManagerServiceClient()
    secret_name = 'projects/{}/secrets/{}/versions/{}'.format(
        os.environ.get('PROJECT'), secret_id, version_id)
    response = client.access_secret_version(name=secret_name)
    return response.payload.data.decode().replace('\r\n', '\n')
