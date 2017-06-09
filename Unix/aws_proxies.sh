function proxy_on() {
    export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com,.XXX.com"

    echo -n "eid: "
    read -e eid
    echo -n "password: "
    read -es password

    local pre="$id:$password"

    export http_proxy="http://$pre@proxy.XXX.com:8099/"
    export https_proxy=$http_proxy
    export ftp_proxy=$http_proxy
    export rsync_proxy=$http_proxy
    export HTTP_PROXY=$http_proxy
    export HTTPS_PROXY=$http_proxy
    export FTP_PROXY=$http_proxy
    export RSYNC_PROXY=$http_proxy
    echo -e "proxy enabled"
}

function proxy_off() {
    unset http_proxy
    unset https_proxy
    unset ftp_proxy
    unset rsync_proxy
    unset HTTP_PROXY
    unset HTTPS_PROXY
    unset FTP_PROXY
    unset RSYNC_PROXY
    echo -e "proxy disabled"
}
