# Simulator PoC

### Idea

There will be 5 major components:
1. Compiler process (for specific languages)
2. Player process
3. Driver process
4. Manager process
5. Server interop

There will be 2 articles we need to deal with:
1. Player code
2. Game logs

#### Player code

Player code can be written in any language(theoretically). For the purposes of this PoC, we will use C++, Java and Python. The started code given to the player will consist of helper functions that handle the I/O and pass the state to an incomplete function, which the player will complete with their strategy. The coding experience can be thought of as an 

 #### Game logs

 There will be 2 game logs: one for each player process, which would basically be the output of the respective player process. It will also contain the error logs if the player process crashes.


#### Compiler process

This will be an ephemeral docker container that will compile the player code. The player code is preferably passed in through stdin. The stdout and stderr of the process will be watched for warnings and errors. Preferably the diagnostic messages will be obtained as a json file to be sent to the user's monaco editor. The compiled artifacts will be retrieved preferably through stdout or through a mounted temp file.

#### Player process

This will be an ephemeral docker container that will run the player binary/code. The stdin and stdout of the process are managed by the driver process. The container will be of a distroless image to reduce bloat.

#### Driver process

This will be an ephemeral docker container which will manage the inputs and outputs of the two player processes. It will provide the initial state, interchange state changes across the two player processes and calculate the final scores and verdict of a match. It will also manage the game logs.

It provides the input to the player processes by piping it to the input fifo connected to the player process. It retrieves the output from the player processes by listening to the output fifo connected to the player process.

It also handles the termination of the player processes in case of timeout, runtime errors, memory or compute constraint violations, premature termination of the other player process, etc. and generates actionable error  reports.

#### Manager process

This will be a long running process which receives the match requests, spins up the containers for the compiler, player and driver processes, passes on the information required to build the initial state to the driver process, creates the fifos which are to be used by the player processes, retrieves the final verdict/error information from the driver process, and performs cleanup after the match is completed.


#### Server interop

This is the interface between the server and the simulator. It will process the match queue and starts the matches. It also parses the match results and player logs and sends them to the server.


## PoC

This will be an interactive calculator game. The player will receive equations from the opponent and will have to send back the result of the equation and has to send a new equation to the opponent. The number of turns will be 500. The player who solves the most equations will win. Players sending invalid equations will be penalized.

