# KMIP Python Client (CipherTrust Manager)

Example Python client for interacting with  **Thales CipherTrust Manager (KMIP)** using mutual TLS (mTLS). This example Python client demonstrates how to interact with Thales CTM (KMIP) using mutual TLS(mTLS).It can be used to validate KMIP connectivity, certificate authentication, and basic communication with CipherTrust Manager before implementing a full integration.

Tested on:

- RHEL 9.7
- Python 3.11
- PyKMIP (legacy compatibility workaround applied)

---

## Features

- KMIP connection over TLS
- Mutual TLS authentication (client certificate)
- AES key creation
- Key retrieval
- Compatible with modern Python (3.11+)


## Requirements

On RHEL 9.7

```
sudo subscription-manager repos --enable=rhel-9-for-x86_64-appstream-rpm
subscription-manager register
subscription-manager attach
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
## Certificates Setup
```
 mkdir -p /opt/kmip
 mkdir -p /opt/kmip/tenant_a
 mkdir -p /opt/kmip/ca

 /opt/kmip/ca/ctm_ca.pem          # Root CA ONLY
 /opt/kmip/tenant_a/client.pem    # Taken from 'Registered Clients' KMIP on CTM
 /opt/kmip/tenant_a/client.key    # Taken from 'Registered Clients' KMIP on CTM
```
## Rebuild system'CA Trust store
```
cp /opt/kmip/ca/ctm_ca.pem /etc/pki/ca-trust/source/anchors/
update-ca-trust extract
```
## Add entry in /etc/hosts related cn of kmip ca
```
 openssl s_client -connect <ip-CTM>:5696 -showcerts

  ................................................

  ..............  CN=kmip.ciphertrustmanager.local

  .................................................

echo "kmip.ciphertrustmanager.local <IP-CTM>" >>/etc/hosts
```
## Verify CA 
```
openssl s_client -connect kmip.ciphertrustmanager.local:5696 -CAfile /opt/kmip/ca/ctm_ca.pem

Expected: Verify return code: 0 (OK)
```
## Configuration
```
Edit kmip_test.py:

CTM_HOST = "kmip.ciphertrustmanager.local"
CTM_PORT = 5696


## Clone Repository


```bash
git clone https://github.com/pirainoa84-dot/kmip-python-client.git
cd kmip-python-client

python3.11 -m venv kmip-env
source kmip-env/bin/activate
  pip install --upgrade pip
  pip install pykmip==0.10.0


``````
### Run

```
(kmip-env) [root@kkmip]# python kmip_test.py

=== KMIP TEST ===
[OK] Connessione stabilita
[OK] Key created: 44e234f5e2a445adb04570b2132a226e5c650c80542f4faa9f090e36e99d6f79
[OK] Key retrieved: None
```
### On CTM

Log in on CTM webUi with the domain user and under keys section verify the presence of the key 
