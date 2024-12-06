<p align="center">
    <img width="720" src="x-linux-azure-logo.png">
</p>

X-LINUX-AZURE is an STM32 MPU OpenSTLinux Expansion Package that targets Microsoft Azure IoT Edge for STM32MP25xx product microprocessors.  

It integrates IoT Edge runtime modules to turn STM32MP25 into an IoT Edge device to start and accelerate the development of an IoT solution.  

In addition, this OpenSTLinux Expansion Package provides good security practices with the integration of a secure solution for credential storage. This solution is based on the usage of OP-TEE and TPM.  

X-LINUX-AZURE includes a grapical demonstration application which interacts with IoT edge runtime to display configuration, list and restart installed modules.

# meta-st-x-linux-azure
X-LINUX-AZURE OpenEmbedded meta layer to be integrated into OpenSTLinux distribution.  
It contains recipes for Microsoft Azure IoT Edge integration with OP-TEE, TPM and application example.

## Compatibility
The X-LINUX-AWS OpenSTLinux Expansion Package is compatible with the Yocto Project™ build system and is validated over the OpenSTLinux Distribution.

| X-LINUX-AZURE Version | Git Branch     | OpenSTLinux Distribution Version | Boards 
|----------             |--------        |----------                        |--------    
| v6.0.x                | scarthgap      | v6.0.x                           | STM32MP257F-EV1<br>STM32MP257F-DK
| v5.1.x                | mickledore     | v5.1.x                           | STM32MP257F-EV1

## Versioning
Since its release v5.1.0, the major and minor versions of the X-LINUX-AZURE OpenSTLinux Expansion Package are aligned on the major and minor versions of the OpenSTLinux Distribution. This prevents painful backward compatibility attempts and makes dependencies straightforward.

The X-LINUX-AZURE generic versioning v**x**.**y**.**z** is built as follows:
* **x**: major version matching the OpenSTLinux Distribution major version. Each new major version is incompatible with previous OpenSTLinux Distribution versions.
* **y**: minor version matching the OpenSTLinux Distribution minor version. Each new minor version might be incompatible with previous OpenSTLinux Distribution versions.
* **z**: patch version to introduce bug fixes. A patch version is implemented in a backward compatible manner.

## Further information on X-LINUX-AZURE Expansion Package
<https://wiki.st.com/stm32mpu/wiki/X-LINUX-AZURE_Expansion_Package>

## Further information on how to install and how to use X-LINUX-AZURE Starter package
<https://wiki.st.com/stm32mpu/wiki/X-LINUX-AZURE_Starter_package>

## Further information on how to install and how to use X-LINUX-AZURE Distribution package
<https://wiki.st.com/stm32mpu/wiki/X-LINUX-AZURE_Distribution_package>

