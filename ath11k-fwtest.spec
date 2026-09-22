%global debug_package %{nil}

Name:           ath11k-fwtest
Version:        1.0.0
Release:        1%{?dist}
Summary:        Firmware test utility for Qualcomm WLAN devices

License:        Qualcomm.nologin.binaries.license
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/wlan-service.qclinux.0.0/260630.1/prebuilt_resolute/%{name}_%{version}_arm64.tar.gz

ExclusiveArch:  aarch64

%description
ath11k-fwtest is a command-line utility for testing Qualcomm WLAN
firmware. It sends firmware test commands through the wireless driver
to support firmware testing and debugging.

%prep
%autosetup -c -n %{name}-%{version}

%build
# Prebuilt payload package: nothing to compile.

%install
mkdir -p %{buildroot}
cp -a data/%{name}/arm64/. %{buildroot}/
find %{buildroot} \( -type f -o -type l \) -printf '/%%P\n' | sort > %{name}.files

%files -f %{name}.files

%changelog
* Fri Aug 21 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.0-1
- Initial prebuilt RPM packaging
