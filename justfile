export EDITOR := 'nvim'

default:
  just --list

fmt:
	yapf --in-place --recursive **/*.py bin/*

compile:
  ./bin/compile
