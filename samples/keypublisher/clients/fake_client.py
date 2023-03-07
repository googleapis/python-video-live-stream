"""File containing a fake CPIX client for demonstration purposes."""

import secrets

from . import cpix_client


class FakeClient(cpix_client.CpixClient):
  """Fake CPIX client, for demonstration purposes only."""

  def fetch_keys(self, media_id, key_ids):
    """Generates random key information.

    Args:
      media_id (string): Name for your asset, sometimes used by DRM providers to
        show usage and reports.
      key_ids (string[]): List of IDs of any keys to fetch and prepare.

    Returns:
      dict: Object containing key information to be written to Secret Manager.
    """
    key_info = dict()
    key_info['encryptionKeys'] = []
    for key_id in key_ids:
      fake_key = secrets.token_hex(16)
      key_info['encryptionKeys'].append({
          'keyId':
              key_id.replace('-', ''),
          'key':
              fake_key,
          'keyUri':
              'https://storage.googleapis.com/bucket-name/{}.bin'.format(
                  fake_key),
          'iv':
              secrets.token_hex(16),
      })
    return key_info

  def required_env_vars(self):
    return []
