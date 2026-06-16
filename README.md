## Requirements
On https://developers.redhat.com/register 
Use account for test: Red Hat Developer Subscription for Individuals

On RHEL 9.7

```

https://developers.redhat.com/register


# Check current status
subscription-manager status

# Register system
sudo subscription-manager register

# Attach subscription
sudo subscription-manager attach --auto

# Enable required repositories
sudo subscription-manager repos --enable=rhel-9-for-x86_64-baseos-rpms
sudo subscription-manager repos --enable=rhel-9-for-x86_64-appstream-rpm

# Verify repositories
dnf repolist


dnf install -y python3.11 python3.11-devel
pip install --upgrade pip
dnf install -y     openssl     ca-certificates     curl     git     gcc     make     python3     python3-pip
dnf install -y python3.11 python3.11-devel

python3.11 -m venv kmip-env
source kmip-env/bin/activate
  pip install --upgrade pip
  pip install pykmip==0.10.0
```
