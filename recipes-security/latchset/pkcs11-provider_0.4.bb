SUMMARY = "This is an Openssl 3.x provider to access Hardware or Software Tokens using the PKCS#11 Cryptographic Token Interface"
HOMEPAGE = "https://github.com/latchset/pkcs11-provider"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM += "file://${COMMON_LICENSE_DIR}/Apache-2.0;md5=89aea4e17d99a7cacdbeed46a0096b10"

inherit meson pkgconfig

SRC_URI = "git://github.com/latchset/pkcs11-provider.git;protocol=https;branch=main"

FILESEXTRAPATHS:prepend := "${THISDIR}:"

SRC_URI += " \
    file://files/openssl-pkcs11-provider-optee.cnf \
    file://files/openssl-pkcs11-provider-tpm2.cnf \
    file://files/pin.txt \
"

SRCREV = "d8e2823bee2268782ec70036618622ee7e87749e"

DEPENDS = "\
    openssl \
    autoconf-archive-native \
    libtool \
    pkgconfig \
    "

S = "${WORKDIR}/git"

do_install:append() {
    install -d ${D}/etc/pki/
    install -m 0755 ${WORKDIR}/files/openssl-pkcs11-provider-optee.cnf ${D}/etc/pki/openssl-pkcs11-provider-optee.cnf
    install -m 0755 ${WORKDIR}/files/openssl-pkcs11-provider-tpm2.cnf ${D}/etc/pki/openssl-pkcs11-provider-tpm2.cnf
    install -m 0755 ${WORKDIR}/files/pin.txt ${D}/etc/pki/pin.txt
}


RDEPENDS:${PN} += "\
    openssl \
    "
    
FILES:${PN} += "\
    /usr/ \
    "
