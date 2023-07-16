ipAddress: str = "localhost" # This will be used in the generated links. Useful if you want to use a tunneling service or a domain. 
frontendPort: int = 5007 # This sets the port on which the frontend will listen.
loggerPort: int = 9586 # This sets the port on which the logger server will listen. 
                       # It will also appear in the generated links, too.
debugMode: bool = False
