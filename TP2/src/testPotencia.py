Int potencia = Potencia(){
   read(b)
   read(c)
   Int d = 1

   for(Int c = c;c>0;Int c = c - 1){
      Int d = d * b
   }
   return d
}

Resultado(){
   Int h = potencia + 1
   write h
}

run()