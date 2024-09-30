SUMMARY = "X-LINUX-AZURE full components"

PACKAGE_ARCH = "${MACHINE_ARCH}"

PV = "5.1"

inherit packagegroup

PROVIDES = "${PACKAGES}"
PACKAGES = "\
    packagegroup-x-linux-azure                  \
"

# Manage to provide all framework tools base packages with overall one
RDEPENDS:packagegroup-x-linux-azure = "\
    iotedge                                     \
    aziotctl                                    \
    aziot-edged                                 \
    aziot-keys                                  \
    aziotd                                      \
    docker                                      \
    connman                                     \
    connman-client                              \
    optee-os-stm32mp-ta-pkcs11                  \
    optee-client (>= 3.19.0+git0+140bf46304-r1) \
    opensc                                      \
    pcsc-lite                                   \
    pkcs11-provider                             \
    demo-application-azure                      \
"

