# Qiskit-basics

# Quantum Computer
A quantum computer is any device for computation that makes direct use of distinctively quantum mechanical phenomena, such as superposition and entanglement, to perform operations on data.

In a classical (or conventional) computer, information is stored as bits; in a quantum computer, it is stored as qubits (quantum bits).
The basic principle of quantum computation is that the quantum properties can be used to represent and structure data, and that quantum mechanisms can be devised and built to perform operations with this data.
Although quantum computing is still in its infancy, experiments have been carried out in which quantum computational operations were executed on a very small number of qubits.
Research in both theoretical and practical areas continues at a frantic pace, and many national government and military funding agencies support quantum computing research to develop quantum computers for both civilian and national security purposes, such as cryptanalysis.

# Qiskit
Qiskit is an open-source framework for quantum computing. It provides tools for creating and manipulating quantum programs and running them on prototype quantum devices and simulators. It follows the circuit model for universal quantum computation, and can be used for any quantum hardware that follows this model.

Qiskit was founded by IBM Research to allow software development for their cloud quantum computing service. Contributions are also made by external supporters, typically from academic institutions. The primary version of Qiskit uses the Python programming language. Versions for Swift and JavaScripts are also available. These are used to create quantum programs based on the OpenQASM representation of quantum circuits.

# Requirements
Qiskit supports Python 3.5 or later.

Recommend installing Anaconda, a cross-platform Python distribution for scientific computing. Jupyter, included in Anaconda, is recommended for interacting with Qiskit.(you can also use PyCharm)

# Installation(Tested on windows, might work on macos and linux)
_If you're using Anaconda_

1. Search for Anaconda Prompt
2. Open Anaconda Prompt

_If you're using PyCharm or any other IDLE_

1. Open/Create a new project
2. Open the terminal in the IDLE 

**The below installation commands work for both Anaconda and any IDLE:**

Create a minimal environment with only Python installed in it.

Use the following commands:

`conda create -n name_of_my_env python=3.8`

_Note: As of now some components of qiskit are not installing for python version 3.8(latest), so it is recommended to install qiskit for python version 3.7.4_

`activate name_of_my_env`

`pip install qiskit`

There are optional dependencies that are required to use all the visualization functions available in Qiskit. You can install these optional dependencies by with the following command:

`pip install qiskit-terra[visualization]`

After you’ve installed and verified the Qiskit packages you want to use, import them into your environment with Python to begin working.

`import qiskit`

**Access IBM Q Systems**

To configure your account, you create a local configuration file which includes an API key

1. Create a free IBM Q Experience account.
2. Navigate to My Account to view your account settings.
3. Click on Copy token to copy the token to your clipboard. Temporarily paste this API token into your favorite text editor so you can use it later to create an account configuration file.
4. Run the following commands to store your API token locally for later use in a configuration file called qiskitrc. Replace MY_API_TOKEN with the API token value that you stored in your text editor.

`from qiskit import IBMQ`

`IBMQ.save_account('MY_API_TOKEN')`

**Checking which version is installed**

To see the versions of all the Qiskit elements in your environment you can use the `__qiskit_version__` attribute. For example, running the following command will return a dictionary that includes the versions for each of the installed Qiskit packages.

`qiskit.__qiskit_version__`

For a detailed instruction note refer: https://qiskit.org/documentation/install.html

# Quantum Basics

If you wish to know the fundamental concepts and basics things like quantum physics,linear algebra, quantum gates, etc. you can use this book. This book will guide you and explain all the fundamentals concepts you need to know to understand quantum computers and qiskit.

https://delapuente.github.io/qiskit-textbook/preface

# References 

https://en.wikipedia.org/wiki/Qiskit

https://qiskit.org/documentation/index.html