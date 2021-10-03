export EDITOR := 'nvim'

default:
  just --list

fmt:
	yapf --in-place --recursive **/*.py
