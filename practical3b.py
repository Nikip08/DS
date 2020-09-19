def hanoi(ndisks,startpeg,endpeg):
      if ndisks:
             hanoi(ndisks-1,startpeg,3-startpeg-endpeg)
             print("move disk",ndisk-1,"to peg",endpeg)
             hanoi(ndisks-1,3-startpeg-endpeg)


hanoi(4,0,2)
