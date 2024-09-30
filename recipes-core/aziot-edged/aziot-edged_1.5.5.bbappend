DESCRIPTION += "\
Customized by X-LINUX-AZURE \
to add aziotks user to teeclnt group, \
to add aziotks user to tss group, \
to change ownership of tpm2_pkcs11 context directory."

pkg_postinst_ontarget:${PN}() {
    chown aziotks:aziotks /etc/tpm2_pkcs11/
    touch /etc/tpm2_pkcs11/tpm2_pkcs11.sqlite3
    chown aziotks:aziotks /etc/tpm2_pkcs11/tpm2_pkcs11.sqlite3
    groupmems -g teeclnt -a aziotks
    groupmems -g tss -a aziotks
}

pkg_prerm:${PN}() {
    rm /etc/tpm2_pkcs11/tpm2_pkcs11.sqlite3
    groupmems -g teeclnt -d aziotks
    groupmems -g tss -d aziotks
}


DEPENDS += "\
    optee-client \
    tpm2-pkcs11 \
    tpm2-tss \
    "

RDEPENDS:${PN} += "\
    optee-client \
    tpm2-pkcs11 \
    tpm2-tss \
    "


PR = "r1"
