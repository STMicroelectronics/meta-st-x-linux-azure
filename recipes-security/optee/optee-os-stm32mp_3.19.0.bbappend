DESCRIPTION += "\
Customized by X-LINUX-AZURE \
to support sign operation with PKCS11_CKM_RSA_X_509 mechanism."

FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI += "file://0001-ta-pkcs11-add-CKM_RSA_X_509-sign-operations.patch "

PR = "r1"
