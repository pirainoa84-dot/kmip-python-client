# KMIP Python Client (CipherTrust Manager)
This script demonstrates how to connect to CipherTrust Manager (KMIP) using mTLS and perform basic key operations. It is intended for testing connectivity, validating certificates, and troubleshooting KMIP integration before implementing a full KMIP integration.

## Requirements

### Red Hat Account

Register on the Red Hat Developer Portal:

https://developers.redhat.com/register

Use the **Red Hat Developer Subscription for Individuals** for testing and lab environments (free for personal use).


### On RHEL 9.7

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

# Create dir
mkdir -p /opt/kmip
mkdir -p /opt/kmip/tenant_a # we'll put "client.pem" and  "client.key" relaated kmip ctm client
mkdir -p /opt/kmip/ca # weìll put "ctm_ca.pem" with default rootca ctm (not kmip ca)

# Copy Root CA ctm to system trust store directory

cp /opt/kmip/ca/ctm_ca.pem /etc/pki/ca-trust/source/anchors/

# Update CA trsust store

pdate-ca-trust extract

# Verify cn hostname certificate kmip and TLS connection 

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
