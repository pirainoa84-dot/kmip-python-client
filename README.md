## Requirements
On RED HAT portal

https://developers.redhat.com/register 
use account for test: Red Hat Developer Subscription for Individuals

On RHEL 9.7

```
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

# Verify cn certificate kmip

openssl s_client -connect <IP-CTM>:5696 -showcerts
.......
             CN = kmip.ciphertrustmanager.local
.......
Result: OK
.......

# Insert entry in hosts file

echo "<CTM-IP> kmip.ciphertrustmanager.local" >>/etc/hosts

# Clone 
git clone https://github.com/pirainoa84-dot/kmip-python-client.git

# Python env
python3.11 -m venv kmip-env
source kmip-env/bin/activate
  pip install --upgrade pip
  pip install pykmip==0.10.0

#Run script kmip_test.py
(kmip-env) [root@kkmip-python-client]# python kmip_test.py

=== KMIP TEST ===
[OK] Connessione stabilita
[OK] Key created: a017df4a0f974caea58621577128a483cd9e22b4d62f4cf8a698c438fb926b5a
[OK] Key retrieved: None

```
