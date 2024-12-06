DESCRIPTION += "\
Customized by X-LINUX-AZURE \
to support PKCS11_CKM_RSA_X_509 mechanism \
and fix libckteec memory allocation leakage on template serialization."

FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI += " \
    file://0001-Support-of-PKCS11_CKM_RSA_X_509-mechanism.patch \
    file://0002-libckteec-fix-memory-allocation-leakage-on-template-serialization.patch \
"

PR = "r2"
