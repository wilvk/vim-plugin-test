if !has('python3')
  echo "Error: python3 not detected in vim"
  finish
endif

function! GReg()
  py3file plugin/test.py
endfunc

python3 << EOF
print("It worked!")
EOF
