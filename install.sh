#!/bin/bash

function installpackage(){

	if apt-get -qq install $pkg; then
	    echo "Successfully installed $pkg"
	else
	    echo "Error installing $pkg"
	fi

}

echo "Check install python"

pkg="python"
installpackage

echo "Check install pygame"

pkg="python-pygame"
installpackage

echo "Check install ffmpeg"

pkg="ffmpeg"
installpackage
