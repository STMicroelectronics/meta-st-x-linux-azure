DESCRIPTION+="\
Customized by X-LINUX-AZURE to \
create a tpm2_pkcs11 directory in /etc/ to avoid \
storing tpm2 pkcs11 context in $HOME directory \
when TPM2_PKCS11_STORE is not defined."

do_install:append() {
    install -d ${D}/etc/tpm2_pkcs11
}

FILES:${PN} += "/etc/tpm2_pkcs11/"

PR = "r1"
