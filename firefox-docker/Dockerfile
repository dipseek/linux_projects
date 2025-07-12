FROM quay.io/centos/centos:stream9

RUN dnf install -y \
    firefox \
    xorg-x11-server-Xorg \
    xorg-x11-xauth \
    xorg-x11-utils \
    gtk3 && \
    dnf clean all

ENV DISPLAY=:0
CMD ["firefox"]


