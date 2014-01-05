#! /bin/bash

cd "$(dirname $0)/../paleodeepdive.language";
ROOT_PATH=`pwd`

$ROOT_PATH/../gtgt/prepare_data.sh
env JAVA_OPTS="-Xmx4g" sbt "run -c $ROOT_PATH/../gtgt/application.conf"
