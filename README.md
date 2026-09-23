<!--
Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
SPDX-License-Identifier: BSD-3-Clause
-->
# ath11k-fwtest RPM - CentOS Stream 10

ath11k-fwtest is a command-line utility for testing Qualcomm WLAN
firmware. It sends firmware test commands through the wireless driver
to support firmware testing and debugging.

This branch contains the CentOS Stream 10 RPM packaging for ath11k-fwtest from the Qualcomm Linux `260825/prebuilt_yocto` release tarball.

## Package

| Field | Value |
|---|---|
| Package | ath11k-fwtest |
| Summary | Firmware test utility for Qualcomm WLAN devices |
| Version | 1.0.0 |
| Source | qcom-ath11k-fwtest_1.0_armv8-2a.tar.gz |
| Source checksum | See sources |

The Yocto source archive version (`1.0`) is tracked separately from the RPM version.

The prebuilt payload installs:

- /usr/sbin/ath11k-fwtest

License documents are installed under `/usr/share/licenses/ath11k-fwtest/`
and marked as license files in the RPM:

- `NO.LOGIN.BINARY.LICENSE.QTI`
- `LICENSE`

The original copies are retained under `/usr/share/doc/qcom-ath11k-fwtest/`.

## Files

- ath11k-fwtest.spec
- sources
- .github/workflows/build-on-pr.yml
- .github/workflows/pkg-release.yml

Do not commit source tarballs or built RPMs. The source tarball is resolved from the dist-git `sources` file and the spec `Source0` URL.

## Build

Local validation can be run with qcom-rpm-utils:

    /path/to/qcom-rpm-utils/scripts/build-rpm.sh \
      --tarball /path/to/qcom-ath11k-fwtest_1.0_armv8-2a.tar.gz \
      --spec ath11k-fwtest.spec \
      --output /path/to/output

For CI, open a PR against this c10s branch. The build-on-pr workflow builds RPM artifacts but does not publish them.

## Release

After the PR is merged, run Actions -> Release on the c10s branch. The release workflow publishes the generated RPMs to Artifactory after approval.
