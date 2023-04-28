@echo off                                                                                                                

echo  " __          ________ ____  _____    _______ ____    _____  _   _  _____ "
echo  " \ \        / /  ____|  _ \|  __ \  |__   __/ __ \  |  __ \| \ | |/ ____|"
echo  "  \ \  /\  / /| |__  | |_) | |__) |    | | | |  | | | |__) |  \| | |  __ "
echo  "   \ \/  \/ / |  __| |  _ <|  ___/     | | | |  | | |  ___/| . ` | | |_ |"
echo  "    \  /\  /  | |____| |_) | |         | | | |__| | | |    | |\  | |__| |"
echo  "     \/  \/   |______|____/|_|         |_|  \____/  |_|    |_| \_|\_____|"
                                                                         
                                                                         
                                                                                       
                                                                                                                  
                                                                                                                   
echo Quale versione vuoi aprire?
echo 1) Singolo
echo 2) Multipli

set /p choice=Scelta: 

if %choice% == 1 (
  start python singolo.py
) else if %choice% == 2 (
  start python multiplo.py
) else (
  echo Scelta non valida.
)
