##A PowerShell script is a text file containing commands and control constructs. The commands are invocations of cmdlets. 
##The control constructs are programming features like loops, variables, parameters, comments, etc. supplied by PowerShell.

##PowerShell script files have a .ps1 file extension. You can create and save these files with any text editor.

# Import the Azure Powershell module

Import-Module -Name Az

# Connect to an Azure account

Connect-AzAccount

# Define Azure variables for a vm

$vmName = "wingtiptoysVM"
$resourceGroup = "wingtiptoysRG"

# Create Azure credentials

$adminCredential = Get-Credential -Message "Enter a username and password for the VM administrator."

# Create a VM in Azure

New-AzVm -ResourceGroupName $resourceGroup -Name $vmName -Credential $adminCredential -Image UbuntuLTS

