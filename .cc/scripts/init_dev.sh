#!/bin/bash

if [ "${BASH_ARGC}" != "1" ]
then
  virtualenv_dir="__"
else
  virtualenv_dir="${BASH_ARGV[0]}"
fi

the_basename=`basename \`pwd\``

echo "virtualenv_dir: ${virtualenv_dir} the_basename: ${the_basename}"

if [ ! -d ${virtualenv_dir} ]
then
  echo "no ${virtualenv_dir}. will create one"
  virtualenv -p `which python3` --prompt="[${the_basename}] " "${virtualenv_dir}"
fi

source ${virtualenv_dir}/bin/activate
the_python_path=`which python`
echo "python: ${the_python_path}"

echo "current_dir: "
pwd

# cp all to current dir
rm -rf .cc/.git*
ln -s .cc/scripts ./

# post setup - git

# gitignore
if [ ! -f .gitignore ]
then
    echo "/${virtualenv_dir}" >> .gitignore
fi

# requirements-dev.txt
if [ ! -f requirements-dev.txt ]
then
    cp .cc/requirements-dev.txt requirements-dev.txt
fi

git init; git add .; git commit -m "init dev"

# requirements-dev
pip install -r requirements-dev.txt
