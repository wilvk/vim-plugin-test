if !has('python3')
  echo "Error: python3 not detected in vim"
  finish
endif

function! GdbStart()
  py3file plugin/start_gdb.py
endfunc

command! GdbStart call GdbStart()
