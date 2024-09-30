require recipes-st/images/st-image-weston.bb

SUMMARY = "OpenSTLinux Azure IotEdge image based on weston image"

# Define ROOTFS_MAXSIZE (ext4)
IMAGE_ROOTFS_MAXSIZE = "2097152"

# Define partition size of ROOTFS 
# 8 * 1024 * 1024
FLASHLAYOUT_PARTITION_SIZE:sdcard:${STM32MP_ROOTFS_LABEL}     = "8388608"

#
# INSTALL addons
#

CORE_IMAGE_EXTRA_INSTALL += " \
     packagegroup-x-linux-azure \
     "

IMAGE_INSTALL:remove = " \
     acl-dev \
     attr-dev \
     bash-completion-dev \
     bash-dev \
     cracklib-dev \
     cryptodev-linux-dev \
     gawk-dev \
     libc6-dev \
     libcap-dev \
     libcrypt-dev \
     libgcc-s-dev \
     libgmp-dev \
     libgpg-error-dev \
     libpam-dev \
     libreadline-dev \
     libstdc++-dev \
     libtss2-dev \
     libtss2-mu-dev \
     libz-dev \
     linux-libc-headers-dev \
     ncurses-dev \
     openssl-dev \
     perl-dev \
     shadow-dev \
     tpm2-tss-engine-dev \
     "
