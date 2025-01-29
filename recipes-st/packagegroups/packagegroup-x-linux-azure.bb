SUMMARY = "X-LINUX-AZURE full components"

PACKAGE_ARCH = "${MACHINE_ARCH}"

PV = "6.0"

inherit packagegroup

PROVIDES = "${PACKAGES}"
PACKAGES = "\
    packagegroup-x-linux-azure                  \
"

# Manage to provide all framework tools base packages with overall one
RDEPENDS:packagegroup-x-linux-azure = "\
    iotedge                                            \
    aziotctl                                           \
    aziot-edged                                        \
    aziot-keys                                         \
    aziotd                                             \
    docker                                             \
    connman                                            \
    connman-client                                     \
    optee-os-stm32mp-ta-pkcs11 (>= 4.0.0-stm32mp-r1-r2)\
    optee-client (>= 4.0.0+git0+acb0885c11-r2)         \
    opensc                                             \
    pcsc-lite                                          \
    pkcs11-provider (>= 0.5-r1)                        \
    demo-application-azure                             \
"

