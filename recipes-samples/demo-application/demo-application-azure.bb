SUMMARY = "Add basic support of Azure IoT Edge on Demo Launcher"
HOMEPAGE = "wiki.st.com"
LICENSE = "BSD-3-Clause"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta/files/common-licenses/BSD-3-Clause;md5=550794465ba0ec5312d6919e203a55f9"

DEPENDS = "\
    demo-launcher \
    "

PV = "6.0"

SRC_URI = " \
    file://__init__.py \
    file://070-azure.yaml \
    file://connected-cloud.png \
    file://azure.py \
    file://sudoers.d/demo-application-azure \
    "

do_configure[noexec] = "1"
do_compile[noexec] = "1"

do_install() {
    install -d ${D}${prefix}/local/demo/application/azure/pictures
    install -d ${D}${prefix}/local/demo/gtk-application

    # install yaml file
    install -m 0644 ${WORKDIR}/*.yaml ${D}${prefix}/local/demo/gtk-application/
    # install pictures
    install -m 0644 ${WORKDIR}/*.png ${D}${prefix}/local/demo/application/azure/pictures
    # python script
    install -m 0755 ${WORKDIR}/*.py ${D}${prefix}/local/demo/application/azure/

    # add priviledges to application:
    install -d ${D}/${sysconfdir}/sudoers.d
    chmod 0750 ${D}/${sysconfdir}/sudoers.d
    install -m 0644 ${WORKDIR}/sudoers.d/demo-application-azure ${D}/${sysconfdir}/sudoers.d/demo-application-azure 
}

RDEPENDS:${PN} += "\
    python3-core \
    python3-pygobject \
    gtk+3 \
    python3-threading \
    demo-launcher \
    sudo \
    "

FILES:${PN} += "\
    ${prefix}/local/demo/application/ \
    ${prefix}/local/demo/gtk-application/ \
    ${sysconfdir}/sudoers.d/demo-application-azure \
    "

CORE_IMAGE_EXTRA_INSTALL += " \
    demo-application-azure \
    "
