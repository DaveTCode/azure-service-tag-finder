# Find Azure Service Tag for an IP

This is a simple script repository that contains a single python script (no external dependencies) which can be executed as follows:

```bash
python3 check_azure_service_tag_for_ip.py uksouth 51.142.168.123
AzureCloud: 51.142.128.0/18
AzureCloud.ukwest: 51.142.128.0/18
```

## Requirements

- python3.3+
- `az` cli tool installed and logged in
