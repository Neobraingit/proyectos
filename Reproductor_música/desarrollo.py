import Funciones

print ('''  o__ __o                                                              o                            o                             
 <|     v\                                                            <|>                          <|>                            
 / \     <\                                                           < \                          < >                            
 \o/     o/      o__  __o   \o_ __o    \o__ __o     o__ __o      o__ __o/   o       o       __o__   |        o__ __o    \o__ __o  
  |__  _<|      /v      |>   |    v\    |     |>   /v     v\    /v     |   <|>     <|>     />  \    o__/_   /v     v\    |     |> 
  |       \    />      //   / \    <\  / \   < >  />       <\  />     / \  < >     < >   o/         |      />       <\  / \   < > 
 <o>       \o  \o    o/     \o/     /  \o/        \         /  \      \o/   |       |   <|          |      \         /  \o/       
  |         v\  v\  /v __o   |     o    |          o       o    o      |    o       o    \\         o       o       o    |        
 / \         <\  <\/> __/>  / \ __/>   / \         <\__ __/>    <\__  / \   <\__ __/>     _\o__</   <\__    <\__ __/>   / \       
                            \o/                                                                                                   
                             |                                                                                                    
                            / \                                                                                                   ''')
print ('Elige una opción: \na \nb')
eleccion = input()
if eleccion == 'a':
    Funciones.reproductor()
else:
    Funciones.reproductor2()