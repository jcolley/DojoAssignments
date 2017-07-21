#!/bin/bash
#title			:djanGO.sh
#description	:creates django project enviornment.
#author			:John Colley
#date			:20170619
#version		:1.1
#usage			:bash djanGO.sh
#note			:run this from your django projects directory

clear
prompt="?"
title="Is your terminal inside a virtualenv?"
options=("Yes" "No")

echo "$title"
PS3="$prompt "
select opt in "${options[@]}" "Quit"; do
	case "$REPLY" in
	
	1 ) echo "Great! Let's continue..."; break;;
	2 ) echo "Start your virutalenv first, then try again!"; exit;;
	3 ) echo "Quitting!"; exit;;
	
	esac
done

djanGOAppDir="$(pwd)/djanGOres/apps/"

if [ ! -d "$djanGOAppDir" ]; then
  mkdir -p ./djanGOres/apps
  
fi
echo ""
echo ""
title="Do you use one of these code editors?"
options=("atom" "nano" "VSCode" "sublime" "Nope, none of these")
echo "$title"
PS3="$prompt "
select opt in "${options[@]}" "Quit";
do
	case "$REPLY" in

	1 ) editor="atom"; cmd=(atom .); echo "nice choice"; break;;
	2 ) editor="nano"; cmd=(nano .); echo "nice choice"; break;;
	3 ) editor="code"; cmd=(code .); echo "nice choice"; break;;
	4 ) editor="sublime"; cmd=(sublime .); echo "nice choice"; break;;
	5 ) editor="none"; echo "fair enough"; break;;
	6 ) echo "Quitting!"; exit;;

	esac
done

echo ""
echo ""
echo Enter a project name:
read projectName
echo ""
echo ""
echo Enter an app name:
read appName
clear
echo "Creating directory structure"

projDir="$(pwd)/$projectName"
projAppDir="$projDir/apps"

django-admin startproject $projectName

mkdir -p ./$projectName/apps

cd ./$projectName/apps

python ../manage.py startapp $appName

cd $djanGOAppDir

function addApp {
	cp -R $1 "$projAppDir/$1"
}

clear
while :
do
	echo "Do you want to add existing apps to this project?"
	select yn in "Yes" "No";
	do
		case $yn in
			Yes ) select d in */ "Quit"; do test -n "$d" && break; echo ">>> Invalid Selection"; done; addApp $d && clear echo "Add another?" && break;;
			No ) break 2;;
		esac
		clear
		echo "Add another?"
	done
done

cd $projAppDir

cd ..

mkdir -p ./apps/$appName/templates/$appName ./apps/$appName/static/$appName/css ./apps/$appName/static/$appName/js ./apps/$appName/static/$appName/img

touch ./apps/__init__.py ./apps/$appName/urls.py ./apps/$appName/templates/$appName/index.html

python ./manage.py migrate

if [ $editor != "none" ]
then
	"${cmd[@]}"
fi

python manage.py runserver
