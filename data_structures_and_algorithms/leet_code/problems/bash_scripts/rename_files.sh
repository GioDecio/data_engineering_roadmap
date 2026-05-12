 cd ../
 for f in *.py; do    
      if [[ "$f" == _* ]]; then
          continue                                                                                                                                         
      fi
      mv "$f" "_$f"                                                                                                                                        
  done   