# CS  410/510 Winter 2019 SFTP Client

Python 3 SFTP client for our CS410/510 - Agile Software Development at Portland State University.

## Contributors

Shweta Paliwal <spaliwal@pdx.edu>

Molly Shove <mshove@pdx.edu>

Daniel Connelly <danc2@pdx.edu>

Dylan Laufenberg <lauf@pdx.edu>

Andrew Wyatt <wyat2@pdx.edu>

Anthony Namba <anamba@pdx.edu>

## Running the client

To run the client from the terminal, run one of two commands:
1) python3 main.py username@host
2) python3 main.py host
   - Leaving out username places the Linux environment's username into the host's username.
   
Each command requires you enter a password after the initial entry.

## Running the tests

Our tests are located in the [tests](tests) folder. To run the tests through the terminal, just run "pytest" from the project's root folder. (Be sure to create tests/test_server.py with the constants HOSTNAME, USERNAME, and PASSWORD first.)

## Libraries

We heavily relied on the following libraries:<br></br>
<b>Software Development</b>: pysftp and paramiko. <br></br>
<b>Testing</b>: pytest.<br></br>
