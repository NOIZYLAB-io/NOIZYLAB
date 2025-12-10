## Installing and Licensing Parasoft C/C++test Standard

The C/C++test extension requires **Parasoft C/C++test Standard** to be installed on your system. See the sections below for installation and licensing information.

For download information or a free trial, contact us at info@parasoft.com or via our [website](https://www.parasoft.com/integrations/microsoft-visual-studio-code/).

### To install C/C++test Standard:
1. Unpack the installation package to a desired location. The `cpptest` directory that contains all C/C++test files will be created.

### To license C/C++test Standard:
1. Open the `cpptestcli.properties` file in the installation directory.
2. Customize the following license settings to configure a local license:
    - `cpptest.license.use_network=false`
    - `cpptest.license.local.password=[the password you received from Parasoft]`

For information about a network license and other details, see [Setting the Parasoft License](https://docs.parasoft.com/display/CPPTEST20252/Setting+the+License).

### To connect C/C++test Standard to Visual Studio Code:
1. Specify the C/C++test Standard installation directory using the [C/C++test Quick Start> Select C/C++test installation...](command:vscode-cpptest.selectInstallLocation) command.  
Alternatively, add the C/C++test Standard installation directory to the `PATH` system variable to enable access to the `cpptestcli` executable from anywhere on the system. This will enable C/C++test extension to launch C/C++test Standard from Visual Studio Code.

2. Before running analysis, be sure to select a test configuration and a compiler configuration for your project in [C/C++test Quick Start](command:vscode-cpptest.quickStart).  

For more information, see the C/C++test extension details page.
