export EDITOR := 'nvim'

default:
  just --list

alias c := compile
alias f := fmt

fmt:
	yapf --in-place --recursive **/*.py bin/*

compile:
  ./bin/compile
