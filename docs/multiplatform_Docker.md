# Multiplatform Docker

## Resources
https://www.docker.com/blog/faster-multi-platform-builds-dockerfile-cross-compilation-guide/

## Process
`# docker run --privileged --rm tonistiigi/binfmt --install all
Unable to find image 'tonistiigi/binfmt:latest' locally
latest: Pulling from tonistiigi/binfmt
8d4d64c318a5: Pull complete 
e9c608ddc3cb: Pull complete 
Digest: sha256:66e11bea77a5ea9d6f0fe79b57cd2b189b5d15b93a2bdb925be22949232e4e55
Status: Downloaded newer image for tonistiigi/binfmt:latest
installing: mips64le OK
installing: mips64 OK
installing: arm OK
installing: s390x OK
installing: riscv64 OK
installing: arm64 OK
installing: ppc64le OK
{
  "supported": [
    "linux/amd64",
    "linux/arm64",
    "linux/riscv64",
    "linux/ppc64le",
    "linux/s390x",
    "linux/386",
    "linux/mips64le",
    "linux/mips64",
    "linux/arm/v7",
    "linux/arm/v6"
  ],
  "emulators": [
    "cli",
    "jar",
    "llvm-10-runtime.binfmt",
    "python2.7",
    "python3.8",
    "qemu-aarch64",
    "qemu-arm",
    "qemu-mips64",
    "qemu-mips64el",
    "qemu-ppc64le",
    "qemu-riscv64",
    "qemu-s390x"
  ]
}
`

### Building multiplatform images
`docker buildx create --use`
then
`docker buildx build --platform=linux/x86_64,linux/arm/v7 .`

