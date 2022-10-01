#!/bin/zsh

get_nc_output(){
  nc saturn.picoctf.net 53935 < msg.txt
}

get_nc_output | tail -1